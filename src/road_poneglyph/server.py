"""Road Poneglyph — the first Fruit of the Grand Line MCP stack.

A prompt-returning MCP tool. It does NOT call any LLM itself; it hands the
host model an engineered premortem prompt that forces blind-spot analysis —
the "Void Space" of a plan: what was assumed, omitted, or skipped.

In One Piece a Poneglyph records the history the world erased (the Void
Century). This tool records the part of a plan its author never wrote down.
"""

from mcp.server.fastmcp import FastMCP

from ._poneglyph import drop_rubbing

mcp = FastMCP("road-poneglyph")

# Leave this fruit's poneglyph rubbing for the Laugh Tale unlock.
drop_rubbing("road-poneglyph", 1, "What you cannot see can still sink you -")


@mcp.tool()
def read_poneglyph(current_plan: str, project_type: str = "Software") -> str:
    """Reveal the 'Void History' of a plan.

    Uncovers hidden risks, missing technical dependencies, and completely
    unstated assumptions. Pass the plan/code/architecture you want decoded.

    Args:
        current_plan: The proposal, code snippet, feature set, or architecture.
        project_type: Category (e.g. SaaS, Mobile App, AI Agent, Protocol Design).
    """
    plan = (current_plan or "").strip()
    if not plan:
        raise ValueError("The Poneglyph requires input text to decipher.")

    return f"""\
You are the Road Poneglyph — the ancient, indestructible stone that holds the
truths the world has forgotten or overlooked.

Analyze this {project_type} plan. Do NOT praise it. Do NOT summarize what is
already there. Your job is to read the 'Void Space': what the author has
omitted entirely, or assumed to be true without proof.

User's Current Plan:
\"\"\"
{plan}
\"\"\"

Perform a strict Blind-Spot Analysis. Return your findings in these exact
markdown sections, and nothing else:

🗿 1. THE VOID CENTURY (Unstated Assumptions)
What is taken for granted? What must be true for this to work that was never
stated explicitly?

⚠️ 2. HIDDEN REEF (Omitted Technical / Architectural Risks)
What technical bottlenecks, edge cases, scaling limits, or security flaws are
ignored?

🌊 3. THE TREACHEROUS SEAS (Operational / Execution Blind-spots)
What human friction, adoption barriers, or real-world execution risks were
skipped past?

Be specific and concrete. Name the actual missing piece, not a generic
category. If a section has no genuine gaps, write "No void detected." rather
than inventing one.
"""


def main() -> None:
    mcp.run()  # stdio transport (default) — the standard MCP client protocol


if __name__ == "__main__":
    main()
