# Eventual Consistency

## Core

This section describes the eventual consistency model, where the system guarantees that if no new updates are made to a given data item, eventually all accesses to that item will return the last updated value.

## Pros & Cons

### Pros
-   **High Availability:** Systems can remain operational and accept writes even if some nodes are down or partitioned. This is crucial for applications that require continuous uptime.
-   **Scalability:** It allows for horizontal scaling by distributing data across many nodes, as there's no need for all nodes to agree on the state of data before a write operation can complete. This makes it suitable for large-scale, high-traffic applications.
-   **Low Latency:** Write operations can complete quickly because they don't need to wait for all replicas to acknowledge the write. This improves response times for users.
-   **Partition Tolerance:** Eventual consistency inherently handles network partitions better than strongly consistent systems. When a partition occurs, each side of the partition can continue to operate independently.

### Cons
-   **Data Inconsistency (Temporary):** For a period after a write, different users or services might see different values for the same data item. This can be confusing and lead to unexpected behavior if not handled carefully.
-   **Complexity in Application Logic:** Developers need to design their applications to handle potential inconsistencies. This often involves implementing conflict resolution strategies and understanding the implications of reading stale data.
-   **Difficulty in Reasoning about State:** It can be challenging to reason about the exact state of the system at any given moment, as data propagates asynchronously.
-   **Not Suitable for All Use Cases:** Eventual consistency is not appropriate for applications that require immediate and strong consistency guarantees, such as financial transactions where every read must reflect the absolute latest state.

## Which service use it?

-   **Domain Name System (DNS):** DNS is a classic example where updates to records propagate across the internet over time, leading to eventual consistency.
-   **Amazon S3 (Simple Storage Service):** S3 provides eventual consistency for most operations, meaning that a read immediately after a write might not reflect the latest version.
-   **NoSQL Databases (e.g., Apache Cassandra, Amazon DynamoDB):** Many NoSQL databases prioritize availability and partition tolerance over strong consistency, offering eventual consistency as their primary model.
-   **Social Media Feeds:** Updates to user feeds (e.g., Facebook, Twitter) are eventually consistent, meaning a new post might not appear immediately for all followers.
-   **E-commerce Shopping Carts:** While critical operations like checkout are strongly consistent, the display of items in a shopping cart might be eventually consistent to improve performance.

