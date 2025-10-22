# Quorum-Based System Mode

## Core

A **quorum-based** system mode is a technique used in distributed systems to ensure data consistency and availability, even when some nodes are unavailable. A quorum is the minimum number of nodes that must participate in an operation (a read or a write) for it to be considered successful.

This approach is based on the idea that by requiring a majority of nodes to agree on an operation, the system can guarantee that the operation is durable and that reads will see the results of the most recent writes.

## How It Works

A quorum-based system is typically configured with three parameters:

-   **N:** The total number of nodes that store replicas of the data.
-   **W:** The **write quorum**, which is the number of nodes that must acknowledge a write before it is considered successful.
-   **R:** The **read quorum**, which is the number of nodes that must respond to a read request before the result is returned to the client.

To ensure strong consistency (i.e., that a read operation always sees the most recent write), the quorums must be configured to satisfy the following rule:

**R + W > N**

This formula guarantees that the set of nodes participating in a read operation (R) and the set of nodes participating in a write operation (W) always have at least one node in common. This overlapping node ensures that the read operation has access to the most recently written version of the data.

For example, in a system with N=5 nodes, you could set W=3 and R=3.
-   When a write occurs, it must be acknowledged by 3 out of 5 nodes.
-   When a read occurs, the system requests the data from 3 out of 5 nodes.
-   Since R+W (3+3=6) is greater than N (5), the read quorum is guaranteed to overlap with the write quorum by at least one node. The system can then determine the most recent value by comparing timestamps or version numbers and return that to the client.

By tuning R and W, system designers can trade off between read and write latency:
-   **Fast Reads (Low R, High W):** Setting R=1 and W=N results in very fast reads but slow, durable writes.
-   **Fast Writes (Low W, High R):** Setting W=1 and R=N results in fast writes but slow, consistent reads.

## Pros & Cons

### Pros

-   **Tunable Consistency:** Allows for a flexible tradeoff between consistency, availability, and latency by adjusting the R and W values.
-   **Fault Tolerance:** The system can tolerate the failure of (N - W) nodes for writes and (N - R) nodes for reads.
-   **Strong Consistency:** When R + W > N, the system can provide strong consistency guarantees.

### Cons

-   **Increased Latency:** Operations must wait for responses from multiple nodes, which can increase latency compared to single-node operations.
-   **Communication Overhead:** Requires coordination between multiple nodes for each read and write operation.
-   **Complexity:** The logic for handling quorum requests, versioning, and data repair (when nodes return with stale data) can be complex to implement correctly.

## Which service use it?

-   **Apache Cassandra:** Cassandra allows users to specify consistency levels (e.g., `ONE`, `QUORUM`, `ALL`) for read and write operations, which are directly based on quorum principles.
-   **Amazon DynamoDB:** While not explicitly exposing N, R, W, DynamoDB offers eventually consistent and strongly consistent reads, where strong consistency implicitly relies on a quorum-like agreement among replicas.
-   **Distributed File Systems (e.g., HDFS):** HDFS uses a configurable replication factor (e.g., 3) for data blocks. While not a strict R+W>N quorum for every operation, the concept of requiring a certain number of replicas to be available for reads and writes is similar.
-   **Consensus Algorithms (e.g., Paxos, Raft):** These algorithms fundamentally rely on quorums (a majority of nodes) to make decisions and ensure consistency in distributed state machines, such as for leader election and log replication.

## Related Concepts

-   **System Modes:** Quorum-based systems represent a specific system mode designed to manage consistency and availability trade-offs in distributed environments by requiring a minimum number of nodes for operations. [Explore other System Modes](../README.md).

-   **Quorum (Coordination):** The concept of a quorum is a fundamental coordination mechanism, ensuring that a sufficient number of nodes participate in an operation to guarantee its integrity and consistency across the distributed system. [Learn more about Quorum as a Coordination mechanism](../../coordination/quorum/README.md).

-   **Consistency Models:** Quorum-based systems offer tunable consistency, allowing designers to balance strong consistency with availability and performance by adjusting the read (R) and write (W) quorum sizes relative to the total number of replicas (N). [Explore Consistency Models](../../consistency-models/README.md).

-   **Fault Tolerance:** Quorum-based systems are inherently fault-tolerant, as they can continue to operate and maintain consistency even if a minority of nodes fail, provided the quorum threshold is still met. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Data Replication:** Quorum reads and writes are commonly used in replicated storage systems to ensure data integrity and availability across multiple copies of data, allowing for flexible consistency guarantees. [Understand Data Replication](../../data-replication/README.md).

-   **Distributed Consensus:** Quorum is a cornerstone of many distributed consensus algorithms (e.g., Paxos, Raft), where a majority of nodes must agree on a decision to ensure consistency and fault tolerance, directly influencing quorum-based system design. [Understand Distributed Consensus](../../distributed-consensus/README.md).
