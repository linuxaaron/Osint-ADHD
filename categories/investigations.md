# Investigation methodology

OSINT quality depends more on methodology than on the number of tools used.

## Evidence model

**Question → identifier → source → observation → corroboration → conclusion**

Keep observations separate from conclusions. Record:

- source URL
- retrieval timestamp
- query/input
- relevant output
- confidence
- independent corroboration

## Confidence

A practical internal scale:

- **High:** directly supported by a primary source or multiple independent sources.
- **Medium:** supported by credible secondary evidence but not independently confirmed.
- **Low:** plausible lead requiring verification.
- **Unknown:** insufficient evidence.

## OPSEC

Understand whether a resource makes requests directly to target infrastructure, through its own infrastructure, or through a search/indexing provider. Never equate a tool's `passive` label with guaranteed anonymity.

## Stop condition

Stop collecting when the research question is answered. More data is not automatically better data.
