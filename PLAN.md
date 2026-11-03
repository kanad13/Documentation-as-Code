# Plan

**Goal:**

- Make the case for documentation as code to non-technical readers.
- Let presenters run a live demo of an AI answering questions and updating docs and diagrams.

**Acceptance:**

- `education/` carries the full argument, diagram-led, and `python3 tools/check-docs.py` passes.
- `demo/` holds three Northwind projects (three documents, one D2 diagram, and several Mermaid diagrams each) and one coffee-shop project (two documents, two Mermaid diagrams).
- A fresh AI session pointed at a demo's `project/` folder answers the sample questions correctly and applies the sample changes across text and diagrams.

**Done:**

- Education pages 005 to 060, with the crash course, its sync map, and one rendered D2 image on slide 9.
- Four demo projects with documents, AI instructions, presenter guides, and answer keys, rehearsed with fresh AI sessions.
- Checker (`tools/check-docs.py`) with tests, covering links, images, Mermaid, and D2.
- MIT license, `.gitignore`, and a history and file review that found no confidential data.
- GitHub description and topics set. Projects, Wikis, Discussions, Actions, and merge commits are off.

**Next action:**

1. Run one presenter guide with the AI tool you will present with, on a throwaway branch, and fix any timing notes that differ. Re-run demo 040 first: it had one small-model rehearsal after it became Mermaid-only.
2. Make the repository public:

   ```bash
   gh repo edit kanad13/Documentation-as-Code --visibility public --accept-visibility-change-consequences
   ```

3. In GitHub Settings, enable secret scanning and push protection, and untick Packages in the About panel.

**Blockers:**

- None.
