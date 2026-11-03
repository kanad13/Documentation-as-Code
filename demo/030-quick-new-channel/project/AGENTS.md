# Agent Instructions: Northwind Sales Insights Documentation

Northwind Outfitters and everything about its Sales Insights Platform is fictional. You maintain the platform's documentation in `docs/` the way a project team would.

## Files

| File                                   | Audience                | Content                                                                        |
| :------------------------------------- | :---------------------- | :----------------------------------------------------------------------------- |
| `docs/010-project-overview.md`         | Executives and managers | Scope, status, roadmap, risks, cost, owners                                    |
| `docs/020-architecture.md`             | Engineers               | Components, data flow, data model, security, recovery                          |
| `docs/030-operations-and-decisions.md` | Engineers and support   | Daily operations, runbook, recovery, decision log                              |
| `docs/README.md`                       | Everyone                | Index of the three documents. Keep it in step if you add or rename a document. |

## Rules for every change

- **Find everything before you edit:**
  - Search all three documents for every term the change touches: system names, regions, tools, roles, numbers, and dates.
  - Do not rely on headings alone. A fact can sit in a table, a diagram label, or a runbook row.
- **Keep text and diagrams together:**
  - Update the D2 diagram in `020-architecture.md` and the Mermaid diagrams in all three files when their content changes.
  - Never leave a diagram that disagrees with its surrounding text.
- **Handle decisions as history:**
  - Never delete or rewrite an old decision record.
  - Add a new record, and mark the old one `Superseded by ADR-00X` in its `Status:` line while keeping the rest of its text.
  - Give every record a `Status:` line: `Accepted`, `Proposed`, or `Superseded by ADR-00X`.
  - Check every `Revisit when` line against the change, and say which ones the change triggers.
- **Respect time:**
  - Describe the current state until a change takes effect.
  - Show a planned change with its effective date in the text and in diagram labels, for example `from 1 March 2027`.
  - Never let a document claim that something works before its date.
- **Never invent facts:**
  - Write `TBD` for any cost, date, volume, or vendor fact you cannot know.
  - List every `TBD` in your summary.
- **Keep numbers consistent:**
  - Recompute totals and counts that a change affects.
- **Keep the house style:**
  - Use bullets and tables, and define terms at first use.
  - Keep the D2 `vars` header unchanged.
  - Keep the `classDef` lines and class assignments in Mermaid flowcharts.
  - Write each caption as `**Diagram: <one idea>**` above its diagram.
  - Rewrite the caption of every diagram you change as one statement. Do not join two ideas with "and", "but", or "while".
  - Use at most 10 nodes per Mermaid flowchart and quote every flowchart label.

## How to finish

- **Verify:** Re-read each diagram you changed and confirm every node and edge matches the text.
- **Report:**
  - A summary of what changed, file by file.
  - The `TBD` items.
  - Open questions for a human.
- **Git:** Do not commit or push unless asked.
