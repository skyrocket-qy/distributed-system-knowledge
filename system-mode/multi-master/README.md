# Multi-Master Mode

## Core

**Multi-master** (or active-active) replication is a system mode where multiple nodes in a distributed system can accept write operations. This is in contrast to a single-master (or master-slave) architecture, where only one node is designated to handle writes.

In a multi-master setup, each master node can process writes independently and then replicate its changes to the other master nodes. This model is often used to achieve high availability, distribute write traffic, and reduce write latency in geographically distributed systems.

## How It Works

When a write is made to any master node, that node updates its local data store and then propagates the change to all other master nodes in the system. This propagation often occurs via change logs or message queues, ensuring that all masters eventually receive the updates. Since writes can occur concurrently on different masters, conflicts can arise. For example, two clients might update the same piece of data on two different masters at the same time.

**[Conflict Resolution](../../conflict-resolution/README.md)** is a critical aspect of multi-master systems. Common strategies for handling conflicts include:
-   **[Last Write Wins (LWW)](../../conflict-resolution/last-write-wins/README.md):** The write with the later timestamp overwrites the earlier one. This is simple to implement but can lead to data loss.
-   **[Vector Clocks](../../conflict-resolution/vector-clocks/README.md):** A more sophisticated timestamping mechanism that can detect concurrent updates and flag them for resolution, allowing for application-level merging.
-   **[Conflict-free Replicated Data Types (CRDTs)](../../conflict-resolution/crdts/README.md):** Data structures that can be replicated across multiple servers, allowing concurrent updates without conflicts, and guaranteeing eventual consistency.
-   **Application-Specific Logic:** The application itself is responsible for resolving conflicts, often by merging the conflicting changes or prompting a user for a decision.

Replication between masters can be synchronous or asynchronous. Asynchronous replication is more common, as synchronous replication would introduce high latency for every write and negate some of the benefits of a multi-master setup.

## Pros & Cons

### Pros

-   **High Availability for Writes:** If one master node fails, other masters can continue to accept write requests, eliminating the single point of failure for writes.
-   **Low Write Latency:** Clients can connect to the nearest master, reducing network latency for write operations.
-   **Write Scalability:** The write load is distributed across multiple nodes, increasing the system's overall write throughput.

### Cons

-   **Conflict Resolution Complexity:** The need to handle and resolve write conflicts adds significant complexity to the system.
-   **[Eventual Consistency](../../consistency-models/eventual-consistency/README.md):** Due to replication lag and the asynchronous nature of updates, data is typically eventually consistent. This means that different nodes might have different versions of the data for a short period, and all replicas are guaranteed to converge to the same state only if no new updates are made for a sufficient period.
-   **Difficult to Reason About:** The possibility of concurrent writes and conflicts can make it harder to reason about the state of the data and the behavior of the system.

## Key Considerations

When designing a system with multi-master replication, several factors need careful consideration:

-   **Network Latency:** While multi-master reduces write latency for local clients, high network latency between master nodes can increase replication lag and the window for conflicts.
-   **Data Consistency Requirements:** Multi-master inherently leads to eventual consistency. Systems requiring strong consistency for all operations might find multi-master unsuitable without additional mechanisms (e.g., distributed transactions, which add complexity).
-   **Operational Overhead:** Managing multiple active masters, monitoring replication, and handling conflict resolution logic adds to operational complexity compared to single-master setups.
-   **Application Design:** Applications need to be designed to gracefully handle eventual consistency and potential conflicts. This might involve implementing custom conflict resolution logic or designing data models that minimize conflicts (e.g., using CRDTs).

## Which service use it?

-   **Distributed Databases (e.g., MySQL, PostgreSQL with BDR):** When configured for multi-master replication, these databases allow writes to occur on multiple nodes, which then synchronize with each other. This is often used for high availability and geographic distribution.
-   **Distributed Version Control Systems (e.g., Git):** In Git, every developer's local repository is a full copy of the codebase, acting as a master. Changes can be made and committed locally, and then pushed and pulled between repositories, effectively operating in a multi-master fashion.
-   **Some Distributed Key-Value Stores:** Certain key-value stores can be configured to allow writes to multiple nodes, handling conflicts through various resolution strategies.
