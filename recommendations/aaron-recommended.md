# Aaron's recommended OSINT resources

This page is intentionally separate from the upstream OSINT Framework dataset. It represents a personal recommendation layer and can evolve independently.

> **Status:** initial baseline. Each resource should be periodically re-evaluated before being treated as operationally current.

## Identity & usernames

| Resource | URL | Primary use | Notes |
|---|---|---|---|
| WhatsMyName | https://whatsmyname.app/ | Username enumeration | Fast web-based cross-platform discovery |
| Sherlock | https://github.com/sherlock-project/sherlock | Username enumeration | Local CLI; direct requests to target platforms |
| Namechk | https://namechk.com/ | Username/domain availability | Useful first-pass correlation |
| Keybase | https://keybase.io/ | Identity/key correlation | Public cryptographic identity data |
| Sylva Identity Discovery | https://sylva.pfeister.dev/ | Identity discovery | Useful for branching from known identifiers |

## Email & identity correlation

| Resource | URL | Primary use | Notes |
|---|---|---|---|
| Hunter | https://hunter.io/ | Business email discovery | Domain/name-based discovery; service limits apply |
| OSINT Industries | https://www.osint.industries/ | Account correlation | Treat results as leads requiring verification |
| theHarvester | https://github.com/laramies/theHarvester | Passive collection | Domains, emails, subdomains and URLs from public sources |
| GHunt | https://github.com/mxrch/GHunt | Google-account OSINT | Requires careful OPSEC and current compatibility checks |

## Web, domains & infrastructure

| Resource | URL | Primary use | Notes |
|---|---|---|---|
| OSINT Framework | https://osintframework.com/ | Resource discovery | Canonical upstream reference for this repository |
| SecurityTrails | https://securitytrails.com/ | DNS/domain intelligence | Historical DNS and infrastructure context |
| crt.sh | https://crt.sh/ | Certificate transparency | Useful for discovering certificate-associated hostnames |
| Shodan | https://www.shodan.io/ | Internet-exposed services | Use only for lawful reconnaissance and interpretation |
| Censys | https://search.censys.io/ | Internet infrastructure | Certificate/host/service discovery |

## GitHub & code intelligence

| Resource | URL | Primary use | Notes |
|---|---|---|---|
| GitHub | https://github.com/ | Public code/repository research | Search public repositories and history |
| GitFive | https://github.com/mxrch/GitFive | GitHub profile investigation | Correlation of public GitHub artifacts |

## Methodology

A recommendation is not a finding. For investigations, corroborate important observations with independent sources and preserve timestamps, URLs and relevant context.

Prefer this workflow:

1. **Define the question.**
2. **Start with the least intrusive public source.**
3. **Collect identifiers, not conclusions.**
4. **Pivot only when an identifier is supported.**
5. **Correlate across independent sources.**
6. **Record timestamps and provenance.**
7. **Mark uncertainty explicitly.**
8. **Stop when the research question is answered.**
