# Decisions

## 2026-11-03 — Name the idea "documentation as code"

- **Context:**
  - The first draft said "code as documentation".
  - That phrase already means code readable enough to need no comments.
- **Chosen:**
  - "Documentation as code", the established name for writing docs with software tooling.
- **Alternatives:**
  - "Docs as code" means the same and is shorter.
  - "Living documentation" is vaguer.
- **Revisit when:**
  - The audience reacts to the term.

## 2026-11-03 — Mermaid for most diagrams, D2 for two

- **Context:**
  - Mermaid renders natively on common code platforms.
  - D2 handles larger architecture better but needs a renderer service or the local `d2` command.
- **Chosen:**
  - Mermaid by default.
  - D2 for the map of where knowledge sits today and for the company AI brain.
- **Revisit when:**
  - Readers cannot see D2 output without the renderer.

## 2026-11-03 — Forceful framing, no defensive section

- **Context:**
  - The author answers audience questions in person.
  - An "objections" section signals doubt.
- **Chosen:**
  - The material presents documentation as code as the standard to adopt.
  - It omits an objections page.
- **Revisit when:**
  - Feedback shows the same question recurring unanswered.

## 2026-11-03 — House standards for prose and diagrams

- **Context:**
  - The first draft used long paragraphs and ad hoc diagram styling.
- **Chosen:**
  - Prose uses bold anchors with single-assertion child bullets.
  - Mermaid follows the Mermaid Architect standard: a caption per diagram, the Cool Slate theme classes, quoted labels, at most 10 nodes.
  - D2 follows the D2 Architect standard: the TALA header, shapes for tiers, theme-default colors.
  - Every heading in `education/` and the root README carries a diagram, except the introduction of the crash course, whose headings are its acts and slides. Meta files (AGENTS, PLAN, DECISIONS, TESTING, tools) do not.
- **Revisit when:**
  - The diagram count makes pages feel heavy to presenters.

## 2026-11-03 — Demo: three self-contained projects, each with its own script

- **Context:**
  - One demo does not fit every slot. Presenters have different amounts of time.
  - The shared story is a retailer whose sales come from several systems, are integrated, transformed, loaded into a warehouse, and shown on dashboards.
- **Chosen:**
  - Three projects under `demo/`, each with its own documents, `AGENTS.md`, presenter guide, and reset step. A fourth, lightweight project was added later (see its own entry).
  - Track 1: one big change (data residency rule), then a consistency audit.
  - Track 2: an escalating series of three changes (a new channel, the residency rule, a vendor swap).
  - Track 3: a short version for tight slots, with one change (add a sales and settlement channel).
- **Alternatives:**
  - One shared base with three guides. Rejected so each project can be run, changed, and reset without touching another.
- **Revisit when:**
  - Keeping three copies of the base documents in step becomes costly.

## 2026-11-03 — Education examples match the demos

- **Context:**
  - The education pages used a streaming change and an SAP extract as examples.
  - Neither appears in the planned demos, so the examples would not land next to them.
- **Chosen:**
  - Examples now use the EU data residency rule and a web store feed, which match the demo scenarios.
- **Revisit when:**
  - The demo scenarios change.

## 2026-11-03 — One fictional story across all three demos

- **Context:**
  - Three different companies would triple the writing and make the audience learn a new story each time.
- **Chosen:**
  - One retailer, Northwind Outfitters, with identical starting documents in each project.
  - Track-specific content lives in each presenter guide and answer key.
- **Revisit when:**
  - Audiences see more than one track and find the repetition dull.

## 2026-11-03 — Frozen Word and PNG props are the one binary exception

- **Context:**
  - The demo contrasts the old way with the new one, so presenters need a real Word file and a real PNG.
- **Chosen:**
  - Each project's `before/` folder holds one `.docx` and one `.png`.
  - They are frozen on purpose. They show what drift looks like.
- **Revisit when:**
  - The props mislead because the documents moved too far from them.

## 2026-11-03 — Demos run on a throwaway branch

- **Context:**
  - The AI edits files and sometimes commits during a demo.
  - A plain `git restore` cannot undo commits.
- **Chosen:**
  - Presenters run `git switch -c demo-run` first and delete the branch afterwards.
  - The step also shows branches, one of the Git ideas in the education pages.
- **Revisit when:**
  - Presenters work outside a clone with a `main` branch.

## 2026-11-03 — The crash course follows a five-act narrative

- **Context:**
  - The working set of diagrams repeated messages and had no order.
- **Chosen:**
  - Sixteen diagrams in five acts: why now, what it costs, the fix, the payoff, the steps and the demo.
  - Each diagram answers the question the previous one raises, and carries one point no other diagram makes.
  - Diagrams that repeated another diagram's point were dropped or merged.
- **Revisit when:**
  - The talk slot shrinks below about eight minutes.

## 2026-11-03 — Name Word, PowerPoint, and SharePoint as today's tools

- **Context:**
  - Many organizations keep design and documentation in those three tools.
  - Generic or niche terms (wiki, intranet, shared drive, Confluence, Visio, Miro) read as less familiar to a general audience.
- **Chosen:**
  - Problem diagrams and education text name Word, PowerPoint, and SharePoint.
- **Revisit when:**
  - The audience adopts a different documentation tool.

## 2026-11-03 — Rehearse demos with an independent AI session

- **Context:**
  - Presenter guides and answer keys were written by the same author as the documents, so they could hide gaps.
- **Chosen:**
  - A fresh AI session with no other context ran each guide's prompts against a copy of the documents, without the guide or the answer key.
  - Findings changed the demo kit: a status line for decision records, a rule to show planned changes with their dates, a caption rule, a load-time inconsistency, and a missing ERP contact.
- **Revisit when:**
  - The documents or prompts change materially, or the presenter switches AI tools.

## 2026-11-03 — The pre-demo diagrams become a crash course inside education

- **Context:**
  - The sequenced diagrams started as a root-level working file.
  - They are the short, presentable version of the argument, and the long pages already live in `education/`.
- **Chosen:**
  - Move them to `education/005-crash-course.md`, with sixteen diagrams that carry a `title:` block inside the code, as a deliberate exception to the usual caption-only rule.
  - Add a map in `education/README.md` that pairs each crash-course diagram with its long-form twin, and a rule in `AGENTS.md` to change both together.
  - Add the three-changes overview and the update sequence that the presenter asked for.
- **Revisit when:**
  - The long pages and the crash course drift despite the map.

## 2026-11-03 — Write for any reader, with no private resources

- **Context:**
  - The repository is intended to be public for any team or company.
  - Early drafts used a private D2 render address and wrote in one organization's voice.
- **Chosen:**
  - Tools read the render service from `D2_RENDERER_URL` or use the local `d2` command, and skip D2 checks with a notice when neither exists.
  - Pages address "teams" and "organizations" in general, and give steps any team can follow.
- **Revisit when:**
  - The repository gains a hosted renderer of its own.

## 2026-11-03 — A fourth, lightweight demo for small models and short slots

- **Context:**
  - Redrawing a large D2 diagram depends on the AI model, and a short slot needs something that shows a change at a glance.
- **Chosen:**
  - A new project, `040-lightweight-coffee-orders`, with two documents, one small Mermaid diagram, and one small D2 diagram.
  - The AI outlines new or changed shapes in green, so the audience sees the change without reading the diagram.
  - Chosen after trying three scenarios (newsletter signup, support triage, coffee orders) with the small Haiku model. All three compiled and kept the diagram setup. Coffee orders was the most relatable and had the clearest change.
- **Alternatives:**
  - Edit an existing project into a lightweight one. Rejected because the existing ones are built to show scale.
- **Revisit when:**
  - A small model fails on the coffee example, or presenters prefer a different story.
- **Update:**
  - The D2 diagram was later replaced by a second Mermaid diagram. See "Demo 040 uses only Mermaid".

## 2026-11-03 — Each demo gives the AI only a project folder

- **Context:**
  - Handing an AI the whole demo folder exposed presenter notes and the answer key, and handing it only the documents left it without rules.
- **Chosen:**
  - Each demo has a `project/` folder holding the fictional team's `AGENTS.md`, a short README, and `docs/`. It is what a real team's documentation repository looks like.
  - Presenter material (the README, the guide, the frozen props) stays outside `project/`.
  - The guide says to open the AI tool in `project/`, and to start with "Read AGENTS.md and follow it." if the tool does not read it automatically.
- **Revisit when:**
  - A popular tool needs a different file name for agent instructions.

## 2026-11-03 — Demos do not prescribe how to preview diagrams

- **Context:**
  - Presenters have different laptops and tools, and the repo should not impose a previewer.
- **Chosen:**
  - Demos tell presenters to have any previewer that shows Mermaid and D2 diagrams.
  - The repository no longer ships a diagram viewer.
  - Only the documentation check in `tools/` remains, and it serves people who maintain the repository.
- **Revisit when:**
  - Presenters ask for a preview option.

## 2026-11-03 — Test the checker, and document how the repository is verified

- **Context:**
  - The documentation checker was the repository's only verification, and nothing proved that it can fail.
- **Chosen:**
  - `tools/test-check-docs.py` plants a broken link, a broken Mermaid block, and a broken D2 block in a temporary tree and asserts that the checker reports each.
  - `TESTING.md` maps each kind of change to its check, and lists what no check covers.
- **Revisit when:**
  - The repository gains automated checks for the diagram structure rules.

## 2026-11-03 — Demo 040 uses only Mermaid

- **Context:**
  - GitHub and most editors render Mermaid but not D2, so a D2 diagram forced presenters of the shortest demo to have a renderer.
  - A second syntax also adds a second way for a small model to fail.
- **Chosen:**
  - Both diagrams in `040-lightweight-coffee-orders` are Mermaid flowcharts, marked with the same green `changed` class.
  - D2 stays in demos 010 to 030, where the architecture is large enough to justify it.
- **Alternatives:**
  - Keep one D2 diagram so every demo shows both tools. Rejected because the other three already do.
- **Revisit when:**
  - Presenters want to show D2 in a short slot.

## 2026-11-03 — One rendered D2 image in the crash course

- **Context:**
  - The crash course says a diagram is a recipe, but a six-line Mermaid example does not show how much a recipe can draw.
  - The repository already commits images as props, so an image is not new, but it must not become the source.
- **Chosen:**
  - Slide 9 shows a PNG rendered from the 89-line D2 block in the 010 architecture page, and links to that page for the text.
  - The image lives in `education/images/`, and `tools/check-docs.py` now fails when an image link points to a missing file.
  - The "Diagrams live only as text" decision is withdrawn. The rule that remains is that every diagram has a text recipe, and an image is an optional rendered copy.
- **Alternatives:**
  - Embed the D2 block with no image. Rejected because GitHub does not render D2, so readers would see code.
  - Draw a new D2 diagram for the slide. Rejected because the 010 diagram is real and already verified.
- **Revisit when:**
  - The 010 architecture changes. Re-render the image from its block.
