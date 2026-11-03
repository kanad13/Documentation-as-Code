# Coffee Orders: How It Works

The cashier enters the order on the counter screen and takes payment. The order appears on the barista screen, and the barista calls the customer's name at pickup.

## Components

```d2
vars: {
  d2-config: {
    layout-engine: tala
    pad: 24
    theme-id: 0
    dark-theme-id: 200
  }
}

direction: right

customer: Customer {shape: person}
counter: Counter screen
reader: Card reader {
  shape: cloud
  style.stroke-dash: 4
}
barista: Barista screen
customer -> counter: orders
customer -> reader: pays
counter -> barista: sends order
barista -> customer: calls name at pickup
```

| Component      | Job                                   |
| :------------- | :------------------------------------ |
| Counter screen | Takes the order                       |
| Card reader    | Takes payment                         |
| Barista screen | Shows orders in the order they arrive |

## Rules

- Every order is entered at the counter.
- Orders show on the barista screen in the order they arrive.
