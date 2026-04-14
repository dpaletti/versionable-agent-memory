# Agent Memory

Persistent memory skill using markdown files meant for version control.

This memory is comprised of a global mutable `MEMORY.md` file which stores the current state of the system together with daily snapshots which are append only files. This way we **avoid memory conflicts when multiple people are working on the same project** except for the global memory file where conflicts are actually expected and should be resolved like code conflicts are.

Memory is stored locally in the target repository under `.agents/memory`.

## Install

### Pi

```bash
pi install git:github.com/dpaletti/versionable-agent-memory
```

### Claude Code

```bash
/skill install versionable-agent-memory
```

### Manual (any agent)

Copy `skills/memory/` into `.agents/skills/` in your workspace:

```bash
cp -r skills/memory/ <your-workspace>/.agents/skills/memory/
```

## Setup

Add this to your project's `AGENTS.md` or `CLAUDE.md` (create it if it doesn't exist):

```
## Agent Memory

This project uses persistent agent memory.
Read `.agents/memory/HOW TO USE THIS MEMORY.md` for the full protocol.
Always read memory at the start of a task.
After each answer, evaluate whether the interaction is worth recording.
```

The agent will auto-bootstrap `.agents/memory/`, `HOW TO USE THIS MEMORY.md`, and `.gitignore` on first use — no manual initialization needed.

## How This Works

This skill teaches the agent the following protocol:

1. **READ** at the start of every task
2. **EVALUATE** after each answer: decide if the interaction is worth recording; batch writes when a meaningful set of exchanges completes
3. **SEARCH** when needed: `grep` or FTS5 via `search.py`

### Memory Files

| File        | What | How it's written |
|-------------|------|------------------|
| `MEMORY.md` | Current project state — architecture, decisions, conventions, issues | Mutable — edit, update, or rewrite sections as needed |
| `YYYY-MM-DD.md` | Daily journal — what was done, learned, decided | Append-only, one file per day, entries tagged with author |
| `HOW TO USE THIS MEMORY.md` | Explains the memory system to any agent | Never modified (auto-created from template) |

### Search

The skill includes `search.py` — a zero-dependency FTS5 search script using Python's stdlib `sqlite3`. It builds an incremental index at `.agents/memory/.index.db` (gitignored) and returns ranked results with snippets. Falls back to simple text matching if FTS5 is unavailable.

For quick searches, `grep` also works:

```bash
grep -rn "query" .agents/memory/ --include='*.md'
```
