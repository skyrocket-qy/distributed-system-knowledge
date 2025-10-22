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
