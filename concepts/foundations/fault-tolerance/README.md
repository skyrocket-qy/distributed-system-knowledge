# Fault Tolerance

## Core

**Fault tolerance** is a critical property of distributed systems that enables them to continue operating correctly even in the presence of failures (or "faults"). In a distributed system, where many independent components are communicating over an unreliable network, failures are not the exception—they are the norm. Therefore, designing systems that can withstand and recover from these failures is essential for building reliable and highly available services.

### Types of Faults

Faults in a distributed system can be broadly categorized into three types:

1.  **Node Failures:** A process or server crashes. This can be a "fail-stop" failure, where the node simply stops working, or a "Byzantine" failure, where the node continues to operate but in an incorrect or malicious way.
2.  **Network Failures:** Messages between nodes can be lost, delayed, or delivered out of order. The network can also become partitioned, where two or more groups of nodes are unable to communicate with each other.
3.  **Storage Failures:** Data stored on disk can be corrupted or lost.

### Techniques for Fault Tolerance

There are a number of techniques that can be used to build fault-tolerant distributed systems. Some of the most common ones include:

-   **Redundancy:** Having multiple components that can perform the same function. This can be achieved through:
    -   **Replication:** Maintaining multiple copies of data on different nodes. If one node fails, the data is still available on other nodes.
    -   **Redundant Components:** Having spare servers or network links that can take over if a primary component fails.
-   **Failure Detection:** Mechanisms to detect when a component has failed. This is often done using heartbeating, where nodes periodically send "I'm alive" messages to each other.
-   **Checkpointing and Recovery:** Periodically saving the state of a process to stable storage. If the process fails, it can be restarted from the last checkpoint.
-   **Graceful Degradation:** Designing the system to continue operating at a reduced level of functionality when some components have failed, rather than failing completely.

The goal of fault tolerance is to mask failures from the end-user, providing the illusion of a continuously available and correct system. The specific techniques used will depend on the system's requirements for availability, consistency, and performance.

### Key Considerations

-   **Failure Domains:** Identifying independent components whose failure won't affect others.
-   **Recovery Time Objective (RTO):** The maximum acceptable downtime after a failure.
-   **Recovery Point Objective (RPO):** The maximum acceptable amount of data loss after a failure.
-   **Cost:** The financial implications of implementing and maintaining fault-tolerant solutions.
-   **Complexity:** The added complexity to the system design, development, and operation.
-   **Testing:** Thoroughly testing failure scenarios to ensure the fault-tolerance mechanisms work as expected.


## Comparison

| Technique | Recovery Time | Resource Overhead | Complexity | Use Case |
|---|---|---|---|---|
| **[Active-Passive Failover](./active-passive-failover)** | Fast | Low | Low | Stateful applications |
| **[Active-Active Cluster](./active-active-cluster)** | Instant | High | High | Stateless applications, load balancing |
| **[Checkpointing](./checkpoint)** | Medium | Medium | Medium | Long-running computations |
| **[Snapshot](./snapshot)** | Fast | High | Medium | Stateful applications, databases |
| **[Consensus-Based Recovery](./consensus-recovery)** | Slow | High | High | Distributed databases, state machine replication |
| **[Gossip-Based Recovery](./gossip-recovery)** | Slow | Low | Low | Peer-to-peer networks, cluster membership |
| **[Idempotency](./idempotency)** | Instant | Low | Medium | Message processing, payment systems |
| **[Chaos Engineering](./chaos-engineering)** | Proactive | Medium | High | Validating system resilience in production |

## Which service use it?



-   **Redundancy (Replication):** Distributed databases (e.g., Cassandra, MongoDB), distributed file systems (e.g., HDFS), and cloud storage services (e.g., Amazon S3) extensively use replication to ensure data availability and durability.

-   **Failure Detection:** Cluster management systems (e.g., Kubernetes, Apache Mesos), distributed coordination services (e.g., ZooKeeper, etcd), and load balancers use various mechanisms to detect unhealthy nodes or services.

-   **Checkpointing and Recovery:** Long-running batch processing jobs (e.g., in Apache Spark, Flink), scientific simulations, and stateful stream processing applications use checkpointing to recover from failures without restarting from scratch.

-   **Graceful Degradation:** Content delivery networks (CDNs), large-scale web services, and streaming platforms often implement graceful degradation to maintain some level of service even when parts of the system are under stress or experiencing failures.

-   **Active-Passive Failover:** Traditional high-availability setups for databases, application servers, and network devices.

-   **Active-Active Cluster:** Load-balanced web servers, stateless microservices, and distributed caching systems.

-   **Consensus-Based Recovery:** Distributed databases (e.g., CockroachDB), distributed transaction systems, and state machine replication systems.

-   **Gossip-Based Recovery:** Peer-to-peer networks, distributed hash tables (DHTs), and some cluster membership services.

## Related Concepts

-   **Data Replication:** A fundamental technique for achieving fault tolerance by maintaining multiple copies of data across different nodes, ensuring availability even if some nodes fail. [Explore Data Replication strategies](../data-replication/README.md).

-   **Distributed Consensus:** Algorithms like Paxos or Raft are crucial for fault-tolerant decision-making in distributed systems, enabling nodes to agree on a single value or state despite failures. [Understand Distributed Consensus](../distributed-consensus/README.md).

-   **Consistency Models:** The choice of consistency model (e.g., strong, eventual) is often influenced by fault tolerance requirements, as stronger consistency can sometimes be harder to maintain during network partitions or node failures. [Learn about Consistency Models](../consistency-models/README.md).

-   **System Modes:** Various system architectures and modes (e.g., active-passive, quorum-based) are designed with specific fault tolerance characteristics to handle different types of failures and recovery scenarios. [Discover System Modes](../system-mode/README.md).

-   **Coordination:** Fault tolerance mechanisms, especially failure detection, leader election, and recovery processes, heavily rely on effective coordination among distributed components. [Explore Coordination Concepts](../coordination/README.md).

-   **Idempotency:** A crucial property for operations in fault-tolerant systems, ensuring that repeated executions of an operation produce the same result, preventing unintended side effects during retries. [Understand Idempotency](./idempotency/README.md).

-   **Chaos Engineering:** A proactive approach to testing the resilience of distributed systems by intentionally injecting failures to uncover weaknesses. [Understand Chaos Engineering ./chaos-engineering/README.md].
