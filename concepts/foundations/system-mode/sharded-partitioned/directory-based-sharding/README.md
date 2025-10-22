# Directory-Based Sharding

## Overview

Directory-based sharding is a sharding strategy where a lookup table, often called a "directory" or "router," is maintained to map each shard key to the specific shard where its corresponding data resides. Instead of using a deterministic function (like a hash or range) to locate data, the system consults this directory to find the correct shard for any given piece of data.

## How It Works

1.  **Shard Key:** Each piece of data still requires a shard key, which is the identifier used to determine its location.
2.  **Directory Service:** A dedicated service or component acts as the directory. This service stores the mapping between shard keys (or ranges of keys) and the physical shards. This directory itself needs to be highly available and scalable.
3.  **Query Routing:** When a client application needs to read or write data, it first sends the request (including the shard key) to a routing layer.
4.  **Lookup:** The routing layer queries the directory service with the shard key.
5.  **Redirection:** The directory service returns the address or identifier of the shard that holds the data for that key.
6.  **Data Access:** The routing layer then forwards the client's request to the appropriate shard.

## Characteristics

### Pros

*   **Flexibility:** Offers the most flexibility in data distribution. Shards can be added, removed, or rebalanced without changing the sharding logic in the application. The directory can be updated to reflect these changes.
*   **Dynamic Rebalancing:** Easier to rebalance data across shards. When a shard becomes too full or a new shard is added, the directory mappings can be updated to redistribute data, potentially with minimal downtime.
*   **Handling Skew:** Can effectively handle data skew (hot spots) by remapping frequently accessed keys to less loaded shards.

### Cons

*   **Increased Complexity:** Introduces an additional layer of complexity due to the need to manage and maintain the directory service itself.
*   **Single Point of Failure (if not designed carefully):** The directory service can become a single point of failure or a performance bottleneck if not made highly available and scalable.
*   **Performance Overhead:** Every data access operation requires an additional lookup in the directory, which adds latency.
*   **Consistency Challenges:** Ensuring consistency between the directory and the actual data distribution across shards can be challenging, especially during rebalancing operations.

## Use Cases

*   Systems requiring highly flexible data placement and dynamic rebalancing.
*   Environments where data distribution patterns are unpredictable or change frequently.
*   Scenarios where fine-grained control over data placement is necessary.

## Examples

*   **Distributed File Systems:** Some distributed file systems use a directory-like service to map file blocks to storage nodes.
*   **Custom Sharding Implementations:** Applications that build their own sharding logic often employ a directory-based approach for maximum control.

## Related Concepts

-   **Sharded/Partitioned System Mode:** Directory-based sharding is a highly flexible strategy for partitioning data across multiple nodes, forming a core component of sharded distributed systems, especially when dynamic rebalancing is required. [Explore Sharded/Partitioned Systems](../README.md).

-   **Range-Based Sharding:** In contrast to directory-based sharding, range-based sharding partitions data based on contiguous value ranges, which is efficient for range queries but can lead to uneven data distribution and less flexible rebalancing. [Compare with Range-Based Sharding](../range-based-sharding/README.md).

-   **Hash-Based Sharding:** Hash-based sharding distributes data evenly using a hash function, but it makes rebalancing difficult and range queries inefficient, unlike the flexibility offered by a directory service. [Compare with Hash-Based Sharding](../hash-based-sharding/README.md).

-   **Horizontal Scaling:** Directory-based sharding is a powerful technique for achieving horizontal scalability in databases and data stores, allowing for dynamic adjustments to data distribution and shard allocation as the system grows. [Learn about Horizontal Scaling](../../../scaling/horizontal/README.md).

-   **Service Discovery:** The directory service in directory-based sharding functions similarly to a service registry, mapping logical data identifiers (shard keys) to physical locations (shards), akin to how service discovery maps service names to instances. [Understand Service Discovery](../../../service-discovery/README.md).

-   **Fault Tolerance:** The directory service itself is a critical component and must be designed with high availability and fault tolerance in mind to prevent it from becoming a single point of failure for the entire sharded system. [Understand Fault Tolerance](../../../fault-tolerance/README.md).

## Core

## Comparison

## Trade-offs
