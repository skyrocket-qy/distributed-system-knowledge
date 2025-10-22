# Strong Consistency

## Core

Strong consistency is the strictest consistency model, guaranteeing that all clients see the same, most up-to-date version of the data at all times. This means that any read operation will return the value of the most recent write, and all operations appear to be executed in a single, atomic order.

To achieve this, strong consistency models often rely on two more specific concepts:

-   **Linearizability:** This is the strongest form of consistency. It requires that all operations appear to have been executed atomically at some point between their invocation and their completion. This gives the illusion of a single, centralized system, making it easier to reason about the system's behavior.
-   **Sequential Consistency:** This is a slightly weaker model that still provides strong guarantees. It requires that all operations appear to be executed in some sequential order, and that the operations of any individual client appear in the same order as they were issued. However, the global order of operations from different clients is not guaranteed to be the same as the real-time order.

## Comparison

| Algorithm | Description | Fault Tolerance | Performance | Use Case |
|---|---|---|---|---|
| **Paxos** | A family of protocols for reaching consensus in a network of unreliable processors. | Byzantine faults | Moderate | Distributed databases, Chubby |
| **Raft** | A consensus algorithm that is designed to be easy to understand. | Crash-stop faults | High | etcd, CockroachDB |
| **ZAB** | (ZooKeeper Atomic Broadcast) A protocol for atomic broadcast and primary-backup replication. | Crash-stop faults | High | ZooKeeper |

## Trade-offs

### Advantages

-   **Simplicity:** Strong consistency makes it easier for developers to reason about the state of the system, as there is a single, authoritative view of the data.
-   **Correctness:** It eliminates the risk of stale reads and other anomalies that can occur with weaker consistency models, which is critical for applications like financial systems.

### Disadvantages

-   **High Latency:** Achieving strong consistency often requires synchronous communication between replicas, which can increase the latency of write operations.
-   **Lower Availability:** If a replica is unable to communicate with the others, it may not be able to serve read or write requests, reducing the overall availability of the system.
-   **Complexity:** Implementing strong consistency protocols can be complex, and they often require a quorum of nodes to be available to make progress.

## Which service use it?

-   **Traditional Relational Databases (e.g., PostgreSQL, MySQL with ACID transactions):** These systems typically provide strong consistency within a single instance or through synchronous replication.
-   **Financial Systems:** Banking applications, stock trading platforms, and payment gateways require strong consistency to ensure accurate transaction processing and prevent data anomalies.
-   **Distributed Databases with Consensus (e.g., Google Spanner, CockroachDB, etcd, ZooKeeper):** These systems use algorithms like Paxos or Raft to ensure that all replicas agree on the order of operations, providing strong consistency guarantees across distributed nodes.
-   **Critical Business Applications:** Any application where data integrity and immediate visibility of changes are paramount, such as inventory management or reservation systems.
