# Range-Based Sharding

## Overview

Range-based sharding is a sharding strategy where data is partitioned based on a contiguous range of values of the shard key. Each shard is responsible for storing data whose shard key falls within a predefined range. This method is intuitive and often aligns well with how data is naturally queried.

## How It Works

1.  **Shard Key:** A specific attribute of the data (e.g., timestamp, geographical location, alphabetical range of names) is chosen as the shard key.
2.  **Range Definition:** The entire range of possible shard key values is divided into smaller, non-overlapping ranges. Each range is then assigned to a specific shard.
3.  **Data Placement:** When a new data record arrives, its shard key is evaluated to determine which predefined range it falls into, and the record is then stored on the corresponding shard.
4.  **Query Routing:** When a client requests data, the shard key in the query is used to identify the specific shard(s) that hold the relevant data. The request is then routed to the appropriate shard(s).

## Characteristics

### Pros

*   **Efficient Range Queries:** Queries that involve a range of shard keys (e.g., "find all orders placed last month," "find all users with last names starting with 'S'") are highly efficient. Such queries can often be directed to a single shard or a small subset of shards, avoiding the need to query all shards.
*   **Simplicity:** The partitioning logic is often straightforward and easy to understand, as it directly maps ranges of values to shards.
*   **Data Locality:** Related data (data with similar shard key values) tends to be co-located on the same shard, which can improve performance for certain types of queries.

### Cons

*   **Uneven Data Distribution (Hot Spots):** If the data distribution is not uniform across the chosen ranges, some shards can become significantly larger or experience much higher traffic than others. This leads to "hot spots" and performance bottlenecks.
*   **Manual Rebalancing:** Rebalancing data when a shard becomes too full or when the data distribution changes significantly often requires manual intervention or complex re-sharding operations. Adding new shards in the middle of existing ranges can be particularly challenging.
*   **Shard Key Choice is Critical:** The choice of the shard key and the definition of the ranges are crucial. A poor choice can lead to severe performance issues and operational overhead.

## Use Cases

*   Time-series data, where data is often queried by time ranges (e.g., logs, sensor data).
*   Geographical data, where data can be partitioned by location ranges.
*   Applications where range queries are frequent and critical for performance.
*   Systems where data growth patterns are predictable, allowing for well-defined ranges.

## Examples

*   **Database Partitioning:** Many relational databases support range partitioning for tables.
*   **Log Management Systems:** Storing logs by date ranges.
*   **E-commerce Platforms:** Sharding orders or products by creation date or product ID ranges.

## Related Concepts

-   **Sharded/Partitioned System Mode:** Range-based sharding is a specific strategy for partitioning data across multiple nodes, forming a core component of sharded distributed systems. [Explore Sharded/Partitioned Systems](../README.md).

-   **Hash-Based Sharding:** In contrast to range-based sharding, hash-based sharding distributes data more evenly by using a hash function on the shard key, but it can make range queries less efficient. [Compare with Hash-Based Sharding](../hash-based-sharding/README.md).

-   **Directory-Based Sharding:** Another sharding strategy that uses a lookup table to map shard keys to physical shards, offering flexibility but introducing the overhead of managing the directory service. [Explore Directory-Based Sharding](../directory-based-sharding/README.md).

-   **Horizontal Scaling:** Range-based sharding is a fundamental technique for achieving horizontal scalability in databases and data stores, allowing systems to handle larger datasets and higher loads by adding more machines. [Learn about Horizontal Scaling](../../../scaling/horizontal/README.md).

-   **Data Replication:** Sharding is often combined with data replication within each shard to provide fault tolerance and high availability, ensuring that data remains accessible even if a shard fails. [Understand Data Replication](../../../data-replication/README.md).

## Core

## Comparison

## Trade-offs
