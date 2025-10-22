# Horizontal Scaling

## Core

This section explains Horizontal Scaling (scaling out), a method of increasing capacity by adding more machines to a distributed system.

## Comparison

| Feature | Description |
|---|---|
| **Approach** | Add more machines/nodes. |
| **Scalability** | High, theoretically unlimited. |
| **Cost** | Can be cost-effective using commodity hardware. |
| **Complexity** | Higher, requires distributed coordination and data partitioning. |

## Which service use it?



-   **Most Modern Web Applications:** Large-scale websites and online services (e.g., social media, e-commerce) distribute user traffic across many web servers and application servers.

-   **Microservices Architectures:** Microservices are inherently designed for horizontal scaling, allowing individual services to be scaled independently based on demand.

-   **Distributed Databases (NoSQL and Sharded SQL):** Databases like Apache Cassandra, MongoDB, Elasticsearch, and sharded relational databases achieve massive scale by distributing data and query processing across clusters of commodity servers.

-   **Big Data Processing Frameworks (e.g., Apache Hadoop, Apache Spark):** These frameworks process and analyze vast datasets by distributing computation across hundreds or thousands of nodes in a cluster.

-   **Cloud-Native Applications:** Applications built for cloud environments are typically designed to be horizontally scalable, leveraging auto-scaling groups and container orchestration platforms (e.g., Kubernetes) to dynamically adjust resources.

## Related Concepts

-   **Sharded/Partitioned System Mode:** A common strategy for horizontally scaling databases and data stores by distributing data across multiple independent nodes. [Explore Sharded/Partitioned Systems](../../system-mode/sharded-partitioned/README.md).

-   **Vertical Scaling:** In contrast to horizontal scaling, vertical scaling (scaling up) involves increasing the resources (CPU, RAM) of a single machine. [Compare with Vertical Scaling](../vertical/README.md).

-   **Load Balancing:** Essential for horizontally scaled systems to distribute incoming network traffic across multiple servers, ensuring efficient resource utilization and high availability. [Related to Client-Server Communication](../../communication/client-server/README.md).

-   **Service Discovery:** In dynamic, horizontally scaled environments, service discovery mechanisms are crucial for services to find and communicate with each other without hardcoding locations. [Understand Service Discovery](../../service-discovery/README.md).

-   **Fault Tolerance:** Horizontal scaling inherently contributes to fault tolerance by providing redundancy; if one instance fails, others can continue to handle the workload. [Learn about Fault Tolerance](../../fault-tolerance/README.md).

## Trade-offs
