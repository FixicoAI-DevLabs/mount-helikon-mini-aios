# Engineering candidate review packet

This directory records local engineering validation. It is not a release or an activation receipt. The candidate archive is reproducibly generated into `build/`; generated ZIPs are not committed as source.

```sh
python3 tools/mini.py validate
python3 -m unittest discover -s tests -v
python3 tools/mini.py build --out build/first
python3 tools/mini.py build --out build/second
cmp build/first/Helikon-Mini-4.0.0-candidate.1.zip build/second/Helikon-Mini-4.0.0-candidate.1.zip
```

Compare the archive checksum with `engineering-validation.json`. Its source digests identify the tested inputs; rebuilding after a source change needs a new receipt and, after issue, a distinguishable candidate revision.

Still unrun: live delivery, installation/migration/recovery, the 48-run behavior pilot, supplementary cases, and 72 utility comparisons. No GitHub merge, tag, release asset, hosted CI run, public download verification or account-settings change is asserted.
