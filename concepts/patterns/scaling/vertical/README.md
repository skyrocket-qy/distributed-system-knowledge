# Vertical Scaling

## Core

This section explains Vertical Scaling (scaling up), a method of increasing capacity by adding more resources (CPU, RAM, storage) to an existing machine in a distributed system.

## Comparison

| Feature | Description |
|---|---|
| **Approach** | Add more resources to a single machine. |
| **Scalability** | Limited by hardware maximums. |
| **Cost** | Can be expensive for high-end hardware. |
| **Complexity** | Relatively simple, no distributed coordination needed. |

## Which service use it?



-   **Traditional Monolithic Applications:** Many legacy applications that were not designed for distributed environments often rely on vertical scaling by running on increasingly powerful single servers.

-   **Single-Instance Relational Databases:** Databases like Oracle, SQL Server, or even a standalone PostgreSQL/MySQL instance are often vertically scaled by upgrading the server's CPU, RAM, and storage to handle more load.

-   **Specialized High-Performance Computing (HPC) Tasks:** Certain computational workloads that are difficult to parallelize across multiple machines might benefit most from running on a single, extremely powerful server with a large amount of memory and many CPU cores.

-   **In-Memory Databases:** Databases designed to operate primarily in RAM (e.g., SAP HANA) often require significant vertical scaling to accommodate large datasets.

## Related Concepts

-   **Scaling:** Vertical scaling is one of the two primary approaches to increasing a system's capacity, focusing on enhancing the resources of a single machine rather than distributing the workload across multiple nodes. [Explore other Scaling methods](../README.md).

-   **Horizontal Scaling:** In direct contrast, horizontal scaling (scaling out) involves adding more machines to a system to distribute the workload, offering potentially unlimited scalability but introducing greater distributed system complexity. [Compare with Horizontal Scaling](../horizontal/README.md).

-   **Fault Tolerance:** Vertical scaling can introduce a single point of failure; if the single, powerful machine goes down, the entire service becomes unavailable, highlighting the need for robust fault tolerance strategies. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **System Modes:** Vertical scaling is often associated with traditional monolithic application architectures, where a single application instance runs on a powerful server, contrasting with distributed system modes like microservices or sharded databases. [Discover System Modes](../../system-mode/README.md).
