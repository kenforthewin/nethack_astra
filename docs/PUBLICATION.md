# Evidence scope and privacy review

This is a conservative public projection, not the private archive renamed.
The original campaign archive remains unchanged locally. The export ends at
checkpoint `eb4bcd97db11450ab288bd56fbacca84`, after ascension and the victory UI.
It includes the two failed campaign runs as well as the winning run. Earlier
shakedown activity appears in the imported conversation; it is not counted as
one of those three campaign runs.

## Included

One record per original ledger sequence number, containing selected structured
game events or an explicit omission marker. Includes command intents and queued
acknowledgments, screen observations, public explanations, guard and Sokoban
events, ordinary human messages and model-context metadata. Source timestamps
are distinguished from ledger-recording timestamps (important for retroactive
imports). A queued input is not independently a proof that the game accepted it.

Historical implementation checkpoints and journals are exported as reviewed
text derivatives. `artifact-index.json` maps original hashes to exported hashes
and explains omissions. Original hash prefixes in filenames identify their
source artifacts, not necessarily the bytes of redacted derivatives.

For server recordings, the export selects the final compressed copy where
available, otherwise the latest retained partial copy for that segment. Older
partial snapshots remain indexed but are not duplicated in the download.
TTYREC framing is validated and joined payloads are scanned across frame
boundaries, both raw and with ANSI escapes removed. A flagged binary recording
is withheld, not silently rewritten. Frame times are indexed. This does not yet
prove complete coverage of every save, reconnect and resumed turn.

## Withheld or transformed

- Credentials and known encoded variants; email addresses, local home paths,
  private IPv4 addresses and common token/private-key patterns are redacted.
- Arbitrary tool-call bodies and tool results are withheld. They can contain
  configuration files, unrelated local data, nested encodings, or text outside
  the intended public commentary. IDs/types remain; game inputs are separate.
- Raw local terminal byte chunks are withheld; screen observations and reviewed
  public server recordings provide the terminal evidence in this release.
- Private reasoning, system/developer instructions and injected environment
  messages are not published. The original recorder already omitted private
  reasoning from its observable projection.
- Unselected future event types are withheld by default.
- Third-party source bodies, HTML dumps and directory listings are indexed by
  origin URL and checksum rather than redistributed here.
- `.runtime`, unreviewed raw session archives and the working blog draft are
  not copied into the public repository.

`redactions.json` reports sequence numbers and replacement categories without
publishing removed values or individual secret hashes. Omission reasons are
also attached to records. Normal game characters, player names and relevant
public URLs remain. Replacements can make historical snippets non-executable;
the current harness source is tested separately.

Public SSH login endpoints and explicitly enumerated synthetic test fixtures
are preserved in source code. These reviewed exceptions do not apply to the
conversation or game-event export. Blindly replacing an SSH login target or a
test's fake email address would damage the reusable harness.

## Checks performed and limits

The private ledger/source/artifact verifier passed before export. The exporter
also independently checks the entire selected ledger chain against its frozen
checkpoint and validates each selected historical artifact's original hash.
The public projection has a new hash chain and file checksums. The public
verifier needs no private files or credentials.

Review combines a strict field allowlist, known-secret and pattern scanning,
inspection of human messages, inspection of harness credential-handling paths,
and artifact-format checks. It is not a claim that a person read every byte of
the multi-gigabyte private archive. Automated scanning is not infallible.

Original source-record hashes are not copied into every public row: omitted
short private strings should not be exposed as individual dictionary-testable
hashes. Whole-prefix checkpoint hashes remain. Consequently readers can verify
public-export integrity, but cannot reconstruct or fully validate the withheld
original transcript from this export alone.

There is no independent timestamp anchor, no proof against owner rewriting,
and no proof against unlogged out-of-band input. Early transcript import is
retroactive; raw terminal capture was not retroactive. Tool truncation in the
original session is not repaired by this export. Twitch video coverage has not
been audited or bundled. No claim of zero human involvement is made.

## Public code release

The owner authorized creating `kenforthewin/nethack_astra` as a public harness
repository. This code release contains the reviewed source, configuration,
documentation and run journals, not the separate event-ledger/recording archive.
The reviewed archive is distributed separately with release v1.0.0. No
credentials, private runtime directory or raw session transcript are included.
The harness software and associated documentation are MIT licensed; third-party
game and server material retains its applicable rights.
The original reviewed export is preserved separately; release README and policy
updates are covered by this repository's refreshed `SHA256SUMS`.

## Evidence release and remaining limits

The release attaches the original reviewed candidate2 archive, unchanged:
`nethack-evidence.tar.gz`, 123,543,663 bytes, SHA256
`73e7b58070fe0b8906494f4b02ec65513d82ec486eb00f648cd9ee0f3e85b1c9`.
Its frozen manifest describes its preparation-time status as a local candidate;
the release notes document subsequent publication and licensing. Historical
bytes have not been rewritten to change that status. Release attachments include
the outer checksum and scope notes; the archive contains its internal checksums.

- Privacy review retains ordinary human interventions and public identities,
  redacts private contact details and credentials, and excludes private reasoning.
  Preserve third-party notices; the MIT grant is not a blanket data license.
- Finish recording coverage reconciliation if making an unbroken-recording claim.
- Correlate action logs and server playback before stronger autonomy claims.
- Keep a separately backed-up original archive. Do not replace it with this export.
- Publish the archive checksum alongside release assets; optionally use an
  independent timestamp/signature service (not done by this build).
