# How To Use This Memory

This directory is persistent memory for AI agents working on this project.

## Reading Memory

1. **Read `MEMORY.md` first** — current project state, architecture, decisions
2. For recent context, check the latest daily journals:
   ```bash
   ls .agents/memory/????-??-??.md | tail -5
   ```
3. For historical context, search:
   ```bash
   grep -rn "<query>" .agents/memory/ --include='*.md'
   ```

## Structure

| File | What |
|------|------|
| `MEMORY.md` | Current project state snapshot — mutable, kept up to date |
| `YYYY-MM-DD.md` | Daily journals — append-only, entries tagged with `@username` |
| `HOW TO USE THIS MEMORY.md` | This file — explains the memory layout |

### MEMORY.md

A living snapshot: architecture, decisions, conventions, known issues.
Mutable — sections are edited, added, or removed as the project evolves.

### Daily Journals

One file per day. Each entry is timestamped and attributed:

```
## HH:MM — Short Title (@username)

What was done, learned, decided.
```

Append-only — past entries are never edited.

## Modifying Memory

To write to this memory, install the `memory` skill:

**https://github.com/dpaletti/versionable-agent-memory**

The skill defines the full protocol: when to write, when to delay,
how to evaluate whether an interaction is worth recording, and how
to keep MEMORY.md useful over time.
