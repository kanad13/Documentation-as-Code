# Plan

**Goal:**

- Build a repository that makes the case for documentation as code to non-technical readers.
- Let presenters run a live demo of an AI answering questions and updating docs and diagrams.

**Acceptance:**

- `education/` carries the full argument, diagram-led, and `python3 tools/check-docs.py` passes.
- `demo/` holds three Northwind projects, each with three documents, one D2 diagram, and several Mermaid diagrams, and one lightweight coffee-shop project with two documents and two small Mermaid diagrams.
- A fresh AI session pointed at a demo's `project/` folder answers the sample questions correctly and applies the sample changes across text and diagrams.

**Done:**

- Education pages 010 to 060, restructured and redrawn to the house diagram standards.
- Root README, AGENTS.md, DECISIONS.md, TESTING.md, `tools/check-docs.py`, and tests for the checker.
- Four demo projects with documents, AI instructions, presenter guides, and answer keys. Three carry frozen Word and PNG props.
- `education/005-crash-course.md`: the sixteen-diagram crash course, with a sync map to the long-form pages.
- Public-readiness pass: no private renderer address, neutral voice.
- Independent rehearsal of the four guides with fresh AI sessions (the lightweight one with a small model), and the fixes it exposed.
- Made demo 040 Mermaid-only, added a rendered D2 image to crash-course slide 9, and made the checker verify image links.
- Set the GitHub description and topics, and turned off Projects, Wikis, Discussions, Actions, and merge commits.
- Chose MIT license (`LICENSE`), added repository hygiene (`.gitignore`), and aligned demo walkthrough graphics.

**Next action:**

- Run one presenter guide with the AI tool you will present with, on the final `project/` layout, and fix timing notes that differ.
- Make the repository public (the 2026-11-03 history review found only the author name and email), then enable secret scanning and push protection in Settings.
- Re-run the 040 guide with the AI tool you present with: the Mermaid-only version had one small-model rehearsal only.

**Blockers:**

- None.
