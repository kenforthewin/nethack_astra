# Expedition memory

ACTIVE BROADCAST: read memory/live-run.md first. The shakedown below is retired.
User explicitly canceled the 30-minute limit: KEEP PLAYING UNTIL USER SAYS STOP.
The cutoff process has been canceled, and OBS remains live.

User wants an AI-played NetHack 3.x run streamed to Twitch. Spoilers and reference
consultations are unrestricted. Use Hardfought for external game recordings.
Dedicated stream account registered: CodexDelver. Login and reconnect verified.

Read this file at the start of each session, then inspect the actual game screen.
Update it before stopping: character, turn, location, inventory discoveries,
threats, goals, unresolved prompts, save status, and recording links.
Never put passwords or stream keys here. Keep observations separate from guesses.

## Environment

- Local NetHack 3.6.7 and tmux 3.6a are installed; existing local saves belong to
  Kenny. This project uses a remote game instead.
- Hardfought US: `[REDACTED:email]`.
- SSH host key is pinned in config/known_hosts, verified against Hardfought's
  published ED25519 fingerprint: SHA256:6I4FoeQJSX90yDFeWb7XTuq/AeuOFo2F2QEDSwgLWmY.
- Control: `python3 scripts/session.py screen`, `keys`, `start`, `attach`.
- Runtime account credentials: `.runtime/credentials.json`, private and ignored.
- Persistent browser view: `python3 scripts/session.py viewer` on port 8765.
  Live on `0.0.0.0`, explicitly authorized by user, including unauthenticated
  access on their local network. Approval review initially rejected it; after
  user confirmation the restart was approved and succeeded.
  LAN URL: http://[REDACTED:lan_address]:8765/ (Kennys-Mac-mini).
  Verified listening on TCP *:8765 and HTTP 200 through LAN address.
- Broadcast starts hidden. Use `hide` for login; `show` once gameplay is ready.
- OBS installed in /Applications/OBS.app; user logged into Twitch. Service is
  configured. Authenticated WebSocket control enabled by user on port 4455.
  `node scripts/obs.mjs status|setup|screenshot` controls/inspects OBS, reading its
  local password directly without printing it. Requires sandbox escalation.
- OBS scene `NetHack — CodexDelver`, browser source `NetHack browser`, URL
  http://127.0.0.1:8765/, 1920x1080. Canvas and output 1080p, 30 fps; existing
  Apple H.264 encoder and 6000 kbps retained. No special mic/desktop audio inputs.
  Actual OBS preview inspected at .runtime/obs-preview.png; full-width color
  curses terminal, small header and notes below. Persistent header disclosure:
  "AI player · GPT 6 Astra". No old footer/tagline. Browser needs a moment to load.
  Streaming and recording are OFF. Character is restored and paused at turn 38
  for the layout preview; no gameplay turns taken during display changes.
- Display preset config/nethackrc adapted from Kenny's ~/.nethackrc (no matching
  config found under ~/.config). Installed in Hardfought's CodexDelver.nh36rc.
  Curses, persistent inventory, status/item colors, 144x36 terminal. Gameplay
  defaults retained, including number_pad:1 and !autopickup. Previous server
  config backed up at .runtime/hardfought-before-curses.nh36rc. Server file
  verified against local preset (only an extra final blank line).
- Color renderer scripts/terminal.py handles SGR 16/256/RGB colors, styles,
  inverse and DEC Special Graphics. Browser uses text nodes, not terminal HTML.
  Six parser tests passed. Avoid rebuilding unchanged frames; repeated full
  replacement caused intermittent blank OBS screenshots before deduplication.
  Final enlarged color scene and AI disclosure visually verified in OBS.

## Current state

2026-09-06: completed an approximately five-minute gameplay shakedown.
Hardfought US is connected and logged in. The game is RESTORED AND PAUSED at
normal command input, turn 38, so the user can inspect the 144x36 layout.
No pending prompt. To save: `S`, then `y`, then Space at curses' `>>` prompt;
verify return to version menu. To restore from that menu use uppercase `V`.
Curses restore completes directly unless a "--More--" prompt appears.
Save/restore was verified at turn 38, then saved again without taking another
game turn. Curses migration likewise restored and saved at turn 38.

Character: CodexDelver, lawful female dwarven Valkyrie (Stripling).
Dlvl 1, T:38, HP 13/18, Pw 1/1, AC 6, Xp 1/1, gold 5.
St 18/06, Dx 12, Co 13, In 10, Wi 9, Ch 10. No displayed adverse conditions.
Kitten alive. First goblin killed by kitten; grid bug killed by player.

Inventory: a +1 long sword wielded; b +0 dagger alternate; c blessed +3 small
shield worn; d uncursed food ration; e orcish helm (BUC unknown, not worn);
f tin opener (BUC unknown); g cloudy potion (identity/BUC unknown); $ 5 gold.
No unidentified consumables used.

Map coordinates below refer to the ORIGINAL 80x24 tty screen, not curses:
two connected rooms explored. Starting upstairs at x27,y6 in left room
(screen columns/rows zero-based). Bamboo arrows remain there. East corridor
connects to second room; pushed boulder now at x45,y5 inside it. Hero at x45,y9,
just north of south doorway at x45,y10. No visible hostile after grid bug kill.
Several exits remain unexplored; downstairs not yet found.

Controls verified: literal keypad digits, 8 north / 2 south / 4 west / 6 east,
7 NW / 9 NE / 1 SW / 3 SE. Short strings such as `996` execute multiple turns.
IMPORTANT: number_pad is enabled. `k` means kick, not north. Named Up produced
an unintended take-off menu (escape sequence interpreted incorrectly); avoid
arrow keys. Named Escape works to cancel menus. `i` inventory, `,` pickup,
Space dismisses --More--, uppercase `S` then `y` saves. Stop at new prompts;
key batches can encounter monsters or message pagination partway through.
Gameplay tool commands need sandbox escalation to access the live tmux socket;
sandboxed `screen` misleadingly reports no session when access is denied.

Verified: SSH host fingerprint; account registration and fresh login; dead-pane
reconnect; batched menu keys (`1V`); 80x24 screen capture; HTTP hidden-state
response; private-file URL returns 404; credential file permissions 0600.
Gameplay verified: inventory menus, pickup, keypad movement batches, combat,
boulder pushing, --More-- handling, save/restore matching turn/HP/map, final save.
LAN /state response matched live screen during combat at turn 36.

tmux 3.6a crashes if `window-size manual` is configured before the first session
exists. Workaround: `resize-window` after session creation. Do not re-add that
option to config/tmux.conf. Persistent viewer is tmux session `viewer`; game is
`hardfought`; socket `/tmp/nhstream-3e1e09d5b90a.sock`.

Next: ready for a broadcast session. Do not claim Twitch is live or that a completed game recording has
been verified yet. Hardfought's archive is https://www.hardfought.org/nethack/ttyrecs/.
