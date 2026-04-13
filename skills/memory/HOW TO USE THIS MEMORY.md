# How To Use This Memory

This directory is persistent memory for AI agents working on this project.
Any agent can read and contribute. No special tools required — just markdown.

## Quick Start

1. **Read `MEMORY.md`** — current project state, architecture, decisions
2. Do your work
3. **Append to today's daily file** — what you did, learned, decided
4. If something significant changed, **overwrite `MEMORY.md`**

## Files

| File | What | How to write |
|------|------|-------------|
| `MEMORY.md` | Current project state snapshot | Overwrite entirely |
| `YYYY-MM-DD.md` | Daily journal for that date | Append only |

## MEMORY.md

A living snapshot of the project: architecture, decisions, conventions, issues.

- **Read this first** when starting any task
- **Overwrite entirely** when the project state changes — don't append
- Keep concise — this is a snapshot, not a log
- Add `> Last updated: YYYY-MM-DD HH:MM UTC` at the top
- If it grows too complex or disconnected, simplify it

## Daily Journals

One file per day, named `YYYY-MM-DD.md`. Append timestamped entries:

```
## HH:MM — Short Title

What was done, what was learned, what changed.
- Files modified
- Decisions and rationale
- Problems and solutions
```

- **Append only** — never edit past entries
- No need to create directories — all files are flat in this folder

## When to Write

**Daily journal** (append) — after completing a task, solving a problem,
making a decision, discovering something, or when the user says "remember this".

**MEMORY.md** (overwrite) — when architecture changes, new conventions are
established, major issues resolved, or project state shifts significantly.

## Conventions

- Dates: `YYYY-MM-DD` (ISO 8601)
- Times: `HH:MM` (24-hour)
- Daily files: append-only, one per day
- MEMORY.md: overwrite, keep concise
- Cross-reference: `[2026-04-10](2026-04-10.md)`
