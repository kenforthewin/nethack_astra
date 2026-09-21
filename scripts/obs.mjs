#!/usr/bin/env node
// OBS WebSocket 5 control. Node 22+; no packages. Credentials stay in OBS.
import {readFile, mkdir, writeFile} from 'node:fs/promises';
import {createHash, randomUUID} from 'node:crypto';
import {homedir} from 'node:os';
import {fileURLToPath} from 'node:url';
import path from 'node:path';

const root = fileURLToPath(new URL('../', import.meta.url));
const sceneName = 'NetHack — CodexDelver';
const inputName = 'NetHack browser';
const command = process.argv[2] ?? 'status';
const hash = text => createHash('sha256').update(text).digest('base64');
let socket;
const pending = new Map();

async function connect() {
  const config = JSON.parse(await readFile(path.join(homedir(),
    'Library/Application Support/obs-studio/plugin_config/obs-websocket/config.json'), 'utf8'));
  if (!config.server_enabled) throw new Error('Enable the OBS WebSocket server in Tools → WebSocket Server Settings.');
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('OBS connection timed out.')), 8000);
    socket = new WebSocket(`ws://127.0.0.1:${config.server_port ?? 4455}`);
    socket.onmessage = event => {
      const {op, d} = JSON.parse(event.data);
      if (op === 0) {
        const identify = {rpcVersion: 1, eventSubscriptions: 0};
        if (d.authentication) identify.authentication = hash(
          hash(config.server_password + d.authentication.salt) + d.authentication.challenge);
        socket.send(JSON.stringify({op: 1, d: identify}));
      } else if (op === 2) {
        clearTimeout(timer);
        resolve();
      } else if (op === 7) {
        const request = pending.get(d.requestId);
        if (!request) return;
        clearTimeout(request.timer);
        pending.delete(d.requestId);
        if (d.requestStatus.result) request.resolve(d.responseData ?? {});
        else request.reject(new Error(`${d.requestType}: ${d.requestStatus.comment ?? d.requestStatus.code}`));
      }
    };
    socket.onerror = () => { clearTimeout(timer); reject(new Error('Could not connect to OBS.')); };
    socket.onclose = event => {
      clearTimeout(timer);
      const error = new Error(`OBS connection closed (${event.code}).`);
      reject(error);
      for (const request of pending.values()) {
        clearTimeout(request.timer);
        request.reject(error);
      }
      pending.clear();
    };
  });
}

function request(requestType, requestData = {}) {
  return new Promise((resolve, reject) => {
    const requestId = randomUUID();
    const timer = setTimeout(() => {
      pending.delete(requestId);
      reject(new Error(`${requestType} timed out.`));
    }, 10000);
    pending.set(requestId, {resolve, reject, timer});
    socket.send(JSON.stringify({op: 6, d: {requestType, requestId, requestData}}));
  });
}

async function status() {
  const [stream, record, video, scenes, audio] = await Promise.all([
    request('GetStreamStatus'), request('GetRecordStatus'), request('GetVideoSettings'),
    request('GetSceneList'), request('GetSpecialInputs')]);
  return {streaming: stream.outputActive, stream, recording: record.outputActive, video,
    currentScene: scenes.currentProgramSceneName, scenes: scenes.scenes.map(s => s.sceneName), audio};
}

async function setup() {
  const current = await status();
  if (current.streaming || current.recording) throw new Error('Stop the active output before changing video settings.');
  const response = await fetch('http://127.0.0.1:8766/state', {signal: AbortSignal.timeout(5000)});
  if (!response.ok) throw new Error('NetHack viewer is unavailable.');
  await request('SetVideoSettings', {baseWidth: 1920, baseHeight: 1080,
    outputWidth: 1920, outputHeight: 1080, fpsNumerator: 30, fpsDenominator: 1});
  if (!current.scenes.includes(sceneName)) await request('CreateScene', {sceneName});
  const {inputs} = await request('GetInputList');
  const inputSettings = {url: 'http://127.0.0.1:8766/', width: 1920, height: 1080,
    fps: 30, fps_custom: true, shutdown: false, restart_when_active: false};
  if (!inputs.some(input => input.inputName === inputName)) {
    await request('CreateInput', {sceneName, inputName, inputKind: 'browser_source', inputSettings,
      sceneItemEnabled: true});
  } else {
    await request('SetInputSettings', {inputName, inputSettings, overlay: true});
    const {sceneItems} = await request('GetSceneItemList', {sceneName});
    if (!sceneItems.some(item => item.sourceName === inputName)) {
      await request('CreateSceneItem', {sceneName, sourceName: inputName, sceneItemEnabled: true});
    }
  }
  await request('SetCurrentProgramScene', {sceneName});
  return status();
}

try {
  if (!['status', 'setup', 'screenshot', 'refresh', 'inspect', 'broadcast', 'start', 'stop'].includes(command)) throw new Error('Usage: node scripts/obs.mjs [status|setup|screenshot|refresh|inspect|start|broadcast MINUTES|stop]');
  await connect();
  if (command === 'status') console.log(JSON.stringify(await status(), null, 2));
  if (command === 'setup') console.log(JSON.stringify(await setup(), null, 2));
  if (command === 'stop') {
    if ((await request('GetStreamStatus')).outputActive) await request('StopStream');
    console.log('Stream stop requested.');
  }
  if (command === 'start') {
    const before = await status();
    if (before.streaming) throw new Error('A stream is already active.');
    if (before.currentScene !== sceneName) throw new Error('The NetHack scene must be selected.');
    const state = await (await fetch('http://127.0.0.1:8766/state', {signal: AbortSignal.timeout(5000)})).json();
    if (!state.audit?.healthy || !state.visible) throw new Error('Viewer and audit must be healthy and visible before streaming.');
    await request('StartStream');
    await writeFile(path.join(root, '.runtime/broadcast.json'), JSON.stringify({startedAt: new Date().toISOString(), stopAt: null}));
    console.log('Stream started without a scheduled cutoff. Local video recording was not started.');
  }
  if (command === 'broadcast') {
    const minutes = Number(process.argv[3]);
    if (!Number.isFinite(minutes) || minutes <= 0 || minutes > 120) throw new Error('Specify a duration between 0 and 120 minutes.');
    const before = await status();
    if (before.streaming) throw new Error('A stream is already active.');
    if (before.currentScene !== sceneName) throw new Error('The NetHack scene must be selected.');
    await request('StartStream');
    const started = Date.now();
    const stopAt = started + minutes * 60000;
    await writeFile(path.join(root, '.runtime/broadcast.json'), JSON.stringify({
      startedAt: new Date(started).toISOString(), stopAt: new Date(stopAt).toISOString()}));
    console.log(`Stream started; automatic stop at ${new Date(stopAt).toISOString()}`);
    try {
      while (Date.now() < stopAt) {
        await new Promise(resolve => setTimeout(resolve, Math.min(10000, stopAt - Date.now())));
        const current = await request('GetStreamStatus');
        if (!current.outputActive && Date.now() - started > 15000) break;
      }
    } finally {
      if ((await request('GetStreamStatus')).outputActive) await request('StopStream');
      console.log('Broadcast ended.');
    }
  }
  if (command === 'inspect') {
    console.log(JSON.stringify({settings: await request('GetInputSettings', {inputName}),
      active: await request('GetSourceActive', {sourceName: inputName}),
      items: await request('GetSceneItemList', {sceneName})}, null, 2));
  }
  if (command === 'refresh') {
    await request('PressInputPropertiesButton', {inputName, propertyName: 'refreshnocache'});
    console.log('OBS browser refreshed.');
  }
  if (command === 'screenshot') {
    await mkdir(path.join(root, '.runtime'), {recursive: true, mode: 0o700});
    const imageFilePath = path.join(root, '.runtime/obs-preview.png');
    await request('SaveSourceScreenshot', {sourceName: sceneName, imageFormat: 'png',
      imageFilePath, imageWidth: 1920, imageHeight: 1080});
    console.log(imageFilePath);
  }
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
} finally {
  if (socket) socket.close();
}
