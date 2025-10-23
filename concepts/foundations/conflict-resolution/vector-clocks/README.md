# Vector Clocks for Conflict Resolution

## Core

Vector clocks are a mechanism used in distributed systems to track the causality and ordering of events across multiple nodes or processes. They help in understanding the sequence of operations and maintaining consistency in systems without a global clock.

### How Vector Clocks Work

Each process or node in a distributed system maintains a vector of integers, where each element in the vector corresponds to a specific process. When a process performs an event (e.g., sends a message, performs a local computation), it increments its own entry in its vector clock.

When a process sends a message, it includes its current vector clock with the message. When a process receives a message, it updates its own vector clock by taking the element-wise maximum of its current vector clock and the received vector clock. It then increments its own entry in the vector clock.

### Comparing Vector Clocks

Vector clocks can be compared to determine the causal relationship between two events:

-   **Event A happened before Event B:** If all elements in A's vector clock are less than or equal to the corresponding elements in B's vector clock, and at least one element is strictly less.
-   **Event B happened before Event A:** If all elements in B's vector clock are less than or equal to the corresponding elements in A's vector clock, and at least one element is strictly less.
-   **Events A and B are concurrent:** If neither A happened before B nor B happened before A.

### Example

Consider three processes P1, P2, and P3. Initially, their vector clocks are [0,0,0].

1.  P1 performs a local event: VC(P1) = [1,0,0]
2.  P2 performs a local event: VC(P2) = [0,1,0]
3.  P1 sends a message to P2. The message carries VC(P1) = [1,0,0].
4.  P2 receives the message from P1. P2 updates its VC: max([0,1,0], [1,0,0]) = [1,1,0]. Then P2 performs a local event: VC(P2) = [1,2,0]
5.  P3 performs a local event: VC(P3) = [0,0,1]

By comparing these vector clocks, we can determine causal relationships. For example, the event at P1 ([1,0,0]) happened before the second event at P2 ([1,2,0]). The event at P3 ([0,0,1]) is concurrent with both events at P1 and P2.

## Pros & Cons

### Pros
-   **Accurate Causality Tracking:** Vector clocks excel at tracking the "happened-before" relationship between events, crucial for maintaining consistency and preventing conflicts.
-   **Conflict Detection and Resolution:** They provide a systematic way to detect concurrent updates or operations, vital for conflict resolution in distributed systems.
-   **No Central Coordinator Needed:** Enables decentralized event ordering, avoiding a single point of failure.
-   **Fault Tolerance:** Enhances fault tolerance by allowing the system to handle network partitions or node failures gracefully.
-   **Concurrency Detection:** Unlike Lamport timestamps, vector clocks can identify concurrent events, providing more complete information about the system's state.

### Cons
-   **Scalability Issues (Vector Size):** The size of a vector clock grows linearly with the number of nodes, leading to significant memory usage and communication overhead in large systems.
-   **Communication Overhead:** Every message must carry the full vector clock, adding extra bytes and potentially impacting bandwidth and latency.
-   **Implementation Complexity:** Correctly implementing vector clocks can be challenging, especially in dynamic systems with frequent node changes or network partitions.
-   **No Inherent Conflict Resolution Strategy:** While vector clocks detect conflicts, they do not inherently provide strategies to resolve them; this logic must be implemented separately.
-   **Operational Complexity:** Introduces operational complexity, requiring specialized monitoring and debugging to understand causal relationships.

## Which service use it?

-   **Distributed Databases (e.g., Riak):** Riak uses vector clocks to detect and manage concurrent updates, allowing applications to resolve conflicts when they read data.

-   **Distributed File Systems:** Some distributed file systems use vector clocks to track the causal history of file versions, helping to resolve conflicts when files are modified concurrently.

-   **Collaborative Editing Systems:** In systems where multiple users can edit a document simultaneously, vector clocks can help in merging changes by understanding the causal relationships between different edits.

-   **Version Control Systems:** While not always explicitly called vector clocks, the underlying principles of tracking divergent histories and merging them are similar to how vector clocks help manage concurrent updates.
