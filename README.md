# Documentation as Code

AI is only as useful as what it can read. Most documents live in Word, PowerPoint, and SharePoint, where AI cannot read, edit, or trust them. Store knowledge as text in Git and every team gets accurate answers, instant diagrams, and one-step updates. Do it across an organization and you get an AI brain.

The repository makes that case, gives a crash course you can present, and proves it with demos you can run yourself.

**Diagram: Text in Git turns documents into inputs for the company AI brain**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    d["Documents AI cannot read"] -->|"store as text in Git"| t["Documents AI can read and edit"]
    t --> a["Accurate answers"]
    t --> g["Instant diagrams"]
    t --> u["One-step updates"]
    a --> b["Company AI brain"]
    g --> b
    u --> b
    class d c5
    class t c3
    class a,g,u c2
    class b c1
```

## Who this is for

The material is for anyone who writes, reads, or relies on documentation, in any team or company. No technical background is needed.

- **Technical terms:**
  - Each term is explained where it appears.
  - The [glossary](education/060-glossary.md) defines every one.

**Diagram: Any reader can read the education pages without technical background because the glossary defines each term**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    p["Any reader"] -->|"reads"| e["Education pages"]
    e -->|"terms defined in"| g["Glossary"]
    class p c1
    class e c2
    class g c3
```

## Start here

- **Step 1 - read the case:**
  - Open the [eight-minute crash course](education/005-crash-course.md). It is a sequence of diagrams that you can read or present.
- **Step 2 - go deeper:**
  - Open the [education folder](education/README.md) for the full argument.
- **Step 3 - try it:**
  - Clone this repository.
  - Open the folder in your AI tool.
  - Follow a [demo project](demo/README.md) and ask it about a fictional company's documentation.

```bash
git clone <repository-url>
```

**Diagram: A reader moves from the summary to the full argument and then to the demo**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Read the case"] --> b["Go deeper"]
    b --> c["Try the demo"]
    class a,b c1
    class c c3
```

## What is in this repository

**Diagram: The repository is organized into an argument, demos, checks and working files**

```mermaid
flowchart TD
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    r["This repository"] --> e["education/ - the argument"]
    r --> d["demo/ - four demo projects"]
    r --> t["tools/ - documentation checks"]
    r --> ts["TESTING.md - how the repo is verified"]
    r --> a["AGENTS.md - rules for AI tools"]
    r --> p["PLAN.md and DECISIONS.md - status and reasons"]
    class r c3
    class e,d,t,ts,a,p c1
```

| Path                              | Job                                                                                                       | Why it is separate                                                                                     |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| [education/](education/README.md) | The argument at two lengths: an eight-minute crash course and long-form pages, all diagram-led            | Readers need it in order, without code or demo material in the way                                     |
| [demo/](demo/README.md)           | Four self-contained demo projects, each with documentation, diagrams, a presenter guide, and a reset step | The AI is pointed here to answer questions and make changes live, and a throwaway Git branch resets it |
| [tools/](tools/README.md)         | A script that checks links and that every diagram renders, and tests for that script                      | Keeps the documentation honest, the same way tests keep code honest                                    |
| [AGENTS.md](AGENTS.md)            | Instructions any AI tool reads before working here                                                        | One file keeps behavior consistent across tools                                                        |
| [TESTING.md](TESTING.md)          | The checks that protect each workflow, how to run them, and what they cannot see                          | Tells you what to run after each kind of change                                                        |
| [PLAN.md](PLAN.md)                | Current goal, progress, and the next action                                                               | Lets anyone, or any AI, resume work without asking                                                     |
| [DECISIONS.md](DECISIONS.md)      | Why the repository looks the way it does                                                                  | Prevents re-deciding settled questions                                                                 |

## Verify the documentation

The script confirms that every link resolves and every diagram renders. The repository follows its own rule: documentation is checked like code. [TESTING.md](TESTING.md) says what to run after each kind of change.

```bash
python3 tools/check-docs.py
```

**Diagram: The check script reads every page and reports whether links resolve and diagrams render**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    s["check-docs.py"] -->|"reads"| f["Every Markdown page"]
    f -->|"links"| l["Resolve to files"]
    f -->|"diagrams"| d["Render without errors"]
    l --> r["Pass or fail report"]
    d --> r
    class s c2
    class f c3
    class l,d c4
    class r c1
```
