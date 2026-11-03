# Presenter Guide: Three Changes of Growing Size

**Length:** About 25 minutes. **Message:** The effort stays at one sentence while the change grows from one new box, to a rule that reaches many files, to a vendor replaced everywhere.

## Before the audience arrives

1. Open a terminal in this folder.
2. Create a throwaway branch:

```bash
git switch -c demo-run
```

3. Open your AI tool in the [project/](project/README.md) folder. If it does not read [AGENTS.md](project/AGENTS.md) on its own, start with: "Read AGENTS.md and follow it."
4. Have a previewer ready that shows Mermaid and D2 diagrams, so you can show the pictures after each change. Use whichever previewer you already have.
5. Have `before/Northwind-Sales-Insights-Overview-v7-FINAL-2.docx` open in Word or Pages.

## Act 1: The old way (3 minutes)

- **Do:**
  - Show the Word document and its architecture picture.
  - Ask: "Who can move one box on this picture today?"
- **Then:**
  - Open `project/docs/020-architecture.md` and show the same diagram as text and as a rendered picture.

## Act 2: Ask (3 minutes)

- **Executive prompt:**

```text
I am a board member with no technical background. In five sentences or fewer, what is the Sales Insights Platform, how far along is it, and what could go wrong? Name the file and section behind each claim.
```

- **Technical prompt:**

```text
List every external system the platform depends on, what it sends, and what breaks if it is unavailable. Cite sections.
```

## Act 3: Change 1, a new box (4 minutes)

- **Say:** "Small change first."
- **Prompt:**

```text
Northwind has acquired Trailside Co., an online retailer in the United States and Ireland. Trailside takes orders in its own system, TrailBooks, and is paid through its own card provider, GoPay, with daily settlement files. Add Trailside as a fifth sales channel and GoPay as a third settlement source, targeting go-live in February 2027. Update every affected file and diagram. Write TBD for anything you cannot know. Summarize what changed.
```

- **Show:** The new box and edges in the D2 diagram, the new row in the channels table, and the new runbook row.
- **Commit:**

```bash
git add -A && git commit -m "Add Trailside channel and GoPay settlement"
```

## Act 4: Change 2, a rule that spreads (6 minutes)

- **Say:** "Now a rule. And remember Trailside has Irish customers."
- **Prompt:**

```text
New requirement from Legal, effective 1 March 2027: personal data of customers in the EU (name, email, phone, address) must be stored and processed only in the EU. This includes Trailside's customers in Ireland. Update the documentation for the whole project. Update text and diagrams together. Add a decision record that supersedes the one this rule overturns, and say which Revisit-when conditions it triggers. Write TBD for any cost or date you cannot know. Summarize what changed.
```

- **Show:** `git diff --stat`, the regional boundary in the D2 diagram, and ADR-002 superseded with its text kept.
- **Point out:** The AI had to combine this change with the one made two minutes earlier.
- **Commit:**

```bash
git add -A && git commit -m "Apply EU data residency rule"
```

## Act 5: Change 3, a vendor replaced everywhere (5 minutes)

- **Say:** "Last one. The name of a vendor appears all over the documents."
- **Prompt:**

```text
The FlowBridge contract will not be renewed on 1 March 2027. Move the platform to Conduit, a different integration platform, before then. Plan two migration waves: wave 1 is the web store and store checkouts, wave 2 is the ERP, the CRM, and Trailside. Update every file and diagram that mentions the integration platform. Add a decision record that supersedes ADR-001. Add a cutover section to the runbook. Write TBD for any cost you cannot know. Summarize what changed.
```

- **Show:** The renamed boxes in the D2 diagram, the cutover section, the risk table, and the new roadmap bars.
- **Commit:**

```bash
git add -A && git commit -m "Replace FlowBridge with Conduit"
```

## Act 6: Close (4 minutes)

- **History prompt:**

```text
Using the git history on this branch, summarize what changed during this session and which risk is now the biggest.
```

- **Audit prompt:**

```text
Audit all three documents. List anything that still mentions FlowBridge as current, still assumes a single US region, or omits Trailside. Cite file and section. Do not fix anything yet.
```

- Show `git log --stat` for the three commits.
- Say: "Three changes, three sentences, and a full history. Now picture every team working this way and one assistant reading all of it."

## Answer keys

### Change 1: Trailside and GoPay

| File | Where                                                                             |
| :--- | :-------------------------------------------------------------------------------- |
| 010  | Channels table, the flow diagram, the roadmap, the Snapshot countries and users   |
| 020  | The D2 sources and settlement groups, the nightly load text, the components table |
| 030  | The failure runbook (a row for TrailBooks), daily operations                      |

### Change 2: EU residency

| File | Where                                                                                                       |
| :--- | :---------------------------------------------------------------------------------------------------------- |
| 010  | Snapshot Hosting row, Regional Operations row, risks, cost, roadmap                                         |
| 020  | D2 us-east container, us-west copy, Austin edge, components locations, nightly load, security, availability |
| 030  | Customer lookup runbook row, disaster recovery, access requests, ADR-002, ADR-004                           |

### Change 3: FlowBridge to Conduit

| File | Where                                                            |
| :--- | :--------------------------------------------------------------- |
| 010  | Snapshot integration platform row, risk R2, annual cost          |
| 020  | D2 container label, components table, sequence participant label |
| 030  | Failure runbook rows, triage diagram, ADR-001                    |

## Rehearsal notes

An independent AI session with no other context ran every prompt in this guide against these documents. The AI tool behaved as follows, and you should expect similar results.

- **Time:** About 5 minutes of AI work across all seven prompts. Each change takes 1 to 3 minutes, so talk through the diff while it runs.
- **What it did:**
  - Change 1 added Trailside and GoPay to every document and to the D2 diagram.
  - Change 2 added an EU region and combined it with Trailside's Irish customers.
  - Change 3 replaced FlowBridge with Conduit, recorded the replacement, and wrote a cutover section.
- **What the audit found:** Real gaps, such as FlowBridge text left in an older decision record, stale channel shares, and settlement data with no EU route. This is the strongest closing beat.
- **Choices it made without being told:**
  - It treated the United Kingdom as outside the EU.
  - It left the PayLink and bank connectors out of both migration waves and said so.
- **Layout:** After three changes the D2 diagram is dense. Say so before you show it. The point is that it still compiles and still matches the text.

## Reset

```bash
git switch main && git branch -D demo-run
```

## If something goes wrong

- **A change feels too slow:** Skip the Act 2 technical prompt.
- **You are short of time:** Drop Change 1. Go from the Ask act to Change 2, then Change 3. The audit still works.
- **The AI invents a number:** Ask "Which of these figures came from the documents?" and show that AGENTS.md says to write TBD.
