# Presenter Guide: Six-Minute Version

**Length:** About 6 minutes. **Message:** An AI answers questions from the documents and cites where it looked. Then one sentence changes a process, and the text and both diagrams change together, with green outlines that show exactly what moved.

## Before the audience arrives

1. Open a terminal in this folder.
2. Create a throwaway branch:

```bash
git switch -c demo-run
```

3. Open your AI tool in the [project/](project/README.md) folder. If it does not read [AGENTS.md](project/AGENTS.md) on its own, start with: "Read AGENTS.md and follow it."
4. Have a previewer ready that shows Mermaid diagrams, so you can show the pictures after the change. GitHub shows them in the browser, and most editors have a Mermaid preview. Use whichever you already have.

## Act 1: The starting point (30 seconds)

- Show the two diagrams: the customer's journey and the parts and how they connect.
- Say: "Both of these are text. There is no picture file behind them."

## Act 2: Ask (2 minutes)

Paste these one at a time. After each answer, point at the file the AI names.

- **What is here:**

```text
I have never seen these documents. In three sentences, tell me what is in this folder and what each document covers.
```

- **Facts:**

```text
How many orders does Bramble Coffee handle in a day, how long does a customer wait on average, and who owns the process? Name the file for each answer.
```

- **Risks:**

```text
What are the risks, and which one is rated Medium?
```

- **A busy executive:**

```text
I am a busy executive. Give me a three-bullet briefing I can read in 20 seconds.
```

- **A question the documents cannot answer:**

```text
How much does Bramble Coffee spend on coffee beans each month?
```

- Say: "Watch what it does when the answer is not in the documents."

## Act 3: The change (2 minutes)

- **Say:** "The owner just decided to take mobile pre-orders."
- **Prompt:**

```text
Bramble Coffee is adding mobile pre-orders. Customers order and pay in a mobile app, then collect from a pickup shelf without queuing at the counter. The barista screen shows app orders before counter orders. Update every affected file and diagram, and summarize what changed.
```

- **Show, in this order:**
  - The AI's summary.
  - Your previewer, refreshed: new boxes and arrows outlined in green in both diagrams.
  - `git diff --stat`.
- **Point out:** The text and both diagrams changed from one sentence.

## Act 4: Clean up (30 seconds)

- **Say:** "The change is reviewed, so the highlights have done their job."
- **Prompt:**

```text
The change has been reviewed. Remove the green highlights from both diagrams and keep everything else exactly as it is.
```

- Refresh your previewer: same new boxes, no outlines.
- Commit:

```bash
git add -A && git commit -m "Add mobile pre-orders"
```

## Answer key

### Questions

| Question     | Expected answer                                                                                                                                                  | Where                       |
| :----------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| What is here | Two documents: an overview (key facts, the customer's journey, risks) and a how-it-works document (components, the diagram, rules), plus the rules for AI agents | `project/`                  |
| Facts        | About 420 orders a day, an average wait of 4 minutes, and the store manager owns it                                                                              | `010-overview.md`, Snapshot |
| Risks        | Queues at the counter at 8 a.m. (Medium) and orders mistyped at the counter (Low)                                                                                | `010-overview.md`, Risks    |
| Briefing     | Three short bullets drawn from the overview                                                                                                                      | Both documents              |
| Coffee beans | The documents do not say, and the AI should not invent a figure                                                                                                  | None                        |

### The change

| File | Where                                                                                            |
| :--- | :----------------------------------------------------------------------------------------------- |
| 010  | The intro, the customer journey diagram (an app path), and the snapshot or risks                 |
| 020  | The intro, the components diagram (a mobile app and a pickup shelf), the components table, and the rules |

## Rehearsal notes

A second independent run with a small, fast AI model (Haiku) and no other context handled every prompt in this guide on the Mermaid-only version. Expect similar results.

- **Time:** About one minute of AI work for the change.
- **What it did:**
  - Updated both documents and both diagrams, and marked new or changed nodes with the `changed` class.
  - Kept the `classDef` setup, and both diagrams compiled.
  - Wrote `TBD` for what it could not know: the app's payment provider, the wait for app orders, and who moves app orders to the shelf.
- **The questions:** All five were answered correctly with the file named. For the coffee-bean question the model answered `TBD` and did not invent a figure.
- **The cleanup:** The model removed the highlights without changing any text. It gave each formerly highlighted node the color of its role, because the rules require every node to keep a class. If your model leaves a highlight behind, ask once more.
- **A good line:** The `TBD` entries are the gaps the owner never filled. That gap is what the human review is for.

## Pair it with the crash course

- **Short slot:** Present the [crash course](../../education/005-crash-course.md), then run this demo. That is about 14 minutes.
- **Tight slot:** Show crash-course diagrams 1, 4, 8, and 13, then run this demo.

## Reset

```bash
git switch main && git branch -D demo-run
```

## If something goes wrong

- **The AI changes more than you asked:** Read its summary aloud and ask it to undo the extra part. That is also a good demo.
- **The AI invents a bean cost:** Ask "Which document says that?" and let the audience see that none does.
