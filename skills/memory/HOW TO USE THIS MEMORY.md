# How To Use This Memory

This directory is persistent memory for AI agents working on this project.
Any agent can read and contribute. No special tools required — just markdown.

## Quick Start

1. **Read `MEMORY.md`** — current project state, architecture, decisions
2. Do your work
3. **Evaluate** whether the interaction is worth recording
4. If yes, **append to today's daily file** and/or **update `MEMORY.md`**

## Files

| File | What | How to write |
|------|------|-------------|
| `MEMORY.md` | Current project state snapshot | Mutable — edit, update, or rewrite as needed |
| `YYYY-MM-DD.md` | Daily journal for that date | Append only |

## MEMORY.md

A living snapshot of the project: architecture, decisions, conventions, issues.

- **Read this first** when starting any task
- **Mutable** — edit sections, add new ones, remove outdated ones, rewrite as needed
- Keep concise — this is a snapshot, not a log
- Add `> Last updated: YYYY-MM-DD HH:MM UTC` at the top
- If it grows too complex or disconnected, simplify it

## Daily Journals

One file per day, named `YYYY-MM-DD.md`. Append timestamped entries
with the author who contributed them:

```
## HH:MM — Short Title (@username)

What was done, what was learned, what changed.
- Files modified
- Decisions and rationale
- Problems and solutions
```

- **Append only** — never edit past entries
- **Always include `@username`** — use `$USER` or the agent/tool name
- No need to create directories — all files are flat in this folder

## When to Write

**Not every interaction is worth recording.** After each answer, evaluate:

- Was something meaningful accomplished, learned, or decided?
- Would a future agent or human benefit from knowing this?
- Or was this a trivial question with an obvious answer?

**Batch when appropriate** — if a series of related exchanges are building
toward a conclusion, wait until the meaningful outcome is reached before
writing a single cohesive entry, rather than recording each small step.

### Write to the daily journal when:
- A task or subtask was completed
- A non-trivial problem was solved
- A decision was made (and why)
- Something important about the codebase was discovered
- The user explicitly says "remember this"

### Update MEMORY.md when:
- Architecture or design changes
- New conventions or patterns are established
- A major issue is resolved or discovered
- The project state changes significantly

## Conventions

- Dates: `YYYY-MM-DD` (ISO 8601)
- Times: `HH:MM` (24-hour)
- Daily files: append-only, one per day
- Daily entries: always include `@username`
- MEMORY.md: mutable, keep concise
- Cross-reference: `[2026-04-10](2026-04-10.md)`
