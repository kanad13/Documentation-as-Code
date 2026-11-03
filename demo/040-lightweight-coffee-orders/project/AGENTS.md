# Agent Instructions

You maintain the small documentation set in `docs/` for a fictional coffee shop, Bramble Coffee.

## Files

| File                       | Content                                                                                         |
| :------------------------- | :---------------------------------------------------------------------------------------------- |
| `docs/010-overview.md`     | What the ordering process is, key facts, the customer's journey as a Mermaid diagram, and risks |
| `docs/020-how-it-works.md` | Components, the Mermaid diagram of how they connect, and the rules                              |
| `docs/README.md`           | Index of the two documents. Keep it in step if you add or rename a document.                    |

## Rules

- **Update everything affected:**
  - Search both files for every term the change touches before you edit.
  - Update the text and the diagrams together. A diagram must never disagree with the text.
- **Make changes easy to see:**
  - Mark every new or changed Mermaid node with the class `changed`. Add this line to the diagram if it is missing: `classDef changed fill:#05966940,stroke:#10B981,stroke-width:4px;`
  - Do this in both diagrams, so the reader sees every change without reading the text.
- **Keep the diagram setup:**
  - Keep the `classDef` lines and the `class` lines in Mermaid flowcharts.
  - Quote every Mermaid node label and edge label.
- **Never invent facts:** Write `TBD` for anything you cannot know.
- **Finish with a short summary** of what changed in each file.
- Do not commit or push unless asked.

## Syntax reminders

Add a node and an edge, then give the node a class:

```text
    a["Existing step"] --> n["New step"]
    class n changed
```
