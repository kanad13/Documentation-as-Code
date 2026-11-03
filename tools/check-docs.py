#!/usr/bin/env python3
"""Checks that every relative Markdown link and image resolves and every diagram renders.

Why it exists: this repository argues that documentation should be verified like
code, so the same standard applies to its own pages. Mermaid renders locally with
`mmdc` when installed. D2 renders through the service named in D2_RENDERER_URL,
or through the local `d2` command; with neither, D2 blocks are skipped with a notice.
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D2_URL = os.environ.get("D2_RENDERER_URL", "").rstrip("/")
FENCE = re.compile(r"^```(\w+)[^\n]*\n(.*?)^```", re.S | re.M)
# Matches page links and image links alike, so a missing image file is caught too.
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def markdown_files():
    """Yields every Markdown file under ROOT in a stable order, skipping Git internals."""
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" not in path.parts:
            yield path


def strip_code(text):
    """Returns text without fenced code blocks, so example links inside code are not checked."""
    return FENCE.sub("", text)


def check_links(path, text, errors):
    """Appends a message to errors for each relative link in text that points to a missing file.

    Args:
        path: The Markdown file the text came from; links resolve against its folder.
        text: The file contents.
        errors: A list that receives one message per broken link.
    """
    for target in LINK.findall(strip_code(text)):
        if re.match(r"^(https?:|mailto:|#)", target):
            continue
        target_path = (path.parent / target.split("#")[0]).resolve()
        if not target_path.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken link -> {target}")


def render_d2(source, workdir):
    """Checks a D2 block through a renderer service or the local `d2` command.

    A service (D2_RENDERER_URL) honors the block's own TALA setting. The local
    command lacks TALA unless licensed, so it checks syntax with the ELK layout.
    Returns (None, reason) when neither is available.
    """
    if D2_URL:
        request = urllib.request.Request(f"{D2_URL}/d2/svg", data=source.encode(), method="POST")
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.status == 200, ""
        except urllib.error.HTTPError as error:
            with error:
                return False, error.read().decode(errors="replace")[:300]
        except OSError as error:
            return False, str(error)
    if shutil.which("d2"):
        src, out = Path(workdir, "in.d2"), Path(workdir, "out.svg")
        src.write_text(source)
        result = subprocess.run(["d2", "--layout", "elk", str(src), str(out)],
                                capture_output=True, text=True, timeout=120)
        return result.returncode == 0, (result.stderr or result.stdout)[:300]
    return None, "no D2 renderer: set D2_RENDERER_URL or install the d2 command"


def render_mermaid(source, workdir):
    """Checks a Mermaid block by rendering it with the local `mmdc` command.

    Args:
        source: The diagram text, without the code fence.
        workdir: A scratch folder for the input and output files.

    Returns:
        (True or False, detail), or (None, reason) when `mmdc` is not installed.
    """
    if not shutil.which("mmdc"):
        return None, "mmdc not installed"
    src, out = Path(workdir, "in.mmd"), Path(workdir, "out.svg")
    src.write_text(source)
    config = Path(workdir, "puppeteer.json")
    # Headless Chrome refuses to start as root or inside containers without this flag.
    config.write_text('{"args": ["--no-sandbox"]}')
    result = subprocess.run(
        ["mmdc", "-i", str(src), "-o", str(out), "-p", str(config), "-q"],
        capture_output=True, text=True, timeout=120,
    )
    return result.returncode == 0, (result.stderr or result.stdout)[:300]


def check_diagrams(path, text, errors, skipped):
    """Renders each `mermaid` and `d2` block in text and records failures.

    Args:
        path: The Markdown file the text came from, used to label failures.
        text: The file contents.
        errors: A list that receives one message per diagram that fails to render.
        skipped: A set that receives the reason a diagram type could not be checked.
    """
    with tempfile.TemporaryDirectory() as workdir:
        for index, (language, source) in enumerate(FENCE.findall(text), start=1):
            if language not in ("mermaid", "d2"):
                continue
            ok, detail = render_d2(source, workdir) if language == "d2" else render_mermaid(source, workdir)
            label = f"{path.relative_to(ROOT)}: {language} block {index}"
            if ok is None:
                skipped.add(detail)
            elif not ok:
                errors.append(f"{label} failed to render: {detail.strip()}")


def main():
    """Checks every Markdown file and prints a summary.

    Returns:
        0 when no problems were found, 1 otherwise. Skipped diagram types do not fail the run.
    """
    errors, skipped = [], set()
    files = list(markdown_files())
    for path in files:
        text = path.read_text()
        check_links(path, text, errors)
        check_diagrams(path, text, errors, skipped)
    for note in sorted(skipped):
        print(f"skipped: {note}")
    for error in errors:
        print(f"FAIL {error}")
    print(f"{len(files)} files checked, {len(errors)} problems")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
