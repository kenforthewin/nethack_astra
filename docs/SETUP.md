# Running or inspecting the harness

Requirements used by this project: Python 3.11+ (standard library), tmux,
OpenSSH; Node22+ for optional OBS control. OBS control reads the macOS OBS
configuration path. The game itself runs on Hardfought, not locally.

Start with the tests; they do not connect to a game or start broadcasting:

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
```

This is a run-specific harness, not a turnkey player. Before using it yourself:

1. Create your own server account. Do not reuse CodexDelver. The current
   credential helper defaults to that username: change it before creating local
   credentials. Never commit `.runtime/` or your raw session transcript.
2. Verify Hardfought's current SSH host key through a trusted channel. The
   bundled `config/known_hosts` is the campaign's public host-key pin, not a
   guarantee of the server's future identity. SSH uses strict checking.
3. Use `config/nethackrc` remotely for the expected curses layout. The parsers
   depend on that layout; arbitrary font/terminal/config changes may break them.
4. Start the SSH pane with `python3 scripts/session.py start`. This opens a
   connection, not an automatic game. Inspect the prompt.
5. Initialize your own private recorder with
   `python3 scripts/audit.py init --source /absolute/path/to/your/session.jsonl`.
   It expects the session metadata's workspace to match this directory. This
   format was specific to the coding-agent session used here; adapt and test if
   your host uses a different format. Do not point it at unrelated sessions.
6. Run `python3 scripts/audit.py start`, then `status` and `verify`. The recorder
   must match your active thread and be healthy before inputs are accepted.
7. Use `session.py hide` for account management; use `credential` only at the
   matching prompt. `session.py show` enables intentional screen publication.
8. Read `session.py screen`; send reviewed actions through `session.py keys
   --why 'Brief public explanation' ...`. Inspect results. `--raw` is for
   reviewed menu responses only, never for bypassing gameplay guards.

`session.py serve --host 127.0.0.1` starts a loopback-only viewer. The historical
`viewer` shortcut binds `0.0.0.0:8766` without authentication: do not expose it
to the internet. The default page now shows the victory card; intentionally
select/adapt `web/game.html` if setting up a new game display. The server only
serves its configured routes, not arbitrary filenames.

OBS is optional. Configure it yourself and inspect `scripts/obs.mjs` before
using `setup`; the script can alter scenes and video settings. `status` is
read-only. Never start/stop a broadcast without the owner's authorization.

Historical run journals are evidence, not instructions to resume CodexDelver.
Start fresh memory for your own character. Do not import randomized item IDs
or maps from this campaign into another run.
