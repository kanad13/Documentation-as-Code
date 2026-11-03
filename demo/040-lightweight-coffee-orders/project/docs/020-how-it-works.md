# Coffee Orders: How It Works

The cashier enters the order on the counter screen and takes payment. The order appears on the barista screen, and the barista calls the customer's name at pickup.

## Components

**Diagram: The customer orders at the counter and pays at the card reader, and the barista screen shows the order**

```mermaid
flowchart LR
    classDef default fill:#64748B1F,stroke:#64748B,stroke-width:1.5px;
    classDef c1 fill:#2563EB24,stroke:#3B82F6,stroke-width:2px;
    classDef c2 fill:#7C3AED24,stroke:#8B5CF6,stroke-width:1.5px;
    classDef c3 fill:#05966924,stroke:#10B981,stroke-width:1.5px;
    classDef c4 fill:#D9770624,stroke:#F59E0B,stroke-width:1.5px;
    classDef c5 fill:#DC262624,stroke:#EF4444,stroke-width:2px;
    cu["Customer"] -->|"orders"| co["Counter screen"]
    cu -->|"pays"| cr["Card reader"]
    co -->|"sends order"| ba["Barista screen"]
    ba -->|"calls name at pickup"| cu
    class cu c3
    class co c1
    class cr c4
    class ba c2
```

| Component      | Job                                   |
| :------------- | :------------------------------------ |
| Counter screen | Takes the order                       |
| Card reader    | Takes payment                         |
| Barista screen | Shows orders in the order they arrive |

## Rules

- Every order is entered at the counter.
- Orders show on the barista screen in the order they arrive.
