# Coffee Orders: Overview

Coffee orders explains how a customer gets a drink at Bramble Coffee. Every order starts at the counter.

## Snapshot

| Item           | Detail                     |
| :------------- | :------------------------- |
| Owner          | Store manager              |
| Orders per day | About 420                  |
| Average wait   | 4 minutes                  |
| Payment        | Card reader at the counter |

## What a customer experiences

**Diagram: A customer orders at the counter and picks up a drink**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    a["Customer orders at the counter"] --> b["Customer pays"]
    b --> c["Barista makes the drink"]
    c --> d["Customer picks up"]
    class a,b c1
    class c c2
    class d c3
```

## Risks

| Risk                            | Impact |
| :------------------------------ | :----- |
| Queues at the counter at 8 a.m. | Medium |
| Orders mistyped at the counter  | Low    |
