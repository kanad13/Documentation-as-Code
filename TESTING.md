# Testing

The repository is documentation, so testing means proving that links resolve, diagrams render, and the demos behave as their guides say. Each check below names the workflow it protects.

## Workflows and checks

| Change you make                              | Check                                                                                              | Command                                                        | Expected result                                                         | When                        |
| :------------------------------------------- | :------------------------------------------------------------------------------------------------- | :------------------------------------------------------------- | :---------------------------------------------------------------------- | :-------------------------- |
| Any Markdown file                            | Every relative link and image resolves and every diagram renders                                   | `python3 tools/check-docs.py`                                  | `0 problems`                                                            | Every change                |
| The checker itself                           | The checker fails on a broken link, a missing image, a broken Mermaid block, and a broken D2 block | `python3 tools/test-check-docs.py`                             | `OK`, with diagram cases skipped when no renderer is installed          | Every change to `tools/`    |
| A demo's documents, rules, or prompts        | An AI given only `project/` answers and edits as the presenter guide says                          | Rehearsal, described below                                     | Every item in the guide's answer key is hit, and every diagram compiles | Every change to a demo      |
| A crash-course diagram or its long-form twin | The pair still tells the same story                                                                | Read both sides of the row in the map in `education/README.md` | No contradiction                                                        | Every change to either side |

## Diagram rendering needs a tool

- **Mermaid:** `check-docs.py` renders with `mmdc` when installed, and skips Mermaid blocks with a notice when it is not.
- **D2:** `check-docs.py` renders through the service named in `D2_RENDERER_URL`, or the local `d2` command with the ELK layout, and skips D2 blocks with a notice when neither exists.
- **What a skip means:** A skipped diagram type was not verified. Install a tool or set the variable before you rely on a green run.

## Rehearsing a demo

Use this when you change anything inside a demo.

1. Copy the demo's `project/` folder to an empty location outside this repository, and run `git init` and one commit there.
2. Give an AI agent that folder and nothing else. Do not give it the presenter guide.
3. Send the guide's prompts one at a time, as separate messages, and ask the agent to record each reply.
4. Check each result against the guide's answer key, and compile every diagram the agent changed.
5. Record what surprised you in the guide's rehearsal notes.

A single run is evidence for that run only. Repeat with a different model when a guide makes a claim about small models.

## Known gaps

- **Diagram structure rules:** The rules in `AGENTS.md` (one idea per diagram, connected, at most ten Mermaid nodes) have no automated check here. Review them by hand.
- **Demo behavior:** The rehearsal is manual, and its results depend on the model.
- **Frozen props:** The Word files and PNGs in each `before/` folder are not checked, by design.
