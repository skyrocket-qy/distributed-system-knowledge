# Distributed Systems Concepts

## Introduction

A distributed system is a collection of independent computers that appears to its users as a single coherent system. These systems are designed to solve problems that are too large or complex for a single machine, offering advantages such as enhanced scalability, reliability, and fault tolerance. However, they also introduce significant challenges related to communication, consistency, coordination, and fault management due to the inherent complexities of networked environments.

This directory aims to document various concepts, modes, and mechanisms related to distributed systems.

## Topics

- [Communication](./communication/README.md)
- [Conflict Resolution](./conflict-resolution/README.md)
- [Consensus](./coordination/consensus/README.md)
- [Consistency Models](./consistency-models/README.md)
- [Coordination](./coordination/README.md)
- [Data Replication](./data-replication/README.md)
- [Fault Tolerance](./fault-tolerance/README.md)
- [Messaging](./messaging/README.md)
- [Scaling](./scaling/README.md)
- [System Modes](./system-mode/README.md)
- [Topology](./topology/README.md)

## Common service with their pattern

## Which service use it?

-   **Cloud Computing Platforms (e.g., AWS, Azure, GCP):** These platforms are massive distributed systems that provide infrastructure, platforms, and software as services.
-   **Large-Scale Web Applications (e.g., Google Search, Facebook, Netflix):** These services handle billions of requests and petabytes of data by distributing their workload across thousands of servers.
-   **Distributed Databases (e.g., Apache Cassandra, MongoDB, Google Spanner):** Databases designed to store and manage data across multiple nodes for scalability, availability, and fault tolerance.
-   **Big Data Processing Frameworks (e.g., Apache Hadoop, Apache Spark):** Systems that process and analyze vast datasets by distributing computation across clusters of machines.
-   **Content Delivery Networks (CDNs):** Networks of geographically distributed servers that deliver web content to users based on their location, improving performance and availability.
-   **Financial Trading Systems:** High-frequency trading platforms and banking systems rely on on distributed architectures for low-latency processing, high throughput, and strong consistency.

## Further Reading

-   [What is a distributed system?](https://www.atlassian.com/microservices/microservices-architecture/distributed-architecture)
-   [Distributed Systems: An Introduction](https://www.confluent.io/learn/distributed-systems/)
-   [What Are Distributed Systems?](https://www.splunk.com/en_us/blog/learn/distributed-systems.html)
