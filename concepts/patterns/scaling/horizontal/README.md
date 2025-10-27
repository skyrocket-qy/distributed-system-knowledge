# Horizontal Scaling



This section explains Horizontal Scaling (scaling out), a method of increasing capacity by adding more machines to a distributed system.

## Characteristics

- **High Scalability**: Horizontal scaling provides high scalability, as new machines can be added to the system to increase capacity.
- **Cost-effective**: It can be a cost-effective way to scale, as it allows for the use of commodity hardware.
- **High Availability**: Horizontal scaling can improve the availability of a system by providing redundancy.
- **Complexity**: Horizontal scaling can be complex to manage, as it requires distributed coordination and data partitioning.
- **Distributed Coordination**: Horizontal scaling requires a mechanism to distribute the load across multiple machines.

## Comparison

| Feature | Description |
|---|---|
| **Approach** | Add more machines/nodes. |
| **Scalability** | High, theoretically unlimited. |
| **Cost** | Can be cost-effective using commodity hardware. |
| **Complexity** | Higher, requires distributed coordination and data partitioning. |

## Trade-offs

- **Scalability vs. Complexity**: Horizontal scaling provides high scalability, but it can also be complex to manage.
- **Cost vs. Performance**: Horizontal scaling can be cost-effective, but it can also introduce performance overhead due to the need for distributed coordination.

## Which service use it?



-   **Most Modern Web Applications:** Large-scale websites and online services (e.g., social media, e-commerce) distribute user traffic across many web servers and application servers.

-   **Microservices Architectures:** Microservices are inherently designed for horizontal scaling, allowing individual services to be scaled independently based on demand.

-   **Distributed Databases (NoSQL and Sharded SQL):** Databases like Apache Cassandra, MongoDB, Elasticsearch, and sharded relational databases achieve massive scale by distributing data and query processing across clusters of commodity servers.

-   **Big Data Processing Frameworks (e.g., Apache Hadoop, Apache Spark):** These frameworks process and analyze vast datasets by distributing computation across hundreds or thousands of nodes in a cluster.

-   **Cloud-Native Applications:** Applications built for cloud environments are typically designed to be horizontally scalable, leveraging auto-scaling groups and container orchestration platforms (e.g., Kubernetes) to dynamically adjust resources.
