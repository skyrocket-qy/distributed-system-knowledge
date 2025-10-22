# Active-Passive Failover

## Core

This section describes Active-Passive Failover, a fault-tolerance strategy where a standby (passive) system takes over operations from a primary (active) system upon failure.

## Characteristics

- **High Availability**: Active-passive failover provides high availability by ensuring that a standby system is available to take over in case of a failure.
- **Fault Tolerance**: The system is resilient to the failure of the active node.
- **Redundancy**: The passive node is a redundant copy of the active node.
- **Consistency**: Data is replicated from the active node to the passive node to ensure consistency.
- **Failover**: The process of switching from the active node to the passive node is called failover.

## Comparison

| Feature | Description |
|---|---|
| **Availability** | High, but with a brief downtime during failover. |
| **Complexity** | Relatively simple to implement. |
| **Cost** | Lower than active-active, as passive resources are idle. |
| **Performance** | No performance gain, as only one node is active. |

## Trade-offs

| Advantages | Disadvantages |
|---|---|
| **High Availability**: Active-passive failover provides high availability. | **Downtime**: There is a brief downtime during failover. |
| **Simple**: Active-passive failover is relatively simple to implement. | **Cost**: The passive node is idle and does not contribute to the performance of the system. |
| **Consistent**: Data is replicated from the active node to the passive node to ensure consistency. | **Data Loss**: Data loss can occur if the active node fails before the data is replicated to the passive node. |

## Which service use it?



-   **Traditional Database High Availability:** Many relational databases (e.g., PostgreSQL, MySQL, SQL Server) are often deployed with an active-passive setup, where a primary database handles all operations and a standby replica takes over in case of primary failure.

-   **Application Servers:** Critical application instances can be configured with an active-passive failover, where a passive server is ready to take over the workload if the active one goes down.

-   **Network Devices:** Firewalls, routers, and load balancers often use active-passive configurations to ensure network connectivity and service availability.

-   **Virtual Machine Clusters:** Virtualization platforms (e.g., VMware vSphere, Microsoft Hyper-V) use active-passive failover to automatically restart virtual machines on healthy hosts if a host fails.

-   **Message Brokers:** Some message queue systems can be configured in an active-passive mode to ensure message durability and availability.

## Related Concepts

-   **Fault Tolerance:** Active-passive failover is a widely used fault tolerance strategy designed to ensure high availability by providing a standby system ready to take over operations upon primary failure. [Explore other Fault Tolerance strategies](../README.md).

-   **Active-Active Cluster:** In contrast, active-active clusters distribute the workload across multiple active nodes simultaneously, offering better resource utilization and potentially faster recovery, but with increased complexity. [Compare with Active-Active Clusters](../active-active-cluster/README.md).

-   **Data Replication:** Data replication is crucial for active-passive setups, as changes from the active node must be continuously synchronized to the passive node to ensure data consistency and minimize data loss during a failover. [Understand Data Replication](../../data-replication/README.md).

-   **Leader-Follower (Master-Slave) System Mode:** Active-passive failover is a common implementation pattern for leader-follower (or master-slave) system modes, where the passive node acts as a follower ready to be promoted to leader. [Discover Leader-Follower Systems](../../system-mode/master-slave/README.md).

-   **Service Discovery:** After a failover event, service discovery mechanisms are essential to update clients and other services about the new active node's location, ensuring traffic is correctly routed to the operational instance. [Understand Service Discovery](../../service-discovery/README.md).
