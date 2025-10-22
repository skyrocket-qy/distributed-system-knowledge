# Saga Pattern

## Core

The **Saga Pattern** is a way to manage transactions that span multiple services in a distributed system, ensuring data consistency without using traditional distributed transactions (like Two-Phase Commit). It's particularly well-suited for microservices architectures where services have their own databases and strong ACID guarantees across services are difficult to achieve.

A Saga is a sequence of local transactions, where each local transaction updates its own database and publishes an event. If a local transaction fails, the Saga executes a series of compensating transactions to undo the changes made by the preceding local transactions.

### Key Principles

-   **Local Transactions:** Each step in a Saga is a local ACID transaction within a single service.
-   **Events:** Services communicate by publishing and subscribing to events.
-   **Compensating Transactions:** For every local transaction that modifies data, there's a corresponding compensating transaction that can undo its effects.
-   **Eventual Consistency:** Sagas achieve eventual consistency across the distributed system.

### Saga Orchestration

There are two main ways to coordinate Sagas:

1.  **Choreography:** Each service produces and listens to events, and decides what to do next without a central coordinator. This is decentralized and can be more resilient but harder to monitor and manage complex workflows.
2.  **Orchestration:** A central orchestrator (or Saga execution coordinator) tells each participant service what local transaction to execute. The orchestrator manages the sequence of steps and executes compensating transactions if a step fails. This provides a clearer view of the Saga's progress and simplifies error handling.

## Trade-offs

-   **Eventual Consistency:** Sagas provide eventual consistency, meaning that at any given point, the system might be in an inconsistent state until all local transactions and potential compensating transactions are completed.
-   **Increased Complexity in Error Handling:** Implementing compensating transactions and ensuring their correctness can be complex, as it requires careful design of the undo logic for each step.
-   **No Global Rollback:** Unlike traditional distributed transactions, there is no automatic global rollback. Instead, the system relies on compensating actions.
-   **Monitoring Challenges:** Especially with choreography, tracking the progress and state of a Saga across multiple services can be challenging without proper tooling.

## Use Case

-   **Microservices Architectures:** Widely adopted in modern microservices architectures (e.g., e-commerce platforms, order processing systems) to maintain data consistency across multiple services without using distributed transactions.
-   **Long-Running Business Processes:** Ideal for complex business workflows that involve multiple steps and services, where immediate global consistency is not strictly required.
-   **Systems Prioritizing Availability:** When high availability and partition tolerance are more critical than strong consistency, Sagas offer a viable alternative to blocking distributed transactions.

## Related Concepts

-   **Distributed Transactions:** The Saga pattern serves as a powerful alternative to traditional distributed transactions (like 2PC/3PC), especially in environments where strong ACID guarantees across services are impractical or undesirable. [Explore Distributed Transactions](../README.md).

-   **Eventual Consistency:** Sagas inherently achieve eventual consistency across the distributed system, meaning that while the system may temporarily be in an inconsistent state, it will eventually converge to a consistent state after all local and compensating transactions complete. [Learn more about Eventual Consistency](../../consistency-models/eventual-consistency/README.md).

-   **Messaging:** Sagas heavily rely on asynchronous messaging, often using event-driven communication, to coordinate local transactions between participating services and to trigger compensating actions. [Explore Messaging Systems](../../messaging/README.md).

-   **Microservices Architecture (System Mode):** The Saga pattern is a cornerstone for managing data consistency in microservices architectures, where each service typically owns its data and direct distributed transactions are avoided. [Discover System Modes](../../system-mode/README.md).

-   **Fault Tolerance:** Sagas contribute to fault tolerance by providing a structured way to handle failures within a distributed business process, allowing for recovery through compensating transactions rather than a complete rollback. [Understand Fault Tolerance](../../fault-tolerance/README.md).
