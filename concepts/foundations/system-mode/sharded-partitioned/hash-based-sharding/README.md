# Hash-Based Sharding

## Overview

Hash-based sharding is a sharding strategy where data is distributed across shards by applying a hash function to the shard key. The output of the hash function determines which shard a particular piece of data will reside on. This method aims to achieve an even distribution of data across all available shards.

## How It Works

1.  **Shard Key:** A specific attribute of the data (e.g., user ID, product ID) is chosen as the shard key.
2.  **Hash Function:** A deterministic hash function is applied to the shard key. This function takes the shard key as input and produces a numerical hash value.
3.  **Modulo Operation (Commonly):** The hash value is then typically subjected to a modulo operation with the total number of available shards. The result of this operation (e.g., `hash_value % number_of_shards`) directly indicates the target shard.
4.  **Data Placement:** The data record is then stored on the shard identified by the hash function's output.
5.  **Query Routing:** When a client requests data, the same hash function is applied to the provided shard key to determine the correct shard to query. The request is then routed to that specific shard.

## Characteristics

### Pros

*   **Even Data Distribution:** Hash functions are designed to distribute inputs uniformly, which generally leads to a more even distribution of data across shards, reducing the likelihood of hot spots.
*   **Simple Routing:** Routing requests is straightforward and efficient, as it only requires applying the hash function to the shard key to determine the target shard. No external lookup service is needed.
*   **Reduced Hot Spots:** By evenly distributing data, hash-based sharding helps prevent individual shards from becoming overloaded with data or traffic.

### Cons

*   **Inefficient Range Queries:** Queries that involve a range of shard keys (e.g., "find all users with IDs between 1000 and 2000") become very inefficient. Since related keys are unlikely to be on the same shard, such queries often require querying all shards and then aggregating the results.
*   **Difficulty in Rebalancing:** Adding or removing shards (scaling up or down) is challenging. Changing the number of shards typically means changing the modulo divisor, which would alter the shard assignment for almost all existing data. This often necessitates a costly and complex data re-hashing and migration process.
*   **Fixed Number of Shards:** Often works best with a fixed or slowly changing number of shards due to the rebalancing difficulties.

## Use Cases

*   Applications where data access is primarily based on exact key lookups (e.g., retrieving a user profile by user ID).
*   Systems that require high write throughput and can tolerate less efficient range queries.
*   Scenarios where an even distribution of data is critical to avoid hot spots.

## Examples

*   **Key-Value Stores:** Many distributed key-value stores use consistent hashing or similar hash-based methods to distribute data.
*   **User Profile Services:** Storing user profiles where access is typically by a unique user ID.
*   **Caching Systems:** Distributing cached items across multiple cache servers.

## Related Concepts

-   **Sharded/Partitioned System Mode:** Hash-based sharding is a specific strategy for partitioning data across multiple nodes, forming a core component of sharded distributed systems, particularly when even data distribution is paramount. [Explore Sharded/Partitioned Systems](../README.md).

-   **Range-Based Sharding:** In contrast to hash-based sharding, range-based sharding partitions data based on contiguous value ranges, which is efficient for range queries but can lead to uneven data distribution. [Compare with Range-Based Sharding](../range-based-sharding/README.md).

-   **Directory-Based Sharding:** Another sharding strategy that uses a lookup table to map shard keys to physical shards, offering flexibility in data placement and rebalancing, but introducing the overhead of managing the directory service. [Explore Directory-Based Sharding](../directory-based-sharding/README.md).

-   **Horizontal Scaling:** Hash-based sharding is a fundamental technique for achieving horizontal scalability in databases and data stores, allowing systems to handle larger datasets and higher loads by adding more machines, especially for key-value lookups. [Learn about Horizontal Scaling](../../../scaling/horizontal/README.md).

-   **Data Replication:** Sharding is often combined with data replication within each shard to provide fault tolerance and high availability, ensuring that data remains accessible even if a shard fails. [Understand Data Replication](../../../data-replication/README.md).
