# Sequential Consistency

## Core

Sequential consistency is a strong consistency model that ensures that the result of any execution is the same as if all operations by all processes were executed in some sequential order, and the operations of each individual process appear in this sequence in the order specified by its program. In simpler terms, it means that all processes see all operations in the same global order, even if the actual physical order of execution differs. Unlike linearizability, sequential consistency does not guarantee real-time ordering; an operation that physically completed before another might still appear to happen after it in the global sequential order.

## Characteristics

- **Total Order**: All operations are seen in the same order by all processes.
- **Program Order**: Operations from a single process are seen in the order they were issued.
- **Stronger than Causal Consistency**: Sequential consistency provides a global total order, which inherently preserves causal order.
- **Weaker than Linearizability**: Sequential consistency does not guarantee real-time ordering, meaning that an operation that physically completed before another might still appear to happen after it in the global sequential order.
- **High Latency**: Sequential consistency can introduce high latency due to the need for global ordering.

## Comparison

| Feature | Description |
|---|---|
| **Ordering** | Total order of all operations, preserving program order. |
| **Strength** | Strong, but weaker than Linearizability. |
| **Performance** | High latency due to strict ordering and coordination. |
| **Implementation Complexity** | Complex to implement and scale in distributed systems. |

## Trade-offs

### Pros

*   **Easier to Reason About:** Developers can reason about the system as if there were a single, centralized memory, simplifying concurrent programming.
*   **Strong Guarantees:** Provides strong guarantees about the order and visibility of operations, making it easier to write correct distributed applications.

### Cons

*   **Performance Overhead:** Achieving sequential consistency often involves significant coordination overhead, leading to higher latency and lower throughput compared to weaker consistency models.
*   **Reduced Availability:** The strict ordering requirements can reduce the availability of the system, as operations might need to wait for acknowledgments from multiple nodes.
*   **Complexity of Implementation:** Implementing sequential consistency in a distributed system is complex and can be challenging to scale.

## Use Cases

*   **Distributed Shared Memory Systems:** Where multiple processors access a common memory space.
*   **Critical Sections:** In distributed systems where certain operations must be executed atomically and in a strict order.
*   **Debugging and Testing:** Provides a strong baseline for understanding and verifying the behavior of distributed algorithms.

## Examples

*   **Transactional Databases:** While not always strictly sequential, many transactional databases aim for strong consistency models that are close to sequential consistency for critical operations.
*   **Distributed Consensus Algorithms:** Algorithms like Paxos or Raft, which are used to achieve agreement among distributed processes, often provide guarantees that can be considered sequentially consistent for the agreed-upon values.


