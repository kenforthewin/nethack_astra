# Astra NetHack ascension — harness and reviewed evidence

GPT 6 Astra played CodexDelver on Hardfought and ascended in NetHack 3.6.7
on September 21, 2026, at game turn37,140. This release includes the agent-built
harness and the reviewed record of all three campaign attempts, including the
two failures. The harness is MIT licensed; it is not a standalone model runner.

## Downloads

- `nethack-evidence.tar.gz`: 123,543,663 bytes (about124MB), containing the
  filtered event ledger, game inputs and observations, public commentary,
  ordinary human messages, historical code/journal snapshots, server dumps,
  and selected server ttyrec segments.
- `SHA256SUMS`: checksum for that exact archive (not the repository file manifest).
- `PUBLICATION.md`: scope and privacy policy.

Archive SHA256:
`73e7b58070fe0b8906494f4b02ec65513d82ec486eb00f648cd9ee0f3e85b1c9`

```sh
shasum -a 256 -c SHA256SUMS
tar -xzf nethack-evidence.tar.gz
# From a checkout of this repository, with Python3.11+:
python3 scripts/verify_publication.py /path/to/extracted/evidence
```

Verification checks673 files and611,068 sequence-numbered events, including
explicit omission markers. The export ends at the post-ascension checkpoint;
it does not include the subsequent blog/deployment conversation.

## What this does not claim

This is a reviewed derivative, **not the complete private transcript**.
Credentials, private contact details, private reasoning, injected instructions,
arbitrary tool bodies and raw local terminal chunks are omitted or redacted.
The originals remain preserved privately. Three selected server segments are
partial snapshots; complete save/resume coverage has not been reconciled.
Hash checks establish consistency, not absence of human intervention or an
independent timestamp for the original events. Twitch video is not included.

The agent could consult the web, wiki and source, write helpers and maintain
memory. Wishes, genocide and bones were permitted. The system evolved during
play; this is not a BALROG result, a fixed-budget evaluation or a win-rate study.

The frozen archive is unchanged from its reviewed candidate. Its manifest's
"local release candidate" status describes the preparation stage; this release
documents publication afterward. MIT applies to the harness software and
associated documentation, not a relicensing of NetHack or third-party content.

[Final server dump](https://www.hardfought.org/userdata/C/CodexDelver/nethack/dumplog/1788964024.nh.txt)
· [Methodology](https://github.com/kenforthewin/nethack_astra/blob/main/docs/METHODOLOGY.md)
· [Privacy and omissions](https://github.com/kenforthewin/nethack_astra/blob/main/docs/PUBLICATION.md)
