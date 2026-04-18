#!/usr/bin/env python3
"""Full-text search across agent memory files using SQLite FTS5."""

# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///

import sqlite3
import os
import sys
import argparse
from pathlib import Path

SKIP_FILES = {"HOW TO USE THIS MEMORY.md"}


def get_db(memory_dir: str) -> sqlite3.Connection:
    db_path = os.path.join(memory_dir, ".index.db")
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS index_meta
           (file_path TEXT PRIMARY KEY, mtime_ns INTEGER)"""
    )
    try:
        conn.execute(
            """CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts
               USING fts5(file_path, content, tokenize='porter unicode61')"""
        )
    except sqlite3.OperationalError:
        # FTS5 not available — fall back to a regular table
        conn.execute(
            """CREATE TABLE IF NOT EXISTS memory_fts
               (file_path TEXT, content TEXT)"""
        )
    return conn


def reindex(conn: sqlite3.Connection, memory_dir: str, force: bool = False) -> None:
    if force:
        conn.execute("DELETE FROM memory_fts")
        conn.execute("DELETE FROM index_meta")

    current_files: set[str] = set()
    for f in os.listdir(memory_dir):
        if not f.endswith(".md") or f in SKIP_FILES:
            continue
        full = os.path.join(memory_dir, f)
        if not os.path.isfile(full):
            continue
        current_files.add(f)
        mtime = os.stat(full).st_mtime_ns

        if not force:
            row = conn.execute(
                "SELECT mtime_ns FROM index_meta WHERE file_path=?", (f,)
            ).fetchone()
            if row and row[0] == mtime:
                continue

        content = Path(full).read_text(errors="replace")
        conn.execute("DELETE FROM memory_fts WHERE file_path=?", (f,))
        conn.execute("DELETE FROM index_meta WHERE file_path=?", (f,))
        conn.execute("INSERT INTO memory_fts VALUES (?,?)", (f, content))
        conn.execute("INSERT INTO index_meta VALUES (?,?)", (f, mtime))

    # Clean deleted files
    for (old,) in conn.execute("SELECT file_path FROM index_meta").fetchall():
        if old not in current_files:
            conn.execute("DELETE FROM memory_fts WHERE file_path=?", (old,))
            conn.execute("DELETE FROM index_meta WHERE file_path=?", (old,))

    conn.commit()


def has_fts5(conn: sqlite3.Connection) -> bool:
    """Check if the memory_fts table is an FTS5 virtual table."""
    row = conn.execute(
        "SELECT sql FROM sqlite_master WHERE name='memory_fts'"
    ).fetchone()
    return row is not None and "fts5" in (row[0] or "").lower()


def search(
    conn: sqlite3.Connection, query: str, limit: int = 10
) -> list[tuple[str, str, float]]:
    if has_fts5(conn):
        try:
            return conn.execute(
                """SELECT file_path,
                          snippet(memory_fts, 1, '>>>', '<<<', '...', 64),
                          rank
                   FROM memory_fts
                   WHERE memory_fts MATCH ?
                   ORDER BY rank
                   LIMIT ?""",
                (query, limit),
            ).fetchall()
        except sqlite3.OperationalError:
            pass  # Invalid FTS5 query syntax — fall through to LIKE

    # Fallback: simple LIKE search (works with or without FTS5)
    return conn.execute(
        """SELECT file_path, substr(content, 1, 200), 0
           FROM memory_fts
           WHERE content LIKE ?
           LIMIT ?""",
        (f"%{query}%", limit),
    ).fetchall()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search agent memory files using full-text search"
    )
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=10, help="Max results (default 10)")
    parser.add_argument(
        "--rebuild", action="store_true", help="Force full re-index before searching"
    )
    parser.add_argument(
        "--memory-dir",
        default=None,
        help="Path to .agents/memory/ directory (auto-detected if not set)",
    )
    args = parser.parse_args()

    # Resolve memory dir
    if args.memory_dir:
        memory_dir = os.path.abspath(args.memory_dir)
    else:
        # Default: ../../memory relative to this script  (skills/memory/search.py)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        memory_dir = os.path.normpath(os.path.join(script_dir, "..", "..", "memory"))

    if not os.path.isdir(memory_dir):
        print(f"Memory directory not found: {memory_dir}", file=sys.stderr)
        sys.exit(1)

    conn = get_db(memory_dir)
    reindex(conn, memory_dir, force=args.rebuild)
    results = search(conn, args.query, args.limit)

    if not results:
        print(f"No results for: {args.query}")
    else:
        for i, (path, snippet, rank) in enumerate(results, 1):
            print(f"[{i}] {path}")
            print(f"    {snippet}")
            print()

    conn.close()


if __name__ == "__main__":
    main()
