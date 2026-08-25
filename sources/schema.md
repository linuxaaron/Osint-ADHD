# Resource metadata schema

The upstream OSINT Framework dataset currently uses a tree structure with folders and URL records. URL records can contain fields such as:

| Field | Meaning |
|---|---|
| `name` | Human-readable resource name |
| `type` | Resource type, normally `url` for external resources |
| `url` | Canonical or operational URL |
| `description` | Resource description |
| `status` | Upstream availability classification |
| `pricing` | Free/freemium/paid classification where supplied |
| `bestFor` | Intended investigative use case |
| `input` | Typical input |
| `output` | Typical output |
| `opsec` | Operational characteristic supplied by upstream |
| `opsecNote` | Additional operational note |
| `localInstall` | Whether a local installation is available |
| `googleDork` | Whether the resource is a Google-dork entry |
| `registration` | Whether registration is required according to upstream data |
| `api` | Whether an API is indicated |
| `invitationOnly` | Whether access is invitation-only |
| `deprecated` | Whether the entry is deprecated |

## Interpretation rules

These fields describe the upstream dataset; they are **not independent guarantees** by OSINT ADHD.

In particular:

- `passive` does not guarantee anonymity.
- `active` does not necessarily mean malicious activity; it generally indicates that the resource may make requests to external services.
- `free` does not mean unlimited.
- `api: true` does not guarantee a currently accessible or free API.
- `status: live` is time-sensitive.

When OSINT ADHD adds its own metadata, it must be clearly identified as project-owned rather than silently merged into upstream claims.
