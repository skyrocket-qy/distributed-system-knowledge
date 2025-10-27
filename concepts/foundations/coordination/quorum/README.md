# Quorum



This section explains the concept of Quorum in distributed systems, particularly its role in ensuring consistency and availability for coordination.

```mermaid
graph TD
    subgraph Replicas (N=5)
        R1
        R2
        R3
        R4
        R5
    end

    subgraph Write Quorum (W=3)
        W1(R1)
        W2(R2)
        W3(R3)
    end

    subgraph Read Quorum (R=3)
        R2_Read(R2)
        R3_Read(R3)
        R4_Read(R4)
    end

    style W1 fill:#f9f,stroke:#333,stroke-width:2px
    style W2 fill:#f9f,stroke:#333,stroke-width:2px
    style W3 fill:#f9f,stroke:#333,stroke-width:2px

    style R2_Read fill:#ccf,stroke:#333,stroke-width:2px
    style R3_Read fill:#ccf,stroke:#333,stroke-width:2px
    style R4_Read fill:#ccf,stroke:#333,stroke-width:2px

    Client -->|Write(v)| W1
    Client -->|Write(v)| W2
    Client -->|Write(v)| W3

    Client -->|Read()| R2_Read
    Client -->|Read()| R3_Read
    Client -->|Read()| R4_Read
```

## Characteristics

- **Consistency**: Quorum-based systems provide tunable consistency, allowing a trade-off between consistency and availability.
- **Availability**: Quorum-based systems can remain available even if some nodes fail.
- **Fault Tolerance**: Quorum-based systems are resilient to a certain number of node failures.
- **Latency**: The latency of an operation depends on the number of nodes in the quorum.
- **Scalability**: Quorum-based systems can be scaled by adding more nodes.

## Comparison

| Feature | Description |
|---|---|
| **Consistency** | Configurable, balancing consistency and availability. |
| **Availability** | Can maintain availability during some node failures. |
| **Fault Tolerance** | Tolerates failures up to a certain threshold. |
| **Complexity** | Adds complexity in configuration and management. |

## Trade-offs

| Advantages | Disadvantages |
|---|---|
| **Tunable Consistency**: Quorum-based systems provide tunable consistency. | **Complexity**: Quorum-based systems can be complex to configure and manage. |
| **Availability**: Quorum-based systems can remain available even if some nodes fail. | **Latency**: The latency of an operation depends on the number of nodes in the quorum. |
| **Fault Tolerance**: Quorum-based systems are resilient to a certain number of node failures. | **Scalability**: Quorum-based systems can be scaled by adding more nodes. |

## Which service use it?



-   **Distributed Storage Systems (e.g., Apache Cassandra, Amazon DynamoDB):** These systems allow users to configure read and write quorums to achieve desired consistency levels. For example, a write quorum of `W` means `W` replicas must acknowledge a write before it's considered successful.

-   **Consensus Algorithms (e.g., Paxos, Raft):** These algorithms fundamentally rely on a majority (quorum) of nodes to agree on a decision (e.g., leader election, log entry commitment) to ensure consistency and fault tolerance.

-   **Distributed Coordination Services (e.g., Apache ZooKeeper, etcd):** These services use quorum-based protocols to maintain a consistent and highly available shared state, which is crucial for distributed locks, leader election, and configuration management.

-   **Distributed File Systems:** Some distributed file systems use quorum-like mechanisms to ensure data integrity and availability, especially when dealing with metadata or critical control plane operations.

