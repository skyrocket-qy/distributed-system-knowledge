# Distributed Transactions

## Core

In distributed systems, a **distributed transaction** is a transaction that involves multiple participants (e.g., databases, services) that are located on different network hosts. The primary challenge is to ensure atomicity, consistency, isolation, and durability (ACID properties) across all participating nodes, even in the face of network failures or node crashes.

Traditional ACID transactions are straightforward in a single-node environment. However, extending these guarantees to a distributed setting introduces significant complexity and overhead, often leading to trade-offs in performance and availability.

### Key Challenges

-   **Atomicity:** Ensuring that either all operations within the transaction succeed, or all of them are rolled back.
-   **Consistency:** Guaranteeing that the transaction brings the system from one valid state to another.
-   **Isolation:** Ensuring that concurrent transactions do not interfere with each other.
-   **Durability:** Confirming that once a transaction is committed, its changes are permanent, even if the system fails.
-   **Network Latency:** The time taken for messages to travel between participants can significantly slow down distributed transactions.
-   **Partial Failures:** Handling situations where some participants fail while others succeed, making it difficult to coordinate a global commit or rollback.

## Mechanisms

| Mechanism | Description | Trade-offs | Use Case |
|---|---|---|---||
| **Two-Phase Commit (2PC)** | A classic atomic commitment protocol that ensures all participants either commit or abort a transaction. It involves a coordinator and multiple participants. | High latency, blocking, single point of failure (coordinator) | Distributed databases, enterprise systems requiring strong consistency |
| **Three-Phase Commit (3PC)** | An extension of 2PC designed to be non-blocking in the face of coordinator failure, by adding a "prepare to commit" phase. | More complex, still susceptible to network partitions, higher overhead than 2PC | Systems where blocking is unacceptable, but strong consistency is still desired |
| **Saga Pattern** | A sequence of local transactions, where each local transaction updates its own database and publishes an event. If a step fails, compensating transactions are executed to undo the preceding steps. | Eventual consistency, increased complexity in error handling, no global rollback | Microservices architectures, long-running business processes |
| **Distributed Sagas (Orchestration/Choreography)** | Different approaches to managing the flow of sagas, either through a central orchestrator or by participants reacting to events. | Orchestration: Centralized control, easier to manage complex workflows. Choreography: Decentralized, more resilient to orchestrator failure, harder to monitor. | Microservices, complex business workflows |

## Which service use it?

-   **Two-Phase Commit (2PC):** Used in traditional distributed relational databases (e.g., XA transactions in Oracle, SQL Server) and some enterprise application servers.
-   **Saga Pattern:** Widely adopted in modern microservices architectures (e.g., e-commerce platforms, order processing systems) to maintain data consistency across multiple services without using distributed transactions.
