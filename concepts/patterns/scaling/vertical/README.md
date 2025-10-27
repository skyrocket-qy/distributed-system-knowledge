# Vertical Scaling



This section explains Vertical Scaling (scaling up), a method of increasing capacity by adding more resources (CPU, RAM, storage) to an existing machine in a distributed system.

## Characteristics

- **Simplicity**: Vertical scaling is simple to implement and manage.
- **Limited Scalability**: The scalability of a single machine is limited by its hardware capacity.
- **Single Point of Failure**: The single machine is a single point of failure.
- **High Cost**: High-end hardware can be expensive.
- **No Distributed Coordination**: Vertical scaling does not require any distributed coordination.

## Comparison

| Feature | Description |
|---|---|
| **Approach** | Add more resources to a single machine. |
| **Scalability** | Limited by hardware maximums. |
| **Cost** | Can be expensive for high-end hardware. |
| **Complexity** | Relatively simple, no distributed coordination needed. |

## Trade-offs

- **Simplicity vs. Scalability**: Vertical scaling is simple, but it has limited scalability.
- **Cost vs. Performance**: High-end hardware can be expensive, but it can provide high performance.

## Which service use it?



-   **Traditional Monolithic Applications:** Many legacy applications that were not designed for distributed environments often rely on vertical scaling by running on increasingly powerful single servers.

-   **Single-Instance Relational Databases:** Databases like Oracle, SQL Server, or even a standalone PostgreSQL/MySQL instance are often vertically scaled by upgrading the server's CPU, RAM, and storage to handle more load.

-   **Specialized High-Performance Computing (HPC) Tasks:** Certain computational workloads that are difficult to parallelize across multiple machines might benefit most from running on a single, extremely powerful server with a large amount of memory and many CPU cores.

-   **In-Memory Databases:** Databases designed to operate primarily in RAM (e.g., SAP HANA) often require significant vertical scaling to accommodate large datasets.
