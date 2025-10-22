# Databases in Distributed Systems

## Core

In a distributed system, a database is a critical component responsible for storing, managing, and retrieving data. Unlike traditional monolithic databases, a distributed database stores data across multiple physical locations, which can be in different data centers or geographic regions. The primary goal is to achieve high availability, fault tolerance, and scalability by distributing the data and workload.

Key challenges in distributed databases revolve around maintaining data consistency, ensuring availability during failures, and tolerating network partitions, as described by the CAP Theorem.

## Characteristics

Distributed databases are defined by several key characteristics:

*   **Data Distribution:** Data is spread across multiple machines or nodes to improve performance and reliability.
*   **Replication:** The system maintains copies (replicas) of the data on different nodes. If one node fails, the data can be served from another, ensuring high availability and fault tolerance.
*   **Partitioning (Sharding):** The database is split into smaller, more manageable parts called shards, and each shard is stored on a separate node. This allows the system to scale horizontally by adding more nodes.
*   **Concurrency Control:** The system must manage simultaneous access to data from multiple users or services without compromising data integrity.
*   **Fault Tolerance:** The system is designed to continue operating without data loss even if some nodes fail.

## Comparison

The most common comparison in the database world is between SQL and NoSQL databases, each suited for different use cases in distributed systems.

*   **SQL (Relational) Databases:**
    *   **Structure:** Organize data in tables with a predefined schema. They enforce data integrity through constraints.
    *   **Transactions:** Provide ACID (Atomicity, Consistency, Isolation, Durability) guarantees, which are ideal for applications requiring strong consistency (e.g., financial systems).
    *   **Scaling:** Traditionally scale vertically (scaling up by adding more power to an existing server). Horizontal scaling (sharding) is possible but often complex to implement and manage.
    *   **Examples:** PostgreSQL, MySQL, Microsoft SQL Server.

*   **NoSQL (Non-Relational) Databases:**
    *   **Structure:** Do not require a predefined schema, allowing for flexible data models. They are categorized as document, key-value, column-family, and graph stores.
    *   **Transactions:** Typically favor the BASE (Basically Available, Soft State, Eventually Consistent) model, prioritizing availability and scalability over strict consistency.
    *   **Scaling:** Designed to scale horizontally (scaling out by adding more servers), which is ideal for large-scale applications with growing data needs.
    *   **Examples:** MongoDB (Document), Redis (Key-Value), Cassandra (Column-Family), Neo4j (Graph).

## Trade-offs

Choosing a database and its architecture involves significant trade-offs:

*   **SQL vs. NoSQL:** The primary trade-off is often **Consistency vs. Availability and Flexibility**. SQL databases provide strong consistency, which is crucial for transactional integrity. NoSQL databases provide higher availability and a more flexible data model, which is better for applications with unstructured data and high traffic loads.

*   **Replication Strategies:**
    *   **Single-Leader Replication:** All writes go to a single leader node, which then propagates them to follower nodes. **Trade-off:** Simplifies write consistency but the leader can become a bottleneck and a single point of failure.
    *   **Multi-Leader Replication:** Multiple nodes can accept writes. This is useful for multi-datacenter deployments. **Trade-off:** Write conflicts can occur between different leaders and must be resolved.
    *   **Leaderless Replication:** All replicas can accept writes. This offers high availability and low latency. **Trade-off:** Can lead to stale reads and requires read repair mechanisms to achieve consistency.

*   **Sharding (Partitioning) Strategies:**
    *   **Ranged Partitioning:** Data is sharded based on a range of values. **Trade-off:** Simple to implement but can lead to "hotspots" if certain ranges are accessed more frequently.
    *   **Hashed Partitioning:** Data is sharded based on the hash of a key. **Trade-off:** Distributes data more evenly but makes range queries (e.g., fetching all users with names starting with 'A') inefficient.
