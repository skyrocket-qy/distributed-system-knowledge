# Idempotency

## Core

**Idempotency** is the property of an operation that, when executed multiple times with the same parameters, produces the same result or causes the same side effect as if it were executed only once. In distributed systems, where network issues, retries, and partial failures are common, designing idempotent operations is crucial for ensuring correctness and reliability.

Without idempotency, retrying failed operations could lead to unintended side effects, such as duplicate data entries, incorrect financial transactions, or inconsistent system states.

### Key Considerations

-   **Side Effects:** Operations should be designed so that any external changes (e.g., database writes, external API calls) are only applied once, even if the operation itself is processed multiple times.
-   **Unique Identifiers:** Using unique transaction IDs or message IDs can help in detecting and discarding duplicate requests.
-   **State Management:** For stateful operations, carefully manage the state to ensure that re-processing an operation doesn't alter the state beyond its initial intended change.
-   **External Systems:** Consider the idempotency guarantees of any external services or databases that your system interacts with.

## Characteristics

- **Safety**: Idempotent operations are safe to retry.
- **Determinism**: Idempotent operations produce the same result every time they are called with the same parameters.
- **Side Effects**: Idempotent operations have the same side effects every time they are called with the same parameters.
- **Fault Tolerance**: Idempotency is a key technique for building fault-tolerant systems.

## Comparison

| Operation | Idempotent |
|---|---|
| `x = 5` | Yes |
| `x++` | No |
| `DELETE /users/123` | Yes |
| `POST /users` | No |

## Trade-offs

- **Complexity**: Implementing idempotency can add complexity to the system.
- **Performance**: Idempotency can introduce performance overhead.
- **State Management**: Idempotency can require additional state management.

## Implementation Strategies

-   **Unique Transaction IDs:** Assign a unique ID to each operation. Before processing, check if this ID has already been processed. If so, return the previous result without re-executing the operation.
-   **Conditional Updates:** Use conditional updates (e.g., `UPDATE ... WHERE version = X`) in databases to ensure that an update only applies if the expected state is still present.
-   **Deduplication Layers:** Implement a layer that filters out duplicate messages or requests based on their unique identifiers.
-   **Atomic Operations:** Leverage atomic operations provided by databases or distributed locks to ensure that a critical section of code is executed only once.

## Which service use it?

-   **Payment Gateways:** To prevent double-charging customers if a payment request is retried.
-   **Order Processing Systems:** To ensure that an order is created only once, even if the order creation request is sent multiple times.
-   **Message Queues:** Consumers of message queues often implement idempotency to handle duplicate messages that can arise from "at-least-once" delivery guarantees.
-   **API Design:** Public APIs often require idempotent endpoints for operations like creating resources (using a client-generated ID) or updating resources.

## Related Concepts

-   **Fault Tolerance:** Idempotency is a key technique for building fault-tolerant systems, as it allows for safe retries of operations in the face of transient failures. [Understand Fault Tolerance](../README.md).
-   **Distributed Transactions:** In distributed transactions, especially with patterns like Saga, idempotency helps in making compensating transactions safe to retry. [Explore Distributed Transactions](../../distributed-transactions/README.md).
-   **Messaging:** Essential for consumers of message queues to handle duplicate messages that can occur with "at-least-once" delivery semantics. [Learn about Messaging](../../messaging/README.md).
-   **Consistency Models:** Idempotency contributes to maintaining consistency in distributed systems by preventing unintended state changes from repeated operations. [Explore Consistency Models](../../consistency-models/README.md).
