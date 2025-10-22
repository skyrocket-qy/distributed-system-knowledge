# Causal Consistency

## Core

This section describes the causal consistency model, which is a weaker guarantee than strong consistency but stronger than eventual consistency. It ensures that operations that are causally related are seen by all processes in the same order.

## Comparison

| Feature | Description |
|---|---|
| **Ordering** | Preserves causal order of events. |
| **Strength** | Stronger than eventual, weaker than strong consistency. |
| **Complexity** | Requires tracking causal dependencies. |
| **Performance** | Better performance than strong consistency. |

## Which service use it?

-   **Collaborative Editing Systems:** In applications like Google Docs, causal consistency ensures that if user A types something, and user B then replies to it, all users will see A's typing before B's reply, even if updates arrive out of order due to network delays.
-   **Distributed Social Networks:** When a user posts a comment on another user's post, causal consistency ensures that all users see the original post before the comment, regardless of which server they are reading from.
-   **Some Distributed Databases:** Certain NoSQL databases or specialized distributed data stores might offer causal consistency as a consistency option, providing stronger guarantees than eventual consistency without the full overhead of strong consistency.
-   **Message Queues with Causal Ordering:** Advanced message queuing systems might implement causal ordering to ensure that messages that are causally related are processed in the correct sequence.

## Related Concepts

-   **Consistency Models:** Causal consistency is a specific consistency model that provides stronger guarantees than eventual consistency by preserving the causal order of operations, without enforcing a total global order. [Explore other Consistency Models](../README.md).

-   **Eventual Consistency:** While stronger than eventual consistency, causal consistency still allows for temporary inconsistencies among replicas, as long as causally related operations are observed in the correct order. [Compare with Eventual Consistency](../eventual-consistency/README.md).

-   **Strong Consistency:** In contrast to strong consistency, causal consistency does not guarantee that all reads will return the most recent write, but it ensures that causally dependent writes are seen in order. [Compare with Strong Consistency](../strong-consistency/README.md).

-   **Vector Clocks:** Vector clocks are the foundational mechanism used to implement causal consistency, allowing distributed systems to track and enforce the causal relationships between events across different nodes. [Learn more about Vector Clocks for Coordination](../../coordination/vector-clock/README.md).

-   **Conflict Resolution:** Causal consistency helps in understanding the causal history of updates, which is crucial for resolving conflicts that arise from concurrent operations in distributed systems. [Explore Conflict Resolution](../../conflict-resolution/README.md).

## Trade-offs
