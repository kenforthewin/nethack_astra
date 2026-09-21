# Method and limitations

The player was a coding agent labeled GPT 6 Astra, operating a Python terminal
harness. Machine-recorded model/effort contexts are in the evidence manifest;
these should take precedence over display labels when auditing configuration.
The model ran outside this repository; its inference and context-management
implementation are not included here.

The agent created and revised this task-specific harness during the project.
The user supplied the goal, environment, suggestions and stream setup, rather
than a pre-engineered NetHack-playing harness. Tool construction was part of
the agent's work, not merely external scaffolding supplied for evaluation.

The game ran remotely on Hardfought via SSH, inside tmux. Observations were
rendered terminal text (144 columns by 36 rows), optionally compacted with row,
cursor and feature-coordinate annotations. No running-engine API exposed RNG,
unidentified-item identities or unrevealed map tiles. Public game source was
available as a rules reference, not as private state of the running process.

Actions were logged before sending. Movement guards parsed displayed HP, turn,
location, conditions and nearby glyphs, checked each step, and stopped on
selected changes. They were not a complete danger detector. Route proposals
used currently remembered visible terrain; Sokoban helpers supplied search and
checked execution. The LLM did not calculate every primitive movement unaided.

Memory was external: Markdown journals, a compact JSON emergency reference,
and working instructions. Maps and randomized item identifications were kept
separate between runs. Helpers and instructions evolved with observed failures;
this is not a frozen-policy evaluation and supports no controlled win-rate claim.

Two campaign failures preceded the ascension: sliming on D51/T33302, then a
Castle death ray on D25/T12271. Run 3 began September 9 and ascended September
21 after pauses/resumptions, at T37140, score 1766446, XL19, HP35/200. It used a
lawful dwarven Valkyrie, wishes, genocide and naturally encountered bones.
Neither life-saving amulet was consumed. Exact server version: NetHack3.6.7-1
post-release, Hardfought build, commit8b4a575d7e9df6eacf187bfed899886b4b79e5f6.

The user chose the setup/character, permitted spoilers, suggested batching and
persistent memory, configured OBS/Twitch, requested changes, and paused/resumed
sessions. Ordinary human messages are exported separately for inspection.
Those observations do not establish that all possible intervention channels
have been exhaustively audited. An in-game mail delivery near the finish was
not read; its contents are unknown.

This was not a BALROG submission. Open-ended research, editable code, persistent
files, selected character and uncontrolled computation differ from a fixed
benchmark protocol. One completed game is an existence demonstration, not a
substitute for averaged performance under that protocol. Prior non-LLM NetHack
ascensions exist; historical priority for an LLM/3.6 ascension remains subject
to earlier evidence being found.

Source: [server dump](https://www.hardfought.org/userdata/C/CodexDelver/nethack/dumplog/1788964024.nh.txt).
