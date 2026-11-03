# The Case in Diagrams

**Diagram: The case runs from decaying documents to a company AI brain in six steps**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    s1["1. Documents decay"] --> s2["2. AI cannot help"]
    s2 --> s3["3. Change the format"]
    s3 --> s4["4. One change updates everything"]
    s4 --> s5["5. A loop that improves"]
    s5 --> s6["6. Company AI brain"]
    class s1,s2 c5
    class s3,s4,s5 c1
    class s6 c3
```

Read time: 3 minutes. The whole argument appears as one picture per step. The pages that follow give the detail behind each picture.

---

## The claim

> AI is only as useful as what it can read. Most knowledge sits in files AI cannot read or edit. Move it to text, and the company gets an AI brain.

**Diagram: AI uses only the knowledge it can read, so converting knowledge to text builds the AI brain**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["AI reads and edits documents"] -->|"uses only what it can read"| b["Knowledge in files AI cannot read"]
    b -->|"convert to text in Git"| c["Knowledge AI can read and edit"]
    c -->|"repeat in every team"| d["Company AI brain"]
    class a c2
    class b c5
    class c c3
    class d c1
```

---

## Step 1. Today, documentation decays on its own

The format causes the decay. Nobody decides to let documentation rot.

**Diagram: A stale diagram erodes trust until nobody updates the documentation**

```mermaid
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Someone pastes a diagram as a picture"] --> b["The system changes"]
    b --> c["Redrawing takes 30 minutes<br/>or the original file is lost"]
    c --> d["The picture is now wrong"]
    d --> e["People stop trusting the documentation"]
    e --> f["People stop reading and updating it"]
    f --> b
    class a,b c1
    class c,d,e,f c5
```

---

## Step 2. AI cannot break this loop with today's formats

**Diagram: Each of today's formats blocks AI in a different way**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    p["PowerPoint diagram"] -->|"cannot be edited"| x["AI"]
    w["Word document"] -->|"changes cannot be compared"| x
    s["Five SharePoint pages"] -->|"no way to pick the true one"| x
    class p,w,s c5
    class x c2
```

---

## Step 3. The fix: three changes of format

**Diagram: Each of today's formats is replaced by a text format that AI can use**

```mermaid
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

---

## Step 4. One change updates everything

**Diagram: One description of a change updates every affected file after a person approves**

```mermaid
sequenceDiagram
    actor You
    participant AI
    participant Docs as Docs in Git
    You->>AI: EU customer data must now stay in the EU
    AI->>Docs: Reads every file that mentions the old design
    AI->>Docs: Edits the text and redraws the diagrams
    AI-->>You: Shows exactly what changed, line by line
    You->>Docs: Approves - Git records who, when and why
```

---

## Step 5. The result: a loop that improves

**Diagram: Up-to-date documents earn trust that surfaces gaps for fixing**

```mermaid
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

---

## Step 6. The destination: a company AI brain

Every answer links to its source file, so anyone can check it.

**Diagram: The AI assistant answers each reader from every team's documentation**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    t1["Team A docs"] --> i(("Company knowledge"))
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

---

## The decision

This is the standard to adopt. [The plan](050-adopting-it.md) shows how.

**Diagram: Converting documents to text in stages leads to one AI brain**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    n["Now"] -->|"new docs start as Markdown in Git"| m["Next quarter"]
    m -->|"old docs convert when touched"| l["Next year"]
    l --> b["One AI brain over all company knowledge"]
    class n,m,l c1
    class b c3
```

---

**Next:** [020 The Problem](020-the-problem.md) · **Index:** [Education](README.md)
