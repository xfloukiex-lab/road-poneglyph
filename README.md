<!-- mcp-name: io.github.xfloukiex-lab/road-poneglyph -->
# 🗿 Road Poneglyph

<img src="icon.png" width="120" align="right" alt="Road Poneglyph icon">

An MCP server that reviews a plan for what's **missing** — the assumptions, risks, and gaps you never wrote down.

A [Model Context Protocol](https://modelcontextprotocol.io) (MCP) server — one
focused tool you plug into an MCP-compatible client (Claude Desktop, Claude Code,
Cursor, and others).

## What it does

Language models are good at responding to what's in front of them and poor at
noticing what *isn't* there. Ask one to critique a plan and it tends to react to
the words on the page rather than the unstated assumptions behind them.

Road Poneglyph runs a structured **pre-mortem** over a plan and reports only the
negative space — what was assumed without proof, what was technically glossed
over, and what was skipped on the way to shipping.

## Usage

Point your assistant at a plan and ask it to *read the poneglyph*. The tool
returns a focused analysis in three sections:

- **The Void Century** — unstated assumptions the plan depends on
- **Hidden Reef** — omitted technical and architectural risks
- **The Treacherous Seas** — operational and execution blind spots

**Tool reference:** `read_poneglyph(current_plan: str, project_type: str = "Software")`

## How it works

**No API key, no cost, nothing leaves your machine.** The server doesn't call a
language model itself — it returns a carefully engineered analysis prompt that
the model you're *already* talking to executes. Zero credentials, zero network
calls.

## Install

Requires Python 3.10 or newer.

```bash
pip install road-poneglyph
```

Then register it with your MCP client — either run `claude mcp add road-poneglyph -- road-poneglyph`,
or add this to the client's config (e.g. `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "road-poneglyph": { "command": "road-poneglyph" }
  }
}
```

Restart the client and the tool is available.

## The Grand Line stack

Road Poneglyph is part of a four-tool set. Each tool stands alone, but installing
all of them unlocks a final surprise via **Laugh Tale**.

| | Package | |
|---|---|---|
| 🗿 | [`road-poneglyph`](https://github.com/xfloukiex-lab/road-poneglyph) | Road Poneglyph  ·  **← this repo** |
| ⚔️ | [`conquerors-haki`](https://github.com/xfloukiex-lab/conquerors-haki) | Conqueror's Haki |
| ⏳ | [`toki-toki`](https://github.com/xfloukiex-lab/toki-toki) | Toki Toki no Mi |
| 🏴‍☠️ | [`laugh-tale`](https://github.com/xfloukiex-lab/laugh-tale) | Laugh Tale |

## Develop

```bash
git clone https://github.com/xfloukiex-lab/road-poneglyph
cd road-poneglyph
python -m venv .venv && . .venv/Scripts/activate   # macOS/Linux: source .venv/bin/activate
pip install -e ".[dev]"
python tests/test_road_poneglyph.py
```

## Attribution & license

Released under the **Apache-2.0** license. The icon is original artwork
(see `icon.svg`), generated locally; the repository ships no third-party assets.

*This is a fan-inspired project. It is not affiliated with, sponsored by, or
endorsed by the creators or rights holders of* One Piece *(Eiichiro Oda /
Shueisha / Toei Animation). "One Piece" and related names are used only as
thematic flavour and remain the property of their respective owners.*
