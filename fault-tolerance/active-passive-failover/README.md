# Active-Passive Failover

## Core

This section describes Active-Passive Failover, a fault-tolerance strategy where a standby (passive) system takes over operations from a primary (active) system upon failure.

## Comparison

| Feature | Description |
|---|---|
| **Availability** | High, but with a brief downtime during failover. |
| **Complexity** | Relatively simple to implement. |
| **Cost** | Lower than active-active, as passive resources are idle. |
| **Performance** | No performance gain, as only one node is active. |

## Which service use it?



-   **Traditional Database High Availability:** Many relational databases (e.g., PostgreSQL, MySQL, SQL Server) are often deployed with an active-passive setup, where a primary database handles all operations and a standby replica takes over in case of primary failure.

-   **Application Servers:** Critical application instances can be configured with an active-passive failover, where a passive server is ready to take over the workload if the active one goes down.

-   **Network Devices:** Firewalls, routers, and load balancers often use active-passive configurations to ensure network connectivity and service availability.

-   **Virtual Machine Clusters:** Virtualization platforms (e.g., VMware vSphere, Microsoft Hyper-V) use active-passive failover to automatically restart virtual machines on healthy hosts if a host fails.

-   **Message Brokers:** Some message queue systems can be configured in an active-passive mode to ensure message durability and availability.
