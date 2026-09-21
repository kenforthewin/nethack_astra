# nethack_astra

**An LLM ascended NetHack. This is the harness it built along the way.**

Harness and evidence for CodexDelver's NetHack 3.6.7 ascension, played by
GPT 6 Astra through a remote terminal on Hardfought. September 21, 2026:
37,140 game turns, 1,766,446 points, lawful dwarven Valkyrie.

To our knowledge this is the first recorded LLM-agent ascension. This is a
historical-priority claim open to correction, not a benchmark result or a claim
that no earlier non-LLM bot won. BotHack ascended years earlier.

[Final server dump](https://www.hardfought.org/userdata/C/CodexDelver/nethack/dumplog/1788964024.nh.txt)
is the simplest starting point. See [methodology](docs/METHODOLOGY.md),
[publication policy](docs/PUBLICATION.md), and [setup](docs/SETUP.md).

## What's here

- `scripts/session.py`: persistent tmux/SSH session, input and text observations.
- `scripts/guard.py`: conservative checked movement batches.
- `scripts/route.py` and `scripts/sokoban.py`: navigation proposals and puzzle assistance.
- `scripts/terminal.py`, `web/`: ANSI rendering, spectator display and victory card.
- `scripts/audit.py`: private hash-linked ledger, transcript watcher and checkpoints.
- `scripts/prepare_publication.py`, `scripts/verify_publication.py`: sanitized export and independent public verification.
- `memory/`: run-scoped journals, including two failed campaign runs.
- `EVIDENCE.md`: contemporary audit notes; historical instructions are not current authorization.

This is the harness, **not a standalone autonomous player**. The coding-agent
session supplied model inference, tool orchestration and context management.
There is no bundled model or API loop that reproduces the win automatically.
The current UI is the victory card; `web/game.html` preserves the gameplay UI.

## Evidence download

The separately prepared `nethack-evidence.tar.gz` contains the filtered event
ledger, public commentary, human messages, game inputs/observations, historical
code and journal snapshots, server dumps and selected server recording segments.
Download the [reviewed evidence archive (124 MB)](https://github.com/kenforthewin/nethack_astra/releases/download/v1.0.0/nethack-evidence.tar.gz)
and [archive checksum](https://github.com/kenforthewin/nethack_astra/releases/download/v1.0.0/SHA256SUMS)
from the [v1.0.0 release](https://github.com/kenforthewin/nethack_astra/releases/tag/v1.0.0).
The archive has its own internal manifest and file checksums. It is a filtered
public projection, not the complete private transcript.

```sh
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/verify_publication.py /path/to/extracted/evidence
python3 scripts/verify_publication.py .
```

The final verification command checks this published repo file set;
intentional edits require new checksums. Local hashes establish consistency,
not independent provenance or proof that no human intervened.

The agent could consult the web, wiki and public source, write helpers, and
keep persistent memory. It used wishes, genocide and bones. The system evolved
over the campaign. This was not a BALROG-protocol evaluation or a win-rate study.

## Publication status and licensing

Public harness repository: [kenforthewin/nethack_astra](https://github.com/kenforthewin/nethack_astra).
The harness software and associated documentation are [MIT licensed](LICENSE).
The larger evidence archive is distributed separately as a release attachment.
The MIT license does not relicense NetHack, server-generated game content, or
other third-party material in the evidence archive. Third-party source bodies are
not bundled in the evidence export; links and original checksums are retained.
NetHack and server artifacts retain their applicable rights and attribution.

`docs/source-export.json` records the original reviewed export's hashes.
The README and publication notes were subsequently updated for this release;
`SHA256SUMS` covers the files as published here. Historical journals and audit
notes describe events at their recorded times, not current operating instructions.
The ascended game is finished and the victory broadcast has been stopped.
