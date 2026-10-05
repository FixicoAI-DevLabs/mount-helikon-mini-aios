# Helikon Mini

This branch contains **Mini 4.0.0-candidate.3**, a compact rebuild from released Helikon 6.0.0. It is an experimental engineering candidate. An isolated project installation and initial browser smoke checks have run; the full delivery, behavior and utility gates remain open.

See the [first live browser test record](release/4.0.0-candidate.1/browser-pilot-01/README.md), including the initial source-reproduction refusals and recovered browser interruption. These observations do not promote a supported profile or establish an ordinary global-chat installation.

Short user-configured System guidance and one compact Operating JSON retain three planes and twelve responsibilities without requiring six Saved Memories or specialized Skills. Exact-source access is required before claiming runtime availability.

- [Installation prototype](docs/install.md) and [support matrix](docs/support-matrix.md)
- [Architecture](docs/architecture.md) and [source map](docs/source-to-mini-map.md)
- [Migration](docs/migration.md) and [recovery](docs/recovery.md)
- [Validation and release requirements](docs/validation.md)
- [Implementation status](docs/implementation-status.md)

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build
```

Python 3.10+ and its standard library suffice. The build writes a deterministic candidate ZIP under `build/`. It does not install settings, modify memory or publish. Canonical files are in `src/`, schema in `schema/`, and generated reading copy in `generated/`.

Session and project profiles are experimental. Ordinary global chat and free-account delivery are not demonstrated. Do not replace an active full Helikon installation to test the candidate.

**Historical edition:** [Mini 3.3.0 release](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/tag/v3.3.0). Its six versioned root files are unchanged. The old installer describes that historical release, not this candidate.

See [LICENSE](LICENSE), [SECURITY.md](SECURITY.md) and [CHANGELOG.md](CHANGELOG.md).

Candidate 2 targets unsupported response-limit claims and separates source access from output production. Candidate 1 source coverage was subsequently completed through bounded responses; its earlier refusals remain in the evidence. Candidate 2 requires its own live regression and pilot results.
