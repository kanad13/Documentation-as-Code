# Adopting It: The New Standard

Adopt documentation as code as the way you document. The steps are small and start today.

**Diagram: Adoption runs from five rules through a four-phase roadmap to defined roles and a first step**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    r["Five rules"] --> p["Four-phase roadmap"]
    p --> w["Roles"]
    w --> s["Start this week"]
    class r,p,w c1
    class s c3
```

## Five rules

- **Rule 1:**
  - New documentation starts as Markdown in Git.
  - Living knowledge gets no new Word documents.
- **Rule 2:**
  - Diagrams are text.
  - Use Mermaid for flows, sequences, timelines, and states.
  - Use D2 for large architecture.
  - Add no new pasted images of diagrams.
- **Rule 3:**
  - Each fact has one home.
  - State the fact in one file and link to it everywhere else.
- **Rule 4:**
  - Documentation changes with the work.
  - A change to a system includes the change to its documentation, reviewed together.
- **Rule 5:**
  - A person approves every AI edit.
  - The reviewer reads the diff, the same way a code change is reviewed.

**Diagram: Five rules together form the documentation standard**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    r1["New docs as Markdown"] --> s["Documentation standard"]
    r2["Diagrams as text"] --> s
    r3["One home per fact"] --> s
    r4["Docs change with the work"] --> s
    r5["People approve AI edits"] --> s
    class r1,r2,r3,r4,r5 c1
    class s c3
```

## What belongs in Git, and what does not

Architecture, decisions, processes, runbooks, policies, project status, and onboarding guides belong in Git. One-time records stay as they are.

**Diagram: Knowledge that changes and that people rely on belongs in Git**

```mermaid
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    q{"Will this knowledge change over time?"}
    q -->|"Yes"| l{"Must anyone rely on it being current?"}
    q -->|"No - one-time record"| x["Keep as it is - signed contract, filed report"]
    l -->|"Yes"| g["Markdown in Git"]
    l -->|"No"| x
    class q,l c4
    class g c3
    class x c5
```

## Roadmap

**Diagram: Four phases take one pilot project to a company-wide AI brain**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    p1["1. Pilot - one project, one month"] --> p2["2. Standard - every new project"]
    p2 --> p3["3. Convert - old docs, when touched"]
    p3 --> p4["4. Brain - one index over all repositories"]
    class p1,p2,p3 c1
    class p4 c3
```

| Phase       | What happens                                                                                                      | Done when                                          |
| :---------- | :---------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| 1. Pilot    | One active project moves its docs into a repository. The team asks the AI questions and makes updates through it. | The team prefers it to the old way                 |
| 2. Standard | Every new project starts with a docs repository using the five rules.                                             | New projects have no pasted-image diagrams         |
| 3. Convert  | When someone touches an old document, AI converts it to Markdown and redraws its diagrams as text.                | Active projects are all converted                  |
| 4. Brain    | One index reads all repositories. The company assistant answers from it.                                          | Anyone can ask any team's documentation a question |

## Who does what

**Diagram: Each role does one job under the standard**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    s["Documentation standard"] -->|"describes and reviews"| a["Author"]
    s -->|"approves diffs"| r["Reviewer"]
    s -->|"reads or asks"| d["Reader"]
    s -->|"asks for status"| l["Leader"]
    class s c3
    class a,r,d,l c1
```

| Role         | What changes for them                                                                               |
| :----------- | :-------------------------------------------------------------------------------------------------- |
| **Author**   | Describes content to the AI and reviews the result. No Markdown syntax required.                    |
| **Reviewer** | Reads the before/after diff and approves, the same as reviewing a Word document with Track Changes. |
| **Reader**   | Opens the rendered page or asks the AI.                                                             |
| **Leader**   | Asks the AI for status and gets it from live files.                                                 |

## Start this week

- **Steps:**
  - Pick one active project.
  - Create a repository for its documentation.
  - Ask the AI to convert its main Word document to Markdown and its key diagrams to Mermaid.
  - Use the projects in the [demo folder](../demo/README.md) as the model.

**Diagram: Four steps start a pilot this week**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Pick one active project"] --> b["Create a documentation repository"]
    b --> c["Ask AI to convert the main document and diagrams"]
    c --> d["Use the demo project as the model"]
    class a,b,c c1
    class d c3
```

---

**Previous:** [040 The Payoff](040-the-payoff.md) · **Next:** [060 Glossary](060-glossary.md) · **Index:** [Education](README.md)
