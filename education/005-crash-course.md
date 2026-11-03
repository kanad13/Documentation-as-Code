# Crash Course: Documentation as Code in Sixteen Diagrams

Sixteen diagrams, about eight minutes, that take a non-technical audience from "documents are fine as they are" to "documentation should be code" and into a demo. Each diagram answers the question the previous one raises, so you can read the file top to bottom or present it one diagram at a time.

## About the diagram titles

Each diagram carries a `title:` block inside its code, matching the caption above it. A title is shortened only where a long one would be cut off, as in the sequence diagram. A presenter who copies only the diagram into a slide keeps its title. This is a deliberate exception to the usual rule that the caption alone titles a diagram.

## Who this is for

- **Presenters:**
  - Copy each diagram into a slide, or show the file as it is.
  - Preview the diagrams in any previewer that shows Mermaid.
- **Readers with eight minutes:**
  - Read the headings and look at the diagrams. The argument stands without the text.
- **Readers with more time:**
  - Follow the [education folder](README.md). It gives the same argument in depth, and its map shows which section matches each diagram here.

## The objective

- **Goal:**
  - The audience leaves convinced, and ready to see a demo prove the point.
- **The argument in one line:**
  - AI is only as useful as what it can read, and most knowledge sits in Word, PowerPoint, and SharePoint, where AI cannot read, edit, or trust it.
- **Test for every diagram:**
  - A viewer who sees only that diagram understands one new point.
  - No other diagram makes the same point.

## The sequence

| #   | Act           | Message                                                            | The question it answers                    |
| :-- | :------------ | :----------------------------------------------------------------- | :----------------------------------------- |
| 1   | Why now       | Documents now have two readers                                     | Why does this matter today?                |
| 2   | Why now       | Changes to the system never reach Word, PowerPoint, or SharePoint  | What is wrong with how teams work?         |
| 3   | Why now       | AI cannot use those formats                                        | Why does AI make it worse?                 |
| 4   | What it costs | Stale diagrams erode trust until nobody updates anything           | What does it do over time?                 |
| 5   | What it costs | The cost shows up in onboarding, incidents, leadership, and audits | Who feels it?                              |
| 6   | The fix       | AI is only as useful as what it can read                           | What is the insight?                       |
| 7   | The fix       | Documentation as code is three changes: text, diagram recipes, Git | What is it called, and what is it made of? |
| 8   | The fix       | Each format has a text replacement                                 | What does it replace?                      |
| 9   | The fix       | A diagram becomes a recipe that anyone can edit                    | How can a diagram be text?                 |
| 10  | The fix       | Git records, reviews, and undoes every change                      | How do you trust a change?                 |
| 11  | The payoff    | Trust and accuracy reinforce each other                            | What changes?                              |
| 12  | The payoff    | Text in Git gives three capabilities: ask, draw, update            | What can you do with it?                   |
| 13  | The payoff    | One described change reaches every file and waits for approval     | What does update look like?                |
| 14  | The payoff    | Text from every team lets one AI assistant answer from all of it   | Where does this lead?                      |
| 15  | The steps     | Four phases from one pilot to the AI brain                         | What must a team do?                       |
| 16  | The demo      | The demo moves from a question to a rule change to an audit        | What happens next?                         |

## Act 1: Why now

### 1. Documents now have two readers

**Diagram: Documents now have two readers, a person and AI**

```mermaid
---
title: "Documents now have two readers, a person and AI"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    d["Document in Word, PowerPoint or SharePoint"] -->|"always read by"| p["Person"]
    d -->|"now also read and edited by"| a["AI"]
    class d c3
    class p c1
    class a c2
```

### 2. Changes never reach the documents

**Diagram: A change to the system gives Word, PowerPoint and SharePoint no prompt to update**

```mermaid
---
title: "A change to the system gives Word, PowerPoint and SharePoint no prompt to update"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    c["System change - code in Git"] -->|"no prompt to update"| w1["Word"]
    c -->|"no prompt to update"| w2["PowerPoint"]
    c -->|"no prompt to update"| w3["SharePoint"]
    class c c1
    class w1,w2,w3 c5
```

### 3. AI cannot use those formats

**Diagram: Word, PowerPoint and SharePoint each block AI in a different way**

```mermaid
---
title: "Word, PowerPoint and SharePoint each block AI in a different way"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    w1["Word - changes cannot be compared"] --> ai["AI"]
    w2["PowerPoint - diagrams are pictures AI cannot edit"] --> ai
    w3["SharePoint - five pages, no way to pick the true one"] --> ai
    class w1,w2,w3 c5
    class ai c2
```

## Act 2: What it costs

### 4. Stale diagrams erode trust

**Diagram: A stale diagram erodes trust until nobody updates the documentation**

```mermaid
---
title: "A stale diagram erodes trust until nobody updates the documentation"
---
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Someone pastes a diagram into PowerPoint or Word"] --> b["The system changes"]
    b --> c["Redrawing takes 30 minutes<br/>or the original file is lost"]
    c --> d["The picture is now wrong"]
    d --> e["People stop trusting the documentation"]
    e --> f["People stop reading and updating it"]
    f --> b
    class a,b c1
    class c,d,e,f c5
```

### 5. Who feels the cost

**Diagram: Untrusted Word, PowerPoint and SharePoint documents cost time in four places**

```mermaid
---
title: "Untrusted Word, PowerPoint and SharePoint documents cost time in four places"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    u["Untrusted Word, PowerPoint and SharePoint documents"] --> c1["Slow onboarding"]
    u --> c2["Wrong turns in incidents"]
    u --> c3["Late leadership answers"]
    u --> c4["Unknown policy impact"]
    class u c5
    class c1,c2,c3,c4 c4
```

## Act 3: The fix

### 6. The insight

**Diagram: AI is only as useful as what it can read, so knowledge belongs in text in Git**

```mermaid
---
title: "AI is only as useful as what it can read, so knowledge belongs in text in Git"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["AI is only as useful as what it can read"] -->|"but most knowledge sits in"| b["Word, PowerPoint and SharePoint"]
    b -->|"so convert it to"| c["Text in Git"]
    class a c2
    class b c5
    class c c3
```

### 7. What it is called

**Diagram: Documentation as code rests on three changes: text, diagram recipes and Git**

```mermaid
---
title: "Documentation as code rests on three changes: text, diagram recipes and Git"
---
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

### 8. What it replaces

**Diagram: Each of today's formats is replaced by a text format that AI can use**

```mermaid
---
title: "Each of today's formats is replaced by a text format that AI can use"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    subgraph from ["Today"]
        direction TB
        a1["Word documents"]
        a2["PowerPoint diagrams"]
        a3["SharePoint pages"]
    end
    subgraph to ["Documentation as code"]
        direction TB
        b1["Plain text - Markdown"]
        b2["Diagrams as text - Mermaid and D2"]
        b3["Git - tracked, reviewed, undoable"]
    end
    a1 -->|"replaced by"| b1
    a2 -->|"replaced by"| b2
    a3 -->|"replaced by"| b3
    class a1,a2,a3 c5
    class b1,b2,b3 c3
    style from fill:#64748B12,stroke:#64748B,stroke-width:1px,stroke-dasharray:4 4
    style to fill:#64748B12,stroke:#64748B,stroke-width:1px,stroke-dasharray:4 4
```

### 9. A diagram becomes a recipe

**Diagram: A diagram recipe is text, so changing one line redraws the diagram**

```mermaid
---
title: "A diagram recipe is text, so changing one line redraws the diagram"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    e["Person or AI changes one line"] -->|"edits"| r["Recipe - a few lines of text"]
    r -->|"drawn by software"| p["Diagram"]
    class e c2
    class r c3
    class p c1
```

### 10. Git makes change trustworthy

**Diagram: A draft branch merges into the official history only after a reviewer approves**

```mermaid
---
title: "A draft branch merges into the official history only after a reviewer approves"
---
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

## Act 4: The payoff

### 11. A loop that improves

**Diagram: Up-to-date documents earn trust that surfaces gaps for fixing**

```mermaid
---
title: "Up-to-date documents earn trust that surfaces gaps for fixing"
---
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Documentation is text in Git"] --> b["AI keeps it current in minutes"]
    b --> c["Documentation matches reality"]
    c --> d["People trust and use it"]
    d --> e["People ask AI instead of interrupting colleagues"]
    e --> f["Gaps surface fast and get fixed"]
    f --> a
    class a,b c1
    class c,d c3
    class e,f c2
```

### 12. Three capabilities

**Diagram: Text in Git gives three capabilities: ask, draw and update**

```mermaid
---
title: "Text in Git gives three capabilities: ask, draw and update"
---
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    k["Knowledge as text in Git"] --> a["Ask - any reader gets an answer with a source link"]
    k --> d["Draw - a diagram of any system in seconds"]
    k --> u["Update - one change reaches every file"]
    class k c3
    class a,d,u c2
```

### 13. What update looks like

**Diagram: One described change is applied to every affected file and waits for a person's approval**

```mermaid
---
title: "One change reaches every file and waits for approval"
---
sequenceDiagram
    actor You
    participant AI
    participant Docs as Docs in Git
    You->>AI: EU customer data must now stay in the EU
    AI->>Docs: Reads every file that mentions the old design
    AI->>Docs: Edits overview, architecture, runbook and decision log
    AI->>Docs: Redraws the diagrams
    AI-->>You: Shows exactly what changed, line by line
    You->>Docs: Approves - Git records who, when and why
```

### 14. The company AI brain

The benefit of writing in text is that text is what an AI brain is built from. Any organization that does this can point one assistant at all of it.

**Diagram: Text from every team lets one AI assistant answer each reader from all of it**

```mermaid
---
title: "Text from every team lets one AI assistant answer each reader from all of it"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    t1["Team A docs"] --> i(("Organization knowledge"))
    t2["Team B docs"] --> i
    t3["Every other team's docs"] --> i
    i --> ai["AI assistant"]
    ai -->|"status"| q1["Executive"]
    ai -->|"connections"| q2["Engineer"]
    ai -->|"where to start"| q3["New hire"]
    ai -->|"controls"| q4["Auditor"]
    class t1,t2,t3 c1
    class i c3
    class ai c2
    class q1,q2,q3,q4 c5
```

## Act 5: The steps and the demo

### 15. What a team does

Any team or organization that wants to use AI on its own knowledge follows these steps.

**Diagram: Four phases take one pilot project to an organization-wide AI brain**

```mermaid
---
title: "Four phases take one pilot project to an organization-wide AI brain"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    p1["1. Pilot - one project, one month"] --> p2["2. Standard - every new project"]
    p2 --> p3["3. Convert - old docs, when touched"]
    p3 --> p4["4. AI brain - all teams"]
    class p1,p2,p3 c1
    class p4 c3
```

### 16. What happens next

**Diagram: The demo moves from a question to a rule change to an audit**

```mermaid
---
title: "The demo moves from a question to a rule change to an audit"
---
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Ask - questions about a fictional company's sales platform"] --> b["Change - a new EU data rule"]
    b --> c["Redraw - text and diagrams updated together"]
    c --> d["Audit - find anything the change missed"]
    class a,b c1
    class c c2
    class d c3
```

---

**Next:** [010 The Case in Diagrams](010-the-case-in-diagrams.md) · **Index:** [Education](README.md)
