# Demo

The folder holds four demo projects. Three tell the same fictional story: Northwind Outfitters sells through several systems, and a platform combines those sales for dashboards. The fourth is a tiny coffee-shop example built to be easy for a small AI model. Each project has its own documents, AI instructions, presenter guide, and reset step.

## Start here

Pick the project that matches your time slot.

| You have   | Open                                                                     |
| :--------- | :----------------------------------------------------------------------- |
| 6 minutes  | [040 Lightweight Coffee Orders](040-lightweight-coffee-orders/README.md) |
| 10 minutes | [030 Quick New Channel](030-quick-new-channel/README.md)                 |
| 20 minutes | [010 Residency and Audit](010-residency-and-audit/README.md)             |
| 25 minutes | [020 Escalating Changes](020-escalating-changes/README.md)               |

## Contents

- [010-residency-and-audit/](010-residency-and-audit/README.md): One data residency rule reaches a dozen places, then the AI audits its own work.
- [020-escalating-changes/](020-escalating-changes/README.md): A new channel, a residency rule, and a vendor swap, in growing size.
- [030-quick-new-channel/](030-quick-new-channel/README.md): One new sales channel and its payments, in ten minutes.
- [040-lightweight-coffee-orders/](040-lightweight-coffee-orders/README.md): Two short documents and two small Mermaid diagrams; executives ask questions, then mobile pre-orders appear outlined in green, in six minutes.

## How the projects relate

- **Every demo has the same shape:**
  - `project/` is the folder you give the AI. It holds the fictional team's `AGENTS.md`, a short README, and `docs/`.
  - The README, the presenter guide, and the frozen props stay outside `project/`, so the AI never sees the answer key.
- **Same story, separate copies:**
  - The three Northwind projects start from the same three documents.
  - The presenter guide and the answer key differ.
  - Copies are separate so one project can be run, changed, and reset without touching another.
- **Keep the copies in step:**
  - When you change a document in one project, apply the same change to the other two.
  - Run `diff -r` on the `project/docs/` folders to check.

## Rehearsal results

An independent AI session with no other context ran each project's prompts against a copy of its documents. The session never saw the presenter guide or the answer key.

| Project                                                                  | AI time                     | Result                                                                                                                                                                                         |
| :----------------------------------------------------------------------- | :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [030 Quick New Channel](030-quick-new-channel/README.md)                 | About 90 seconds            | All places in the answer key updated, with `TBD` for unknowns                                                                                                                                  |
| [010 Residency and Audit](010-residency-and-audit/README.md)             | About 5 minutes             | Rule applied across all files, ADR-002 superseded, and the audit found 17 further gaps                                                                                                         |
| [020 Escalating Changes](020-escalating-changes/README.md)               | About 5 minutes             | Three changes applied in order, with a final audit that found real leftovers                                                                                                                   |
| [040 Lightweight Coffee Orders](040-lightweight-coffee-orders/README.md) | About 1 minute, small model | Both Mermaid diagrams compiled and the green highlights marked every change, and the highlights came off cleanly. Five executive questions were answered correctly, including one the documents cannot answer |

- **What the rehearsal changed:**
  - A `Status:` line on every decision record.
  - A rule to show planned changes with their dates.
  - A caption rule for redrawn diagrams.
  - Fixes to a load-time inconsistency and a missing ERP contact.
- **What it did not cover:**
  - The sessions were Claude subagents (the lightweight demo used the small Haiku model), so timing and behavior may differ in the tool you present with.
  - The fixes above and the final `project/` layout were applied after the rehearsal and have not been run again.
  - The D2 diagrams in projects 010 to 030 were compiled afterwards, not by the session itself.

**Navigation:** [Repository home](../README.md)
