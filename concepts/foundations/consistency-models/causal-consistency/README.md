# Causal Consistency

## Core

Causal consistency means that if one event directly influences another, everyone who sees both events will see them in the correct order. If events aren't related, their order might vary. It's a middle ground: stronger than eventual consistency (where order can be completely mixed up) but not as strict as strong consistency (where everything is always in perfect order everywhere).

## Pros & Cons

### Pros
- **Improved Performance and Availability:** Causal consistency allows for higher availability and lower latency compared to strong consistency models, as it doesn't require global synchronization for all operations.
- **Stronger Guarantees than Eventual Consistency:** It provides a more intuitive and predictable behavior than eventual consistency by preserving the order of causally related events, which is crucial for many applications.
- **Suitable for Collaborative Applications:** Ideal for systems where the order of operations based on user interactions is important, such as collaborative editing or social media feeds.

### Cons
- **More Complex to Implement:** Implementing causal consistency can be more complex than eventual consistency due to the need to track causal dependencies (e.g., using vector clocks or similar mechanisms).
- **Weaker than Strong Consistency:** It does not guarantee that all replicas will see all operations in the exact same order, only causally related ones. This means that some non-causally related operations might still appear in different orders on different replicas.
- **Overhead of Metadata:** Maintaining causal relationships often requires additional metadata (like version vectors) to be propagated with updates, which can add overhead in terms of storage and network bandwidth.

## Which service use it?

-   **Collaborative Editing Systems:** In applications like Google Docs, causal consistency ensures that if user A types something, and user B then replies to it, all users will see A's typing before B's reply, even if updates arrive out of order due to network delays.
-   **Distributed Social Networks:** When a user posts a comment on another user's post, causal consistency ensures that all users see the original post before the comment, regardless of which server they are reading from.
-   **Some Distributed Databases:** Certain NoSQL databases or specialized distributed data stores might offer causal consistency as a consistency option, providing stronger guarantees than eventual consistency without the full overhead of strong consistency.
-   **Message Queues with Causal Ordering:** Advanced message queuing systems might implement causal ordering to ensure that messages that are causally related are processed in the correct sequence.

