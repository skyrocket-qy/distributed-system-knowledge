# Active-Active Cluster

## Core

This section describes the Active-Active Cluster configuration for fault tolerance, where multiple nodes are simultaneously active and capable of handling requests, providing high availability and improved performance.

## Comparison

| Feature | Description |
|---|---|
| **Availability** | High, all nodes are active. |
| **Performance** | Improved, workload distributed across nodes. |
| **Complexity** | High, requires robust conflict resolution and synchronization. |
| **Cost** | Higher, more resources are actively used. |

## Which service use it?



-   **Load-Balanced Web Servers:** Multiple web servers running concurrently behind a load balancer, all actively serving user requests. If one server fails, the load balancer redirects traffic to the remaining active servers.

-   **Stateless Microservices:** Microservices designed to be stateless can easily be deployed in an active-active configuration, as any instance can handle any request without needing to maintain session-specific data locally.

-   **Distributed Caching Systems:** Caching solutions like Redis Cluster or Memcached can operate in an active-active manner, distributing cached data across multiple nodes, all of which are available for reads and writes.

-   **Multi-Master Databases:** Databases configured for multi-master replication (e.g., some NoSQL databases, PostgreSQL BDR) allow multiple nodes to accept writes simultaneously, forming an active-active setup for data modification.

-   **Global Traffic Management (GTM) for Geo-Redundancy:** Systems that direct user traffic to the closest or healthiest active data center, where each data center is an active cluster.

## Related Concepts

-   **Fault Tolerance:** Active-active clusters are a robust fault tolerance strategy, ensuring high availability and continuous operation by distributing the workload across multiple active nodes, so that the failure of one does not halt the service. [Explore other Fault Tolerance strategies](../README.md).

-   **Active-Passive Failover:** In contrast, active-passive failover relies on a single active node with a standby passive node, which takes over only upon failure, typically offering simpler management but with potential downtime during failover. [Compare with Active-Passive Failover](../active-passive-failover/README.md).

-   **Multi-Leader Data Replication:** Active-active clusters often leverage multi-leader (or multi-master) data replication, allowing writes to occur on multiple nodes simultaneously, which then synchronize their state, introducing challenges in conflict resolution. [Understand Multi-Leader Replication](../../data-replication/multi-leader/README.md).

-   **Horizontal Scaling:** Active-active configurations inherently provide horizontal scaling benefits, as adding more active nodes directly increases the system's capacity to handle more requests and process more data. [Learn about Horizontal Scaling](../../scaling/horizontal/README.md).

-   **Conflict Resolution:** A critical challenge in active-active clusters, especially those allowing writes to multiple nodes, is managing and resolving conflicts that arise from concurrent updates to the same data. [Explore Conflict Resolution](../../conflict-resolution/README.md).

-   **Service Discovery:** Load balancers and service discovery mechanisms are essential for distributing incoming requests efficiently across all active nodes in the cluster and for dynamically routing traffic away from failed instances. [Understand Service Discovery](../../service-discovery/README.md).
