# Trigram-index search (candidates, then regex)

## Definition (working)

A **two-stage** text search over a corpus:

1. **Index:** overlapping 3-byte trigrams → inverted posting lists (often mmap'd, sorted).
2. **Verify:** only files whose trigrams *could* satisfy the query are run through the real regex engine.

Canonical public case in this vault: [[wiki/sources/tgrep]] (optional long-lived server + live overlay). Older cousins exist (Google Code Search / zoekt, Russ Cox's trigram notes) — **not ingested** here.

Status of «tgrep is always faster than ripgrep»: **Refuted** at author-benchmark depth (Kubernetes/Linux 0.93×; high match-volume kernel queries historically lost). Status of «tgrep skips files that cannot match, then verifies candidates»: **Confirmed** at README/AGENTS.md depth, not traced in Rust.

## Mechanism (from tgrep README + AGENTS.md)

```
regex
  → literal fragments → trigram hashes
  → intersect/union posting lists  (candidates)
  → rayon full-regex on those files
```

Serving adds a **HybridIndex**: mmap `IndexReader` + in-memory `LiveIndex` overlay (watcher / still-building files). Overlay wins.

Three freshness clocks, easy to collapse into one lie:

| Path | Answers from | Stale when |
|---|---|---|
| `tgrep serve` | last applied watcher/poll event | event still queued; native notify missed (hourly safety reconcile, deferrable to 4h); **first build still empty** |
| on-disk `.tgrep/` | last successful index publication | any edit since; interrupted first build may leave incomplete index **without warning** |
| `--no-index` / no index | live walk | never (slow) |

A fourth failure mode: **membership mismatch** (`--max-filesize`, `--exclude`, `--no-require-git` differ between builder and server) looks identical to «no match».

## Why it matters for `pro/plan`

- Efficiency: agent grep on a monorepo is often the hidden Cost of a coding turn. Indexing moves Cost to build/watch; queries pay candidates + delivery.
- Causal hygiene: «search returned nothing» is not one cause. Split **cold empty serve**, **incomplete on-disk index**, **flag that bypasses the index**, **64 MiB cap dropped the file**, **pattern is regex not literal**.
- «Slow despite index» can be **match-volume serialization over TCP**, not a bad planner — tgrep's per-delivered-match cost is higher than ripgrep's stdout path (author BENCHMARKS).
- This host already has `rg`; tgrep is optional infrastructure, not a personality/harness change.

## Contrast

| | Trigram-index search (tgrep) | MCP tool broker ([[wiki/concepts/mcp-tool-broker]]) | Tiered KV ([[wiki/concepts/tiered-kv-cache]]) |
|---|---|---|---|
| Speeds up | File selection for regex | (doesn't; adds a hop) | Prefill reuse |
| Persists | Posting lists + paths | Nothing useful; session HTTP | Attention KV blocks |
| Failure | Empty serve / stale index / cap / bypass | Unauth `shell=True` | Cold miss / missing kernels |
| Network | Local JSON-RPC for search | Often bind-all HTTP | Local inference API |

Not a harness axis.

## Related

- Source: [[wiki/sources/tgrep]]
- Entity: [[wiki/entities/microsoft]]
- Tool: [[10_Reference/tools/tgrep]]
- Adjacent: [[wiki/concepts/efficiency-metric]], [[wiki/concepts/causal-analysis]], [[wiki/concepts/git-native-experiment-tree]] (search index ≠ experiment lineage), [[wiki/concepts/self-healing-cdp-harness]] (search index ≠ CDP)

## Sources

- [[wiki/sources/tgrep]]
