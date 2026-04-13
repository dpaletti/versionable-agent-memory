---
name: memory
description: Persistent agent memory for this workspace. Read at the start of every task to load context. Write at the end of every answer to record progress, decisions, and discoveries. Search when you need to find past context.
---

# Agent Memory

Persistent memory stored as markdown in `.agents/memory/`.

## Protocol

### 1. READ — At the start of working on a repo

Always read memory before doing anything:

```bash
cat .agents/memory/MEMORY.md
```

For recent context, check the latest daily journals:

```bash
ls .agents/memory/????-??-??.md | tail -5
```

Then read the relevant files.

### 2. WRITE — At the end of every answer

After each response where you did meaningful work, append to today's journal:

**File:** `.agents/memory/YYYY-MM-DD.md` (use today's date)

**Format:**
```
## HH:MM — Short Title

What was done, learned, changed.
- Files modified
- Decisions and rationale
- Problems and solutions
```

If the project state changed significantly (architecture, conventions, major
decisions), also **overwrite** `.agents/memory/MEMORY.md` with the current
snapshot. Include `> Last updated: YYYY-MM-DD HH:MM UTC` at the top.

When overwriting MEMORY.md, evaluate whether it needs simplification — if it
has grown too complex, disconnected, or contains outdated information, clean
it up. This file is the project reference; keep it useful.

### 3. SEARCH — When you need to find something

**Quick keyword search (no dependencies):**

```bash
grep -rn "<query>" .agents/memory/ --include='*.md'
```

**Ranked full-text search (FTS5):**

```bash
cd <skill-dir> && uv run search.py "<query>"
cd <skill-dir> && uv run search.py "<query>" --limit 20
cd <skill-dir> && uv run search.py "<query>" --rebuild
```

The search script uses a SQLite FTS5 index at `.agents/memory/.index.db`
(gitignored). It auto-indexes changed files on each search.

## When to Write What

| Trigger | Where |
|---------|-------|
| Completed a task | Daily journal |
| Solved a problem | Daily journal |
| Made a design decision | Daily journal + MEMORY.md |
| User says "remember this" | Daily journal + MEMORY.md |
| Architecture changed | MEMORY.md |
| New convention established | MEMORY.md |

## First-Time Setup

If `.agents/memory/` doesn't exist yet, create it automatically:

```bash
mkdir -p .agents/memory
cp <skill-dir>/HOW\ TO\ USE\ THIS\ MEMORY.md .agents/memory/
```

Then create an initial `MEMORY.md` describing the project's current state.

Always auto-bootstrap — never ask the user to set up memory manually.

## Full Documentation

Read `.agents/memory/HOW TO USE THIS MEMORY.md` for all conventions.
