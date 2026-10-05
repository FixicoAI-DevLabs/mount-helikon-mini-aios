# Engineering candidate review packet

This directory records local engineering validation. It is not a release or an activation receipt. The candidate archive is reproducibly generated into `build/`; generated ZIPs are not committed as source.

The original engineering receipt and archive below predate publication of draft PR #9 and the [first live browser pilot](browser-pilot-01/README.md). That separate record contains current hosted-CI and browser observations. The issued archive and its input files have not been revised by adding this evidence.

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build --out build/first
python3 tools/mini.py build --out build/second
cmp build/first/Helikon-Mini-4.0.0-candidate.1.zip build/second/Helikon-Mini-4.0.0-candidate.1.zip
```

Compare the archive checksum with `engineering-validation.json`. Its source digests identify the tested inputs; rebuilding after a source change needs a new receipt and, after issue, a distinguishable candidate revision.

At the original engineering checkpoint, live delivery, installation/migration/recovery, the 48-run behavior pilot, supplementary cases, and 72 utility comparisons were unrun. No GitHub merge, tag, release asset, hosted CI run, public download verification or account-settings change was asserted by that receipt. Consult the subsequent browser record for the limited scope completed since then; merge, tag and release remain unperformed.
