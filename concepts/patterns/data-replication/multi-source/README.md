# Multi-Source Replication

## Core

This section describes Multi-Source Replication, a data replication setup where a single replica receives data from multiple primary sources, often used for data aggregation or complex data flows.

## Comparison

| Feature | Description |
|---|---|
| **Data Aggregation** | Consolidates data from multiple sources. |
| **Complexity** | High, especially with conflict resolution and data transformation. |
| **Use Case** | Data warehousing, complex data integration. |
| **Consistency** | Varies, often eventual consistency. |

## Which service use it?



-   **Data Warehousing and ETL (Extract, Transform, Load):** Data warehouses often aggregate data from numerous operational databases and external sources. Multi-source replication can be used to feed data from these diverse sources into a central data warehouse.

-   **Data Aggregation Platforms:** Systems that collect and consolidate data from various independent systems or microservices into a unified view for analytics or reporting.

-   **Complex Data Integration Scenarios:** In large enterprises, where different departments or legacy systems maintain their own data stores, multi-source replication can be used to create a consolidated view for specific applications or business intelligence.

-   **Global Data Synchronization:** In some global deployments, a central data store might receive updates from regional data centers, each acting as a source.

## Related Concepts

-   **Data Replication:** Multi-source replication is a specialized data replication strategy focused on aggregating data from diverse origins into a single destination, often for analytical or integration purposes. [Explore other Data Replication strategies](../README.md).

-   **Multi-Leader Replication:** In contrast to multi-source replication, multi-leader replication involves multiple active primary nodes that can accept writes, with changes then synchronized among them, often leading to more complex conflict resolution. [Compare with Multi-Leader Replication](../multi-leader/README.md).

-   **Consistency Models:** The consistency achieved in multi-source replication can vary significantly, often leaning towards eventual consistency, especially when dealing with disparate sources and potential delays in data propagation. [Explore Consistency Models](../../consistency-models/README.md).

-   **Conflict Resolution:** Aggregating data from multiple independent sources can introduce conflicts when the same data is updated differently across sources, necessitating robust conflict resolution strategies during the integration process. [Understand Conflict Resolution](../../conflict-resolution/README.md).

-   **Messaging:** Event streaming platforms or message queues are frequently used in multi-source replication scenarios to reliably capture and transport data changes from various sources to the central replica for processing and aggregation. [Explore Messaging Systems](../../messaging/README.md).

## Trade-offs
