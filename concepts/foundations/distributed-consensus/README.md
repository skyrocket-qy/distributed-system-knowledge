# Distributed Consensus

## Core

This section discusses consensus mechanisms specifically in the context of distributed coordination.

```mermaid
graph TD
    subgraph Nodes
        A[Node 1]
        B[Node 2]
        C[Node 3]
    end

    A -- Propose Value --> D(Consensus Protocol);
    B -- Propose Value --> D;
    C -- Propose Value --> D;
    D -- Reach Agreement --> E[Agreed Value];
    E --> A;
    E --> B;
    E --> C;
```

## Characteristics

- **Agreement**: All non-faulty processes agree on the same value.
- **Validity**: If all non-faulty processes propose the same value, then all non-faulty processes will decide on that value.
- **Termination**: All non-faulty processes eventually decide on a value.
- **Fault Tolerance**: The consensus algorithm is resilient to a certain number of process failures.
- **Asynchrony**: The consensus algorithm is designed to work in an asynchronous network.

## Comparison

| Algorithm | Understandability | Fault Tolerance | Performance | Use Case |
|---|---|---|---|---|
| **[Paxos](./paxos)** | Low | High | Medium | Critical systems, high-consistency requirements |
| **[Raft](./raft)** | High | High | Medium | Distributed key-value stores, coordination services |

## Trade-offs

- **Performance**: Consensus algorithms can have high latency due to the need for multiple rounds of communication.
- **Complexity**: Consensus algorithms can be complex to implement and understand.
- **Scalability**: The scalability of consensus algorithms is limited by the number of processes.

## Which service use it?



-   **Distributed Databases (e.g., Google Spanner, CockroachDB):** These databases use consensus algorithms (like Paxos or Raft) to ensure that all replicas agree on the state of the data, enabling strong consistency and fault tolerance.

-   **Distributed Coordination Services (e.g., Apache ZooKeeper, etcd):** These services are built on consensus protocols to provide a consistent and highly available shared state for distributed applications, used for leader election, configuration management, and service discovery.

-   **Leader Election:** In many distributed systems, a leader needs to be elected to coordinate tasks or handle writes. Consensus algorithms are used to reliably elect a single leader among a group of nodes.

-   **Distributed Transactions:** While complex, some distributed transaction protocols (e.g., Two-Phase Commit) aim to achieve consensus among participating nodes to either commit or abort a transaction atomically.

-   **State Machine Replication:** Systems that replicate a state machine across multiple nodes use consensus to ensure that all nodes process the same sequence of commands in the same order, maintaining a consistent state.

