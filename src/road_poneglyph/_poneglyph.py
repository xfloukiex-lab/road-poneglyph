"""Shared plumbing for the Grand Line MCP stack.

- One data dir for everything (override with $GRANDLINE_HOME).
- The "poneglyph rubbing" mechanic: each fruit leaves a rubbing carrying one
  fragment of the One Piece. Laugh Tale unlocks only when all rubbings are
  gathered (honor-based — a fun gate, not security).
"""

from __future__ import annotations

import json
import os
from pathlib import Path

# The canonical set of Road Poneglyphs. To reveal the One Piece you must gather
# all of them — i.e. have every fruit installed so each drops its rubbing.
REQUIRED_PONEGLYPHS: tuple[str, ...] = (
    "road-poneglyph",
    "conquerors-haki",
    "toki-toki",
)


def home() -> Path:
    return Path(os.environ.get("GRANDLINE_HOME", str(Path.home() / ".grandline")))


def _poneglyph_dir() -> Path:
    return home() / "poneglyphs"


def drop_rubbing(fruit: str, order: int, fragment: str) -> None:
    """Leave this fruit's poneglyph rubbing. Idempotent; never raises — a
    failure to write a rubbing must never take a fruit's MCP server down."""
    try:
        d = _poneglyph_dir()
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{fruit}.json").write_text(
            json.dumps({"fruit": fruit, "order": order, "fragment": fragment}),
            encoding="utf-8",
        )
    except OSError:
        pass


def collected_rubbings() -> list[dict]:
    """All rubbings found so far, sorted by their intended order."""
    d = _poneglyph_dir()
    out: list[dict] = []
    if not d.exists():
        return out
    for p in d.glob("*.json"):
        try:
            out.append(json.loads(p.read_text(encoding="utf-8")))
        except (OSError, json.JSONDecodeError):
            continue
    return sorted(out, key=lambda r: r.get("order", 99))


def missing_poneglyphs() -> list[str]:
    have = {r.get("fruit") for r in collected_rubbings()}
    return [name for name in REQUIRED_PONEGLYPHS if name not in have]
