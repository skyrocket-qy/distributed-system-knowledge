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
