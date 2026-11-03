# Presenter Guide: Ten-Minute Version

**Length:** About 10 minutes. **Message:** One sentence about a new sales channel updates the text, the architecture diagram, and the runbook in about a minute, with a full record of what changed.

## Before the audience arrives

1. Open a terminal in this folder.
2. Create a throwaway branch:

```bash
git switch -c demo-run
```

3. Open your AI tool in the [project/](project/README.md) folder. If it does not read [AGENTS.md](project/AGENTS.md) on its own, start with: "Read AGENTS.md and follow it."
4. Have a previewer ready that shows Mermaid and D2 diagrams, so you can show the pictures after each change. Use whichever previewer you already have.
5. Have `before/architecture-diagram.png` ready to show.

## Act 1: The old way (1 minute)

- Show `before/architecture-diagram.png`.
- Ask: "Who can move a box on this today?"
- Open the same diagram as text in `project/docs/020-architecture.md`.

## Act 2: Ask (2 minutes)

- **Executive prompt:**

```text
I am a senior leader with no technical background. In five sentences or fewer, tell me what the Sales Insights Platform does and how far along it is. Name the file and section behind each claim.
```

- **Picture prompt:**

```text
Draw a Mermaid diagram for a non-technical audience that shows how sales from each channel reach the dashboards. Five boxes at most. Do not change any file.
```

## Act 3: The change (4 minutes)

- **Say:** "Marketing just told us about a new sales channel."
- **Prompt:**

```text
Northwind is launching a marketplace channel, Bazaarly, on 6 April 2027. Orders arrive through the Bazaarly seller API. Bazaarly pays Northwind through its own daily payout file. Customers are in the United States and Canada. Add Bazaarly as a fifth sales channel and Bazaarly payouts as a third settlement source. Update every affected file and diagram. Write TBD for anything you cannot know. Summarize what changed.
```

- **Show, in this order:**
  - The AI's summary.
  - Your previewer: the new box and edges in the D2 diagram and the new bar on the roadmap.
  - `git diff --stat`.
- **Commit:**

```bash
git add -A && git commit -m "Add Bazaarly channel and payouts"
```

## Act 4: Close (1 minute)

- Show `git log --stat -1`.
- Say: "One sentence, three files, every diagram redrawn, and a full record. Now imagine every team's documents working this way."

## Answer key

| File | Where                                                                                          |
| :--- | :--------------------------------------------------------------------------------------------- |
| 010  | Channels table, the flow diagram, the roadmap, the Snapshot countries                          |
| 020  | The D2 sources and settlement groups, the nightly load text and sequence, the components table |
| 030  | The failure runbook (a row for the Bazaarly API), daily operations                             |

## Rehearsal notes

An independent AI session with no other context ran every prompt in this guide against these documents. The AI tool behaved as follows, and you should expect similar results.

- **Time:** About 90 seconds of AI work across all three prompts. The change prompt takes under a minute.
- **What it did:**
  - Added Bazaarly and its payouts to the flow diagram, the roadmap, the D2 diagram, the data model text, and the runbook.
  - Added a new risk and wrote `TBD` for shares, volumes, and costs it could not know.
- **A point worth saying aloud:** The AI noted that the channel shares in the table no longer add up to 100%. That is the kind of catch a pasted picture never makes.
- **Picture prompt:** "Five boxes at most" makes the AI group the four channels into one box. That is fine.

## Reset

```bash
git switch main && git branch -D demo-run
```

## If something goes wrong

- **Short on time:** Skip the executive prompt in Act 2.
- **The AI invents a launch figure:** Point at the TBD rule in [AGENTS.md](project/AGENTS.md).
