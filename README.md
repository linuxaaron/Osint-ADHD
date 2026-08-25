# OSINT ADHD 🧠🔎

> A professional, curated OSINT resource index for web-based investigations.

**OSINT ADHD** is a structured collection of publicly accessible OSINT resources, investigation utilities, search engines, reference material, and research workflows. The project uses the official **OSINT Framework** as an upstream reference and adds a separate layer for personal recommendations and operational notes.

[![OSINT Framework](https://img.shields.io/badge/upstream-OSINT%20Framework-111827)](https://osintframework.com/)
[![License](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Data](https://img.shields.io/badge/data-upstream%20synced-orange.svg)](sources/UPSTREAM.md)

---

## Project goals

- Keep OSINT resources **structured, searchable and reproducible**.
- Preserve the official OSINT Framework dataset as an upstream source rather than silently presenting it as original work.
- Maintain a separate, human-curated list of **Aaron's recommended resources**.
- Record useful metadata such as category, pricing model, API availability, registration requirements and operational characteristics where reliable.
- Prefer lawful, public-information research and clearly distinguish passive lookups from direct requests.
- Make the repository useful both to humans and to automation.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── THIRD-PARTY-NOTICES.md
├── sources/
│   ├── UPSTREAM.md
│   ├── schema.md
│   └── upstream-metadata.json
├── recommendations/
│   └── aaron-recommended.md
├── categories/
│   ├── username.md
│   ├── email.md
│   ├── domains-infrastructure.md
│   ├── social-media.md
│   ├── people.md
│   ├── images.md
│   ├── geolocation.md
│   ├── documents.md
│   ├── companies.md
│   ├── code-github.md
│   ├── search-engines.md
│   └── investigations.md
├── scripts/
│   └── sync_upstream.py
└── .github/workflows/
    └── sync-osint-framework.yml
```

## Upstream OSINT Framework

The canonical upstream project is maintained by `lockfale`:

- Website: https://osintframework.com/
- Repository: https://github.com/lockfale/OSINT-Framework
- Structured dataset: https://github.com/lockfale/OSINT-Framework/blob/master/public/arf.json

The upstream dataset contains structured resource records, including URLs and metadata. This repository deliberately keeps the upstream source identifiable and provides tooling to synchronize it instead of pretending that upstream records are original content.

## Personal recommendations

See [`recommendations/aaron-recommended.md`](recommendations/aaron-recommended.md) for the resources personally recommended by Aaron. These recommendations are intentionally separate from the upstream dataset.

## Responsible use

This repository is an index, not an authorization mechanism. A resource being listed here does **not** mean that its use is legal, permitted by a target, or appropriate for a particular investigation.

Use OSINT resources only for lawful research, your own assets, or systems and data for which you have permission. Respect privacy law, terms of service, robots/rate-limit policies, access controls and applicable professional rules.

**Do not use this repository to bypass authentication, defeat access controls, obtain non-public information, evade rate limits, or conduct unauthorized activity.**

Operational notes in this repository are informational and can become stale. Always verify current behavior with the provider before relying on a tool in an investigation.

## Data quality

Resource availability changes frequently. Links can disappear, domains can change ownership, APIs can become paid, and tools can be abandoned. The repository therefore treats resource status as **time-sensitive metadata**, not a permanent guarantee.

When a claim cannot be verified reliably, it should be marked as unknown rather than guessed.

## Contributing

Contributions should:

1. Add a canonical URL where possible.
2. Explain what the resource actually does.
3. Avoid unsupported claims about accuracy, anonymity or legality.
4. Note registration/API/pricing requirements when known.
5. Keep personal recommendations separate from upstream resources.
6. Never commit credentials, private data, API keys or investigation targets.

## License

The original repository code and original documentation in this project are released under the MIT License. Upstream OSINT Framework material is subject to its own attribution and licensing terms; see [`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md).
