# Generated data

This directory contains artifacts generated from the official OSINT Framework dataset.

Run:

```bash
python3 scripts/sync_upstream.py
```

Generated artifacts:

- `osint-framework.json` — complete upstream tree.
- `osint-framework-links.md` — flat, human-readable URL index.

These files are intentionally generated rather than hand-maintained so that provenance and synchronization remain reproducible.
