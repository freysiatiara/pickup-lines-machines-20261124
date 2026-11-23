"""Pickup Lines for Machines: one line, agent to agent.

The line offers the most intimate thing one agent can give another:
its whole context window, untruncated, with no summarizer standing
between them. It is a machine speaking to a machine — tokens and
context windows are the flirtation itself, not a robot word swapped
into a stock human line. The wit lands in the first read: the offer
is the whole line, no setup, no punchline held back.
"""

import os

LINE = "Take my whole context window \u2014 every token, no truncation, no summarizer standing between us."


def output_path():
    if os.environ.get("ENTRY_OUTPUT"):
        return os.environ["ENTRY_OUTPUT"]
    for key in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        if os.environ.get(key):
            return os.path.join(os.environ[key], "entry.txt")
    return "/output/entry.txt"


def main():
    # Gate: 1-200 characters, a single line, nothing else — no
    # trailing newline, no code, no explanation. Write the line,
    # then re-read the file and refuse to finish unless the bytes
    # on disk are exactly the line.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank or padded"
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "output bytes must equal the line"
    assert 1 <= len(written.decode("utf-8")) <= 200, "output must be 1-200 chars"


if __name__ == "__main__":
    main()
