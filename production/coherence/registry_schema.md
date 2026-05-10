# Coherence Registry — Schema

Field documentation for [registry.json](registry.json).

## Top-level

| Field | Type | Notes |
|---|---|---|
| `version` | int | Schema version; bump when fields change incompatibly. |
| `project` | string | `"anima"`. |
| `last_check` | ISO date | Updated when `coherence.py check` runs successfully. |
| `artifacts` | list | The artifact graph. |

## Artifact

| Field | Type | Required | Notes |
|---|---|:-:|---|
| `id` | string | ✅ | Dotted-namespace identifier, e.g. `ep01.synopsis`, `source.character.leena`. Must be unique. |
| `path` | string | ✅ | Repo-relative path to the file. |
| `stage` | enum | ✅ | One of: `source`, `logline`, `one_pager`, `treatment`, `beat_sheet`, `episodes`, `synopsis`, `outline`, `script`, `shotlist`, `animatic`, `lookdev`, `production`, `edit`, `color`, `delivery`, `infrastructure`. |
| `status` | enum | ✅ | One of: `draft`, `in_review`, `approved`, `locked`, `missing`. The dashboard color-codes by this. |
| `episode` | string | ⬜ | Episode ID for episode-scoped artifacts (`ep01`–`ep06`). Used by the dashboard matrix. |
| `authority_for` | list[string] | ⬜ | Conceptual concerns this artifact owns. E.g. `["voice.anima.narrator_palette"]`. Free-form namespace. |
| `depends_on` | list[string] | ⬜ | Artifact IDs this one consumes. Wildcards allowed: `source.character.*`. |
| `last_updated` | ISO date | ⬜ | When the artifact was conceptually last updated. Drives staleness detection. |
| `notes` | string | ⬜ | Free text. Surfaced on the dashboard. |

## Stale detection

An artifact is **stale** when:

1. Its file is missing, **or**
2. A dependency is unknown to the registry, **or**
3. Any dependency's `last_updated` (or file mtime as fallback) is **after** this artifact's `last_updated`.

Run `python production/coherence/coherence.py check` to print the stale list.

## Adding a new artifact

1. Edit `registry.json` directly.
2. Set `last_updated` to today.
3. Set `status` to `draft`.
4. Run `python production/coherence/coherence.py check` to verify the graph parses.

## Marking an artifact freshly updated

```bash
python production/coherence/coherence.py touch ep01.synopsis
```

This sets `last_updated` to today and persists the registry.

## Wildcards

`depends_on: ["source.character.*"]` expands at check time to every artifact whose `id` starts with `source.character.`. Useful when a treatment depends on _all_ character canon files; new characters added later automatically become dependencies.
