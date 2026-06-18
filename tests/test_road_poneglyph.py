"""End-to-end test: spin up the server over stdio as a real MCP client would,
list its tools, call read_poneglyph (happy path), and confirm empty input
fails (failure path)."""

import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> int:
    params = StdioServerParameters(command=sys.executable, args=["-m", "road_poneglyph.server"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            names = [t.name for t in tools.tools]
            assert names == ["read_poneglyph"], names
            print("list_tools OK:", names)

            # Happy path
            res = await session.call_tool(
                "read_poneglyph",
                {"current_plan": "Build a payments API. Stripe webhook updates the DB.",
                 "project_type": "SaaS"},
            )
            text = res.content[0].text
            assert "VOID CENTURY" in text and "HIDDEN REEF" in text, text[:200]
            assert "payments API" in text
            assert not res.isError
            print("call_tool happy-path OK (", len(text), "chars )")

            # Failure path: empty plan must error
            err = await session.call_tool("read_poneglyph", {"current_plan": "   "})
            assert err.isError, "empty input should have errored"
            print("call_tool failure-path OK:", err.content[0].text.strip()[:80])

    print("\nALL TESTS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
