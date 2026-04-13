# Agent Memory

Cross-agent persistent memory using markdown files.
Works with pi, Claude Code, Cursor, Codex, and any Agent Skills-compatible agent.

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

Add this to your project's `AGENTS.md` (create it if it doesn't exist):

```markdown
## Agent Memory

This project uses persistent agent memory.
Read `.agents/memory/HOW TO USE THIS MEMORY.md` for the full protocol.
Always read memory at the start of a task.
After each answer, evaluate whether the interaction is worth recording.
```

The agent will auto-bootstrap `.agents/memory/`, `HOW TO USE THIS MEMORY.md`, and `.gitignore` on first use — no manual initialization needed.

## How It Works

One skill (`memory`) teaches the agent the protocol:

1. **READ** at the start of every task — `cat .agents/memory/MEMORY.md`
2. **EVALUATE** after each answer — decide if the interaction is worth recording; batch writes when a meaningful set of exchanges completes
3. **SEARCH** when needed — `grep` or FTS5 via `search.py`

### Memory Files

| File | What | How it's written |
|------|------|-----------------|
| `MEMORY.md` | Current project state — architecture, decisions, conventions, issues | Mutable — edit, update, or rewrite sections as needed |
| `YYYY-MM-DD.md` | Daily journal — what was done, learned, decided | Append-only, one file per day, entries tagged with author |
| `HOW TO USE THIS MEMORY.md` | Explains the memory system to any agent | Never modified (auto-created from template) |

### Search

The skill includes `search.py` — a zero-dependency FTS5 search script using Python's stdlib `sqlite3`. It builds an incremental index at `.agents/memory/.index.db` (gitignored) and returns ranked results with snippets. Falls back to simple text matching if FTS5 is unavailable.

For quick searches, `grep` also works:

```bash
grep -rn "query" .agents/memory/ --include='*.md'
```

## Design

- **Flat directory** — daily files are `YYYY-MM-DD.md` in a single folder, no nesting
- **No database required** — all memory is plain markdown, searchable with grep
- **No extension required** — pure skill, works with any agent
- **Auto-bootstrap** — creates `.agents/memory/` on first use
- **Git-friendly** — version memory alongside your code, share across your team
- **Multiplayer** — daily journals are append-only with author tags; MEMORY.md conflicts resolved via standard git merge

## License

MIT
