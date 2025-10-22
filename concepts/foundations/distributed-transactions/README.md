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

## Mechanisms

| Mechanism | Trade-offs | Use Case |
|---|---|---|
| **[Two-Phase Commit (2PC)](./two-phase-commit)** | High latency, blocking, single point of failure (coordinator) | Distributed databases, enterprise systems requiring strong consistency |
| **[Three-Phase Commit (3PC)](./three-phase-commit)** | More complex, still susceptible to network partitions, higher overhead than 2PC | Systems where blocking is unacceptable, but strong consistency is still desired |
| **[Saga Pattern](./saga-pattern)** | Eventual consistency, increased complexity in error handling, no global rollback | Microservices architectures, long-running business processes |

## Which service use it?

-   **Two-Phase Commit (2PC):** Used in traditional distributed relational databases (e.g., XA transactions in Oracle, SQL Server) and some enterprise application servers.
-   **Saga Pattern:** Widely adopted in modern microservices architectures (e.g., e-commerce platforms, order processing systems) to maintain data consistency across multiple services without using distributed transactions.

## Related Concepts

-   **Consistency Models:** Distributed transactions aim to uphold strong consistency across multiple data stores, ensuring that all participants agree on the outcome of a transaction. However, this often comes with trade-offs in availability and partition tolerance. [Explore Consistency Models](../consistency-models/README.md).

-   **Coordination:** The successful execution of a distributed transaction heavily relies on robust coordination mechanisms to manage the state and actions of all participating nodes, especially during commit or rollback phases. [Understand Coordination Concepts](../coordination/README.md).

-   **Fault Tolerance:** Designing fault-tolerant distributed transactions is a significant challenge, as failures in any participant or network can jeopardize the atomicity and consistency of the entire operation. [Learn about Fault Tolerance](../fault-tolerance/README.md).

-   **Distributed Consensus:** While not always a direct application, the principles of distributed consensus are often at play in the commit phases of protocols like Two-Phase Commit, where all participants must agree on a final decision. [Understand Distributed Consensus](../distributed-consensus/README.md).

-   **Microservices Architecture (System Mode):** In modern microservices, traditional distributed transactions are often replaced by patterns like Saga, which prioritize availability and use eventual consistency, reflecting a different approach to system design. [Discover System Modes](../system-mode/README.md).
## Comparison

## Trade-offs
