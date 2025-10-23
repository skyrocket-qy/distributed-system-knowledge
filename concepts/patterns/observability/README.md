# Observability

## Core

**Observability** in distributed systems refers to the ability to infer the internal states of a system by examining its external outputs. In complex, dynamic, and often ephemeral distributed environments, it's impossible to predict every failure mode or performance bottleneck. Therefore, having robust observability practices is crucial for understanding how a system is behaving, diagnosing issues, and ensuring its reliability and performance.

Observability is typically achieved through the collection and analysis of three main types of telemetry data: **logs**, **metrics**, and **traces**.

### Key Challenges

-   **Volume of Data:** Distributed systems generate vast amounts of logs, metrics, and traces, requiring scalable storage and processing solutions.
-   **Correlation:** Connecting disparate pieces of information (e.g., a log entry to a specific trace span, or a metric spike to a particular service) across multiple services and components.
-   **Context Switching:** The difficulty of understanding the flow of requests across numerous services, often written in different languages and running on different infrastructures.
-   **Alerting Fatigue:** Designing effective alerts that are actionable and minimize false positives.
-   **Tooling Complexity:** Managing and integrating various observability tools can be challenging.

## Characteristics

- **Logs**: Detailed, timestamped records of events.
- **Metrics**: Aggregated, numerical data about the system's performance.
- **Traces**: End-to-end view of a request's journey through the system.
- **Alerting**: Proactive notification of potential issues.
- **Dashboards**: Visual representation of the system's health and performance.

## Comparison

| Telemetry Type | Granularity | Storage Cost | Query Complexity | Primary Use |
|---|---|---|---|---|
| **Logs** | High (event-level detail) | High | High (text search, parsing) | Debugging, forensic analysis, detailed event context |
| **Metrics** | Low (aggregated data points) | Low | Low (numerical queries, aggregations) | Monitoring system health, alerting, trend analysis, dashboards |
| **Traces** | Medium (request-level flow) | Medium | Medium (graph traversal, span filtering) | Performance optimization, root cause analysis, understanding service dependencies |

## Trade-offs

- **Cost vs. Visibility**: Collecting and storing observability data can be expensive, but it provides valuable visibility into the system.
- **Overhead vs. Insight**: Instrumenting applications to generate telemetry data can introduce performance overhead, but it provides deep insights into the system's behavior.
- **Signal vs. Noise**: It can be challenging to filter out the noise and identify the meaningful signals in the vast amount of observability data.

## Pillars of Observability

| Pillar | Description | Purpose | Examples |
|---|---|---|---|
| **Logs** | Timestamped, immutable records of discrete events that happened within a service. | Provide detailed context about specific events, errors, or state changes. | Application logs, server logs, error messages |
| **Metrics** | Aggregatable numerical measurements that represent the state of a system over time. | Quantify system behavior, track trends, identify performance issues, and trigger alerts. | CPU utilization, memory usage, request rates, error rates, latency |
| **[Distributed Tracing](./distributed-tracing)** | Representations of the end-to-end journey of a single request or transaction as it propagates through multiple services. | Visualize the flow of requests, identify bottlenecks, and understand dependencies between services. | OpenTelemetry traces, Zipkin, Jaeger |

## Operational Aspects

Beyond collecting telemetry, effective observability involves actively using this data for operational insights:

-   **Alerting:** Defining rules and thresholds on metrics, logs, or traces to proactively notify operators about potential issues or deviations from normal behavior. Effective alerting minimizes "alert fatigue" by being actionable and relevant.
-   **Dashboards & Visualization:** Creating visual representations of key metrics, logs, and traces to provide a holistic view of system health, performance, and behavior. Dashboards help in quickly identifying trends, anomalies, and the root cause of problems.

## Which service use it?

-   **Logs:** Every distributed service generates logs. Centralized logging systems (e.g., ELK Stack, Splunk, Datadog Logs) are used to aggregate, search, and analyze logs from across the system.
-   **Metrics:** Monitoring platforms (e.g., Prometheus, Grafana, New Relic, Datadog Metrics) collect and visualize metrics to provide dashboards and alerts on system health and performance.
-   **Traces:** Distributed tracing tools (e.g., Jaeger, Zipkin, Lightstep, Datadog APM) are used in microservices architectures to understand request flows and pinpoint latency issues.
