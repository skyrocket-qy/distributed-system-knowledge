# Master-Slave Mode

## Core

The **master-slave** system mode is a replication pattern where one node, the **master**, serves as the authoritative source for data, and one or more other nodes, the **slaves**, replicate the data from the master. It is a specific implementation of the leader-follower pattern.

The master node is responsible for processing all write operations. Slaves are read-only copies of the master and can be used to serve read traffic, thus scaling the system's read capacity.

## How It Works

1.  **Write Operations:** All data modification requests (writes, updates, deletes) are sent to the master node. The master applies these changes to its local data store.
2.  **Replication:** After a write is committed, the master records the change in its transaction log and sends it to all its slaves.
3.  **Read Operations:** Read requests can be handled by either the master or any of the slaves. Offloading reads to slaves allows the system to handle a higher volume of read traffic.
4.  **Failover:** If the master node fails, one of the slave nodes must be promoted to become the new master. This process can be manual or automated by a monitoring system.

Replication can be configured in two primary ways:
-   **Asynchronous Replication:** The master sends updates to the slaves and does not wait for an acknowledgment. This offers lower write latency but carries the risk of data loss if the master fails before the changes have been sent to the slaves.
-   **Synchronous Replication:** The master waits for at least one (or all) slaves to confirm they have received the update before acknowledging the write to the client. This guarantees consistency but increases write latency.

## Pros & Cons

### Pros

-   **Read Scalability:** The ability to add more slaves allows the system to handle a large number of concurrent read operations.
-   **High Availability for Reads:** If the master fails, slaves can continue to serve read traffic.
-   **Backup and Recovery:** Slaves can be used as hot backups of the master's data.

### Cons

-   **Single Point of Failure for Writes:** The master is the only node that can accept writes. If it fails, the system cannot process any write requests until a slave is promoted.
-   **Replication Lag:** In asynchronous mode, slaves can fall behind the master. Applications reading from a slave might see stale data.
-   **Failover Complexity:** The process of promoting a slave to a new master can be complex and may involve potential data loss if the slave was not fully synchronized.

## Which service use it?

-   **Relational Databases (e.g., MySQL, PostgreSQL, SQL Server):** This is a very common replication setup for traditional databases, where a primary database handles all writes and replicates data to one or more secondary (read-only) databases.
-   **Redis:** Redis can be configured in a master-replica (formerly master-slave) setup, where the master handles writes and replicas serve read requests.
-   **Some Message Brokers (e.g., RabbitMQ with mirrored queues):** While not a pure master-slave, some message queue systems use similar concepts for high availability, where a primary node handles writes and mirrors messages to other nodes.

## Related Concepts

-   **System Modes:** Master-slave (or leader-follower) is a fundamental system mode where a single master node handles all writes and replicates data to one or more slave nodes, which serve read requests. [Explore other System Modes](../README.md).

-   **Data Replication:** Master-slave is a primary pattern for data replication, ensuring that multiple copies of data exist across different nodes, with the master being the authoritative source for updates. [Understand Data Replication](../../data-replication/README.md).

-   **Fault Tolerance:** While master-slave setups provide high availability for reads, the master node represents a single point of failure for writes, necessitating robust fault tolerance mechanisms like failover to ensure continuous write availability. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Scaling:** Master-slave architectures primarily scale read operations by distributing read traffic across multiple slave nodes, allowing the system to handle a higher volume of read requests. [Learn about Scaling](../../scaling/README.md).

-   **Consistency Models:** The consistency guarantees in a master-slave setup depend on the replication mode; synchronous replication can provide strong consistency, while asynchronous replication typically leads to eventual consistency. [Explore Consistency Models](../../consistency-models/README.md).

-   **Active-Passive Failover:** Master-slave configurations often implement active-passive failover, where a passive slave node is promoted to become the new master if the active master fails, ensuring continuity of write operations. [Explore Active-Passive Failover](../../fault-tolerance/active-passive-failover/README.md).
