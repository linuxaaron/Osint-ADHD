# Upstream data source

## Canonical source

OSINT ADHD uses the official OSINT Framework repository as the canonical upstream resource dataset:

**https://github.com/lockfale/OSINT-Framework**

The structured source is:

**https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json**

The live framework is available at:

**https://osintframework.com/**

## Why an upstream source?

The OSINT Framework changes over time. Keeping the source explicit makes the provenance of imported URLs auditable and allows this repository to refresh its data without manually pretending that every third-party entry was independently authored here.

## Synchronization

Run:

```bash
python3 scripts/sync_upstream.py
```

The script downloads the current upstream JSON, validates its structure, writes a normalized copy to `data/osint-framework.json`, and generates a flat Markdown URL index under `data/osint-framework-links.md`.

The same process can be run by the GitHub Actions workflow in `.github/workflows/sync-osint-framework.yml`.

## Important distinction

- `data/osint-framework.json` = upstream-derived structured data.
- `data/osint-framework-links.md` = generated navigation index.
- `recommendations/aaron-recommended.md` = personal curation by Aaron.
- `categories/` = human-readable topical navigation and guidance.

Generated files should not be edited manually. Change the source or generator instead.
