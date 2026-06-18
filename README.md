<!-- mcp-name: io.github.xfloukiex-lab/road-poneglyph -->
# 🗿 Road Poneglyph

> **Fan-inspired homage. Not affiliated with, sponsored by, or endorsed by the
> creators or rights holders of *One Piece* (Eiichiro Oda / Shueisha / Toei
> Animation).** All code and artwork here are original; no official assets, logos,
> or artwork are used. "One Piece" and related marks belong to their owners.

<img src="icon.png" width="120" align="right">

A [Model Context Protocol](https://modelcontextprotocol.io) server. Finds a plan's **blind spots** — the things you forgot or assumed. LLMs are good with what's in front of them and bad at noticing what *isn't there*; this forces a premortem pass and surfaces unstated assumptions, omitted technical risks, and execution blind-spots.

**Tool:** `read_poneglyph`

Prompt-returning: makes **no LLM call and needs no API key** — it returns an engineered prompt the host model executes.

## Install

Requires Python ≥ 3.10.

```bash
pip install road-poneglyph
```

Then add to your MCP client config (e.g. Claude Desktop, or `claude mcp add`):

```json
{ "mcpServers": { "road-poneglyph": { "command": "road-poneglyph" } } }
```

## Develop

```bash
git clone https://github.com/xfloukiex-lab/road-poneglyph
cd road-poneglyph
python -m venv .venv && . .venv/Scripts/activate   # or .venv/bin/activate
pip install -e ".[dev]"
python tests/test_road_poneglyph.py
```

## 🏴‍☠️ Part of the Grand Line stack — collect them all

Each tool drops a *poneglyph rubbing* into `~/.grandline/poneglyphs/`. Install all of them and **Laugh Tale** reveals the One Piece.

- 🗿 [`road-poneglyph`](https://github.com/xfloukiex-lab/road-poneglyph) — Road Poneglyph ← you are here
- ⚔️ [`conquerors-haki`](https://github.com/xfloukiex-lab/conquerors-haki) — Conqueror's Haki
- ⏳ [`toki-toki`](https://github.com/xfloukiex-lab/toki-toki) — Toki Toki no Mi
- 🏴‍☠️ [`laugh-tale`](https://github.com/xfloukiex-lab/laugh-tale) — Laugh Tale — the One Piece

## License

Apache-2.0. Icon: original art (see source `icon.svg`); generated locally, no
official assets.
