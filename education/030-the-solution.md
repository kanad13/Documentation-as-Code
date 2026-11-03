# The Solution: Documentation as Code

Documentation as code means writing documentation with the tools and habits software teams use for code. Three changes do the work.

**Diagram: Documentation as code rests on three changes: text, diagram recipes and Git**

```mermaid
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    d["Documentation as code"] -->|"1"| t["Text, not files"]
    d -->|"2"| r["Diagrams as recipes"]
    d -->|"3"| g["Git, not SharePoint folders"]
    t --> tt["Markdown"]
    r --> rr["Mermaid and D2"]
    g --> gg["History, review, undo"]
    class d c1
    class t,r,g c2
    class tt,rr,gg c3
```

## 1. Text, not files

**Markdown** is plain text with light marks for structure. A `#` makes a heading and a `-` makes a bullet. Displayed, it looks like any formatted document.

```text
# Payments Platform

## Status
- Launch: **on track** for March
- Top risk: partner onboarding delays
```

- **Why text:**
  - Software engineers, version control, and AI all handle plain text natively.
  - No other format works for all three without conversion.
- **What you need to do:**
  - Read the formatted result.
  - Ask the AI to write or change the text.
  - Skip learning Markdown syntax.

**Diagram: Plain text serves people, AI and Git at once**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    t["Plain text with # and - marks"] -->|"displays as"| p["Formatted page for people"]
    t -->|"read and edited by"| a["AI"]
    t -->|"tracked by"| g["Git"]
    class t c3
    class p c1
    class a c2
    class g c4
```

## 2. Diagrams as recipes, not pictures

**Mermaid** and **D2** turn a few lines of text into a diagram.

- **Analogy:**
  - A photo of a whiteboard cannot be edited.
  - A recipe can: change "2 eggs" to "3 eggs" and the dish changes.
  - A diagram recipe works the same way: add one line and a new box and arrow appear.

The recipe for a small diagram follows. Styling lines are left out.

```text
flowchart LR
    Customer --> Website --> Payments --> Bank
```

**Diagram: A one-line recipe is drawn by software into this diagram**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    c["Customer"] --> w["Website"]
    w --> p["Payments"]
    p --> b["Bank"]
    class c c1
    class w,p c2
    class b c5
```

To add a fraud check between Website and Payments, add one word to the recipe. A person can do it. AI can do it in seconds.

**Diagram: Adding one word to the recipe adds a fraud check between Website and Payments**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    c["Customer"] --> w["Website"]
    w --> f["FraudCheck"]
    f --> p["Payments"]
    p --> b["Bank"]
    class c c1
    class w,p c2
    class f c4
    class b c5
```

- **Which tool when:**
  - Mermaid draws flows, sequences, timelines, and state diagrams. Most code platforms show it automatically.
  - D2 suits large architecture diagrams with many nested parts. It gives finer control over layout.

## 3. Git, not SharePoint folders

**Git** stores every version of every file, with who changed it, when, and why.

- **Analogy:**
  - Track Changes in Word, applied to the whole project, forever.
  - Each change carries an explanation and a one-click undo.

| Term           | Meaning                                                   |
| :------------- | :-------------------------------------------------------- |
| **Repository** | A project folder that Git keeps history for               |
| **Commit**     | One saved change, with a note explaining it               |
| **Diff**       | A side-by-side view of what a change added and removed    |
| **Review**     | A person checks the diff and approves it before it counts |

**Diagram: A draft branch merges into the official history only after a reviewer approves**

```mermaid
gitGraph
    commit id: "Initial architecture"
    commit id: "Add fraud check"
    branch eu-data-rule
    commit id: "Add EU data boundary"
    commit id: "Redraw diagrams"
    checkout main
    merge eu-data-rule id: "Approved by reviewer"
    commit id: "Update runbook"
```

- **How to read the picture:**
  - Each dot is a saved change.
  - The branch is a draft that nobody sees until a reviewer approves it.
  - Review is how you see exactly what an AI changed before it becomes the truth.

## How a change moves through the system

A person decides. The AI does the typing.

**Diagram: The AI drafts a change and a person approves it before it becomes official**

```mermaid
sequenceDiagram
    actor Person
    participant AI
    participant Draft as Draft copy in Git
    participant Main as Official docs
    Person->>AI: Describes what changed
    AI->>Draft: Updates text and diagrams in every affected file
    AI-->>Person: Shows the diff
    Person->>Draft: Approves, or asks for adjustments
    Draft->>Main: Merged, recorded with author and reason
```

## Why each change fixes a failure from before

Every failure named in [the problem](020-the-problem.md) has a matching fix.

**Diagram: Each failure has a matching fix that keeps documentation accurate**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    f1["Dead-pixel diagrams"] --> s1["Diagrams as text - edited in seconds"]
    f2["Docs apart from the work"] --> s2["Docs in the same repository as the work"]
    f3["Machines cannot read them"] --> s3["Text - AI reads, edits and cites it"]
    f4["No history or accountability"] --> s4["Git - author, time, reason, undo"]
    s1 --> g["Documentation stays accurate"]
    s2 --> g
    s3 --> g
    s4 --> g
    class f1,f2,f3,f4 c5
    class s1,s2,s3,s4 c2
    class g c3
```

---

**Previous:** [020 The Problem](020-the-problem.md) · **Next:** [040 The Payoff](040-the-payoff.md) · **Index:** [Education](README.md)
