# Distributed Transactions

## Core

In distributed systems, a **distributed transaction** is a transaction that involves multiple participants (e.g., databases, services) that are located on different network hosts. The primary challenge is to ensure atomicity, consistency, isolation, and durability (ACID properties) across all participating nodes, even in the face of network failures or node crashes.

Traditional ACID transactions are straightforward in a single-node environment. However, extending these guarantees to a distributed setting introduces significant complexity and overhead, often leading to trade-offs in performance and availability. Consequently, in many modern distributed systems, especially microservices architectures, traditional distributed transactions (like 2PC/3PC) are often avoided in favor of alternative patterns that prioritize availability and partition tolerance, such as the Saga pattern, accepting eventual consistency.

### Key Challenges

-   **Atomicity:** Ensuring that either all operations within the transaction succeed, or all of them are rolled back.
-   **Consistency:** Guaranteeing that the transaction brings the system from one valid state to another.
-   **Isolation:** Ensuring that concurrent transactions do not interfere with each other.
-   **Durability:** Confirming that once a transaction is committed, its changes are permanent, even if the system fails.
-   **Network Latency:** The time taken for messages to travel between participants can significantly slow down distributed transactions.
-   **Partial Failures:** Handling situations where some participants fail while others succeed, making it difficult to coordinate a global commit or rollback.

## Characteristics

- **Atomicity**: All participants either commit or abort the transaction.
- **Consistency**: The transaction brings the system from one valid state to another.
- **Isolation**: Concurrent transactions do not interfere with each other.
- **Durability**: The outcome of the transaction is durable, even in the case of failures.
- **Complexity**: Distributed transactions are more complex than local transactions.

## Comparison

| Mechanism | Trade-offs | Use Case |
|---|---|---|
| **[Two-Phase Commit (2PC)](./two-phase-commit)** | High latency, blocking, single point of failure (coordinator) | Distributed databases, enterprise systems requiring strong consistency |
| **[Three-Phase Commit (3PC)](./three-phase-commit)** | More complex, still susceptible to network partitions, higher overhead than 2PC | Systems where blocking is unacceptable, but strong consistency is still desired |
| **[Saga Pattern](./saga-pattern)** | Eventual consistency, increased complexity in error handling, no global rollback | Microservices architectures, long-running business processes |

## Trade-offs

- **Performance**: Distributed transactions can be slow due to the overhead of coordination and network latency.
- **Availability**: Distributed transactions can be blocked if a participant is unavailable.
- **Complexity**: Distributed transactions are complex to implement and manage.

## Which service use it?

-   **Two-Phase Commit (2PC):** Used in traditional distributed relational databases (e.g., XA transactions in Oracle, SQL Server) and some enterprise application servers.
-   **Saga Pattern:** Widely adopted in modern microservices architectures (e.g., e-commerce platforms, order processing systems) to maintain data consistency across multiple services without using distributed transactions.
