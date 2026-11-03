#!/usr/bin/env python3
"""Tests that tools/check-docs.py fails when documentation is broken, not only that it passes.

Why it exists: a checker that cannot fail proves nothing. Each case builds a tiny
documentation tree in a temporary folder, plants one defect, and asserts the
checker reports it. Diagram cases skip when no renderer is installed, so the
suite runs anywhere with plain Python.

Run: python3 tools/test-check-docs.py
"""

import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("check_docs", Path(__file__).with_name("check-docs.py"))
check_docs = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_docs)

FENCE = "`" * 3


def run_checker(files):
    """Runs the checker over a temporary tree and returns (exit code, printed output).

    Args:
        files: A mapping of relative path to file text for the tree.
    """
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name, text in files.items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
        original = check_docs.ROOT
        check_docs.ROOT = root
        try:
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = check_docs.main()
        finally:
            check_docs.ROOT = original
        return code, output.getvalue()


class LinkChecks(unittest.TestCase):
    def test_valid_link_passes(self):
        code, _ = run_checker({"a.md": "[b](b.md)", "b.md": "text"})
        self.assertEqual(code, 0)

    def test_missing_target_fails(self):
        code, output = run_checker({"a.md": "[gone](gone.md)"})
        self.assertEqual(code, 1)
        self.assertIn("broken link -> gone.md", output)

    def test_missing_target_with_anchor_fails(self):
        code, _ = run_checker({"a.md": "[gone](gone.md#section)"})
        self.assertEqual(code, 1)

    def test_link_inside_code_fence_is_ignored(self):
        code, _ = run_checker({"a.md": f"{FENCE}text\n[gone](gone.md)\n{FENCE}\n"})
        self.assertEqual(code, 0)

    def test_missing_image_fails(self):
        code, output = run_checker({"a.md": "![alt](images/gone.png)"})
        self.assertEqual(code, 1)
        self.assertIn("broken link -> images/gone.png", output)

    def test_existing_image_passes(self):
        code, _ = run_checker({"a.md": "![alt](images/x.png)", "images/x.png": "png"})
        self.assertEqual(code, 0)

    def test_web_and_anchor_links_are_ignored(self):
        code, _ = run_checker({"a.md": "[x](https://example.com) [y](#top)"})
        self.assertEqual(code, 0)


@unittest.skipUnless(shutil.which("mmdc"), "mmdc not installed")
class MermaidChecks(unittest.TestCase):
    def test_valid_diagram_passes(self):
        code, _ = run_checker({"a.md": f"{FENCE}mermaid\nflowchart LR\n    A --> B\n{FENCE}\n"})
        self.assertEqual(code, 0)

    def test_broken_diagram_fails(self):
        code, output = run_checker({"a.md": f"{FENCE}mermaid\nflowchart LR\n    A -->\n{FENCE}\n"})
        self.assertEqual(code, 1)
        self.assertIn("mermaid block 1 failed to render", output)


@unittest.skipUnless(check_docs.D2_URL or shutil.which("d2"), "no D2 renderer available")
class D2Checks(unittest.TestCase):
    def test_valid_diagram_passes(self):
        code, _ = run_checker({"a.md": f"{FENCE}d2\na -> b\n{FENCE}\n"})
        self.assertEqual(code, 0)

    def test_broken_diagram_fails(self):
        code, output = run_checker({"a.md": f"{FENCE}d2\na -> {{{{{{\n{FENCE}\n"})
        self.assertEqual(code, 1)
        self.assertIn("d2 block 1 failed to render", output)


if __name__ == "__main__":
    unittest.main()
