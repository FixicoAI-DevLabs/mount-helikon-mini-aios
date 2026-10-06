# Helikon Mini

**Helikon Mini 4 — Project beta** is a compact rebuild from released Helikon 6.0.0. Version `4.0.0-candidate.5` is published and available now. It uses short project instructions and one compact Operating JSON, with versioned installation and behavior evidence.

**[Download Mini 4](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/download/v4.0.0-candidate.5/Helikon-Mini-4.0.0-candidate.5.zip)** · **[Installation guide](START_HERE.md)** · **[Release notes](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/tag/v4.0.0-candidate.5)**

No Python or local build is needed to install the package. The published ZIP was downloaded without authentication and checked against the exact tested bytes. See the [publication record](release/4.0.0-candidate.5/PUBLICATION_STATUS.md).

Short System guidance and one compact Operating JSON retain three planes and twelve responsibilities without requiring six Saved Memories or specialised Skills. The source map covers 92 source components and 474 nested normative IDs; it does not claim full semantic equivalence.

Candidate 4 completed 48 behavior case-runs and a 72-response utility comparison. It passed the behavior criteria but exposed planning errors. Candidate 5 adds preservation of supplied durations and reconciliation of task/day/project totals. See the versioned reports for exact tested scope and retained failures.

- [Candidate 4 complete pilot](release/4.0.0-candidate.4/browser-pilot-04/README.md)
- [Candidate 5 tests](release/4.0.0-candidate.5/browser-pilot-05/README.md)
- [Installation](docs/install.md), [support matrix](docs/support-matrix.md) and [implementation status](docs/implementation-status.md)
- [Architecture](docs/architecture.md), [source map](docs/source-to-mini-map.md), [validation](docs/validation.md) and [recovery](docs/recovery.md)

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build
```

Python 3.10+ and its standard library suffice. The deterministic build writes a candidate ZIP under `build/`; it does not install settings, modify memory or publish. Canonical files are in `src/`, schema in `schema/`, and the generated reading copy in `generated/`.

Testing used Pro, browser ChatGPT, GPT-5.6 Sol / Medium. Free-account and ordinary global-chat delivery remain untested. Complete source content was recovered in a bounded-copy candidate-4 conversation, but hidden full-body delivery on every turn was not observable. No general reliability or utility advantage is established. Do not replace an active full Helikon installation to try Mini.

This release is an experimental ChatGPT project edition. Package documentation retains its tested candidate metadata; the publication record provides current release status.

See [LICENSE](LICENSE), [SECURITY.md](SECURITY.md) and [CHANGELOG.md](CHANGELOG.md).
