# Presenter Guide: One Big Change, Then an Audit

**Length:** About 20 minutes. **Message:** A new rule from Legal reaches a dozen places in three documents, and the AI finds all of them, redraws the diagrams, and then proves nothing was missed.

## Before the audience arrives

1. Open a terminal in this folder.
2. Create a throwaway branch so every demo starts clean:

```bash
git switch -c demo-run
```

3. Open your AI tool in the [project/](project/README.md) folder. If it does not read [AGENTS.md](project/AGENTS.md) on its own, start with: "Read AGENTS.md and follow it."
4. Have a previewer ready that shows Mermaid and D2 diagrams, so you can show the pictures after each change. Use whichever previewer you already have.
5. Have `before/Northwind-Sales-Insights-Overview-v7-FINAL-2.docx` open in Word or Pages.

## Act 1: The old way (3 minutes)

- **Do:**
  - Show the Word document and scroll to the architecture picture.
  - Ask the room: "Who can move one box on this picture today?"
- **Say:**
  - Nobody has the original file, and the picture is already wrong the day after someone exports it.
- **Then:**
  - Open `project/docs/020-architecture.md` and show the same diagram as text.
  - Show the same diagram in your previewer. Same picture, but this one has a recipe behind it.

## Act 2: Ask (4 minutes)

Paste each prompt into the AI tool. Point at the file and section it cites after every answer.

- **Executive prompt:**

```text
I am the VP of Sales Operations and I do not have a technical background. In five sentences or fewer, tell me what the Sales Insights Platform is, where it stands today, and the top two risks. Name the file and section you used for each claim.
```

- **Executive follow-up:**

```text
Which sales channels are live today, which go live next, and on what dates?
```

- **Technical prompt:**

```text
I am joining the data engineering on-call rotation tonight. Walk me through what happens between 01:00 and 11:00 UTC, what I check when the dashboard looks stale, and who I contact if the ERP connector times out. Cite sections.
```

- **Personal data prompt:**

```text
List every system that touches customer personal data, which fields it holds, and who can read them. Cite sections.
```

- **Picture prompt:**

```text
Draw a Mermaid diagram for a non-technical audience that shows how sales from each channel reach the dashboards. Five boxes at most. Do not change any file.
```

## Act 3: The change (6 minutes)

- **Say:** "Legal just sent us a requirement. I am not going to tell the AI which files to open."
- **Prompt:**

```text
New requirement from Legal, effective 1 March 2027: personal data of customers in the EU (name, email, phone, address) must be stored and processed only in the EU. Update the documentation for the whole project. Update the text and the diagrams together. Add a decision record that supersedes the one this rule overturns, and say which Revisit-when conditions this triggers. Write TBD for any cost or date you cannot know. Finish with a summary of what changed in each file.
```

- **Show, in this order:**
  - The AI's summary.
  - `git diff --stat` for the size of the change.
  - Your previewer again: the new regional boundary in the D2 diagram and the changed sequence diagram.
  - ADR-002 marked superseded, with its original text kept.
- **Follow-up prompt:**

```text
Using only the updated documents, what does the EU rule mean for the project's timeline, cost, and risks? Say what is still TBD.
```

- **Commit it:**

```bash
git add -A && git commit -m "Apply EU data residency rule"
```

## Act 4: The audit (4 minutes)

- **Say:** "Now I want proof nothing was missed."
- **Prompt:**

```text
Audit all three documents against the new EU rule. List every statement, table row, diagram element, or process that still assumes a single US region or lets personal data leave the EU. Cite file and section. Do not fix anything yet.
```

- **Expected result:** A grouped list of gaps with file and section for each. Pick two, fix them live with one sentence, and show the diff.

## Act 5: Close (2 minutes)

- Show `git log --stat` and one diff: who changed what, when, and why.
- Say: "Now imagine every team's project documents work this way, and one assistant reads them all. That is the company AI brain."

## Answer key: where the rule must land

The AI should touch all of these. Use the list to check its work.

| File | Where                                                                            |
| :--- | :------------------------------------------------------------------------------- |
| 010  | Snapshot table: Hosting row                                                      |
| 010  | Dashboards table: Regional Operations row shows name and email                   |
| 010  | Risks table: no regulatory risk exists yet                                       |
| 010  | Annual run cost: warehouse is a single region                                    |
| 010  | Roadmap: a new phase is needed                                                   |
| 020  | D2 diagram: the us-east container, the us-west copy, and the Austin support edge |
| 020  | Components table: locations                                                      |
| 020  | Nightly load text and sequence: every country loads into us-east                 |
| 020  | Security and access: Austin support access and unmasked personal data            |
| 020  | Availability and recovery: the us-west replica                                   |
| 030  | Failure runbook: the customer lookup row                                         |
| 030  | Disaster recovery: restore from us-west                                          |
| 030  | Access requests: Austin support approval                                         |
| 030  | ADR-002 (superseded) and its Revisit-when line; ADR-004 matches on email         |

## Rehearsal notes

An independent AI session with no other context ran every prompt in this guide against these documents. The AI tool behaved as follows, and you should expect similar results.

- **Time:** About 5 minutes of AI work across all eight prompts. The change prompt alone takes 2 to 3 minutes, so talk through the answer key or the diff while it runs.
- **What it did:**
  - Updated all three documents and redrew the D2 diagram with a separate EU region.
  - Marked ADR-002 `Superseded` and kept its text.
  - Wrote a new decision record and listed the Revisit-when lines the rule triggers.
  - Wrote `TBD` for costs, dates, and vendor facts instead of inventing them.
- **Choices it made without being told:**
  - It treated the United Kingdom as outside the EU.
  - It proposed a second warehouse in an EU region.
  - It marked its new decision `Proposed`, pending approval.
- **The audit:** It found 17 real gaps even after a careful update. Examples are a support ticket path that sends EU customer emails to Austin, ADR-004 still reading as a global rule, and no EU on-call contact. This is the strongest beat in the demo, so leave time for it.
- **Layout:** Redrawn diagrams get denser. Say so before you show them.

## Reset

```bash
git switch main && git branch -D demo-run
```

## If something goes wrong

- **The AI misses a place:** Say "Search again for every mention of the US region and Austin." Then make the point that the search is cheap.
- **You run long:** Skip the follow-up prompt in Act 3 and the personal data prompt in Act 2.
