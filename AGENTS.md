# Agent Instructions

The repository teaches non-technical readers why and how to keep documentation as text in Git. It also holds demo projects that AI agents edit live. Read this file before you change anything.

## Purpose of each area

| Area                      | Rule for agents                                                                                                                                                        |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `education/`              | The argument. Edit with care: each page answers the question the previous one raised. Keep terms explained at first use.                                               |
| `demo/`                   | Four self-contained demo projects about fictional businesses. Each has its own `AGENTS.md`, which governs edits inside it. Presenters run demos on a throwaway branch. |
| `tools/`                  | Verification script and its tests. Run them as `TESTING.md` says.                                                                                                      |
| `TESTING.md`              | Which check protects which workflow. Keep it current when workflows or tools change.                                                                                   |
| `PLAN.md`, `DECISIONS.md` | Project memory. Keep them current.                                                                                                                                     |

## Documentation conventions

- **Diagrams:**
  - Write documentation diagrams as text: use fenced `mermaid` blocks for flows, sequences, timelines, and states, and fenced `d2` blocks for complex architecture.
  - Visual assets, screenshots, and demonstration props may be committed alongside documentation.
- **Diagram setup:**
  - Start every `d2` block with the standard `vars` header that selects the TALA layout. Copy it from an existing block.
  - Start every Mermaid flowchart with the theme `classDef` lines, and give every node a class. Copy them from an existing diagram.
  - Titles come from the caption above each diagram. `education/005-crash-course.md` also carries a `title:` block inside each diagram on purpose.
- **Diagram quality in `education/`:**
  - Give each diagram one idea, stated in a `**Diagram: ...**` caption above it.
  - Connect every group of nodes with a hub, a labeled edge, or a named outer box.
  - Give every heading in `education/` at least one diagram. The exception is the crash course, where each act and slide heading carries its diagram and the introduction is plain text.
- **Long and short versions:**
  - `education/005-crash-course.md` is the short, presentable version of the argument in pages 010 to 050.
  - When you change an idea on one side, change the other. The map in `education/README.md` pairs each crash-course diagram with its long-form section.
- **File naming:**
  - Content files in curated folders use a three-digit prefix and kebab-case names, in steps of ten (`010-name.md`).
  - Every content folder has a `README.md` that lists its files.
- **Links:**
  - Use relative Markdown links only.
  - Make every file named in an index a link.
- **Prose:**
  - Write for non-technical readers.
  - Define each technical term at first use.
  - Put each assertion in its own bullet under a bold anchor.

## Working agreements

- **Start:**
  - Read `PLAN.md`, the latest entries in `DECISIONS.md`, and `git log -10`.
  - Fix stale items first.
- **Before an increment:**
  - Record its goal and acceptance check in `PLAN.md`.
- **After a documentation change:**
  - Run `python3 tools/check-docs.py`.
  - Fix every failure.
  - After a change to `tools/`, also run `python3 tools/test-check-docs.py`.
  - After a change to a demo, rehearse it as `TESTING.md` describes.
- **When a fact appears in several files:**
  - Search for every mention.
  - Update all of them in the same change.
- **When a choice has trade-offs:**
  - Add an entry to `DECISIONS.md`.
- **End of session:**
  - Leave "Next action" in `PLAN.md` runnable by a reader with no chat history.

## Rendering diagrams

Mermaid renders with `mmdc` (Mermaid CLI) when installed. D2 renders through a service named in the `D2_RENDERER_URL` environment variable, or through the local `d2` command.

```bash
printf 'client -> server: Hello\n' | curl -X POST --data-binary @- "$D2_RENDERER_URL/d2/svg" -o diagram.svg
```

Write rendered output to a temporary location, not into the repository.

## Demo behavior

- **Inside a demo project:**
  - Read the `AGENTS.md` inside its `project/` folder and follow it.
  - Treat its files as a real project's documentation.
- **Keeping projects in step:**
  - The three Northwind projects (010, 020, 030) share the same starting documents.
  - Apply any base document change to all three `project/docs/` folders.
  - The lightweight project (040) has its own small documents.
- **What the demos prescribe:**
  - Each demo says what to change and which prompts to use.
  - No demo says how to preview diagrams or which tools to install.
- **The `before/` folders:**
  - They hold deliberately frozen Word and PNG props.
  - Never edit them or cite them as a source.
