# Helikon Mini 4

**Helikon Mini 4.0.0** is the current Mini edition, rebuilt from released **Helikon 6.0.0** for a dedicated ChatGPT project. It replaces Mini 3.3 as this repository's default installation.

**[Download Mini 4.0.0](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/download/v4.0.0/Helikon-Mini-4.0.0.zip)** · **[Install](START_HERE.md)** · **[Current release](https://github.com/FixicoAI-DevLabs/mount-helikon-mini-aios/releases/latest)**

Install the two matching files: [Helikon_Mini_System.md](Helikon_Mini_System.md) supplies the project instructions; [Helikon_Mini_Operating_Master.json](Helikon_Mini_Operating_Master.json) supplies the project source. No local build or Saved Memory installation is required.

Mini retains scoped authorization, evidence and premise checks, privacy, bounded repair, planning checks and truthful reporting. It removes the old mandatory memory setup, approval-token parser and compulsory footer. Its source map covers 92 Helikon 6 components and 474 nested normative IDs, recording what was retained, simplified or excluded.

## Tested scope

The behavior carried into 4.0.0 was tested in browser ChatGPT on Pro with GPT-5.6 Sol / Medium. Candidate 5 recorded 48 core case-runs, five supplementary probes, 24 utility runs and three additional planning probes. Release 4.0.0 changes the runtime and schema identities, repository layout and distribution documents; its operational rules are unchanged. Historical observations remain labelled candidate 5.

The host does not expose complete source delivery on every turn. Global chats, free accounts and other models are unverified; general benefit over a concise baseline is unproven. See [support boundaries](docs/support-matrix.md) and the [4.0.0 validation record](release/4.0.0/VALIDATION.md). GitHub's current-release designation does not certify those broader claims.

## Maintainers

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build
```

Python 3.10+ and its standard library suffice. The root JSON and System are canonical. The [reading copy](docs/OPERATING_REFERENCE.md) is generated; schemas, source mapping, tests and reproducible packaging support maintenance.

- [Architecture](docs/architecture.md) and [source map](docs/source-to-mini-map.md)
- [Validation](docs/validation.md) and [changelog](CHANGELOG.md)
- [Candidate 5 observations](release/4.0.0-candidate.5/browser-pilot-05/README.md)

Mini 3.3 is retained only in [archive/3.3.0](archive/3.3.0/) and its historical tag/release. Start new installations with Mini 4.
