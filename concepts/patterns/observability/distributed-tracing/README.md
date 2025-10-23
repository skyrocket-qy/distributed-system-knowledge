# Distributed Tracing

## Core

**Distributed Tracing** is a technique used to monitor and observe requests as they flow through a distributed system. In a microservices architecture or any complex distributed environment, a single user request might traverse multiple services, databases, and queues. Distributed tracing provides an end-to-end view of this request's journey, allowing developers and operators to understand the performance bottlenecks, identify failures, and debug issues across service boundaries.

Each request is assigned a unique trace ID, and as it moves through different services, each operation (called a "span") is recorded with details like its duration, service name, operation name, and parent span ID. These spans are then linked together to form a complete trace, visualizing the entire request flow.

### Key Challenges

-   **Instrumentation:** All services involved in a trace must be instrumented to emit tracing data. This can be complex, especially in polyglot environments.
-   **Overhead:** Collecting and transmitting tracing data can introduce some performance overhead, which needs to be managed.
-   **Storage and Analysis:** Tracing data can be voluminous, requiring scalable storage and powerful analysis tools to make sense of it.
-   **Sampling:** Due to the volume of data, often only a sample of requests is traced, which means not all issues might be captured.

## Characteristics

- **End-to-end Visibility**: Distributed tracing provides an end-to-end view of a request's journey through a distributed system.
- **Latency Analysis**: It helps in identifying performance bottlenecks and latency issues.
- **Root Cause Analysis**: It facilitates root cause analysis of errors and failures.
- **Service Dependency Analysis**: It helps in understanding the dependencies between services.
- **Request Profiling**: It provides a detailed profile of a request, including the time spent in each service.

## Comparison

| Tool | Open Source | Standard |
|---|---|---|
| **OpenTelemetry** | Yes | Yes |
| **Jaeger** | Yes | No |
| **Zipkin** | Yes | No |

## Trade-offs

- **Overhead vs. Visibility**: Collecting and transmitting tracing data can introduce performance overhead, but it provides valuable visibility into the system.
- **Sampling vs. Completeness**: Sampling a subset of requests can reduce the overhead, but it may not capture all the issues.
- **Instrumentation vs. Adoption**: Instrumenting all services can be a complex and time-consuming task, which can be a barrier to adoption.

## Components of a Distributed Tracing System

-   **Trace:** Represents the entire journey of a single request through the distributed system.
-   **Span:** A single operation within a trace. Spans have a name, start time, end time, and can have attributes (key-value pairs) and events (logs).
-   **Parent-Child Relationship:** Spans are organized hierarchically, with child spans representing operations initiated by a parent span.
-   **Trace Context:** Information (like trace ID and span ID) that is propagated across service calls to link spans together.

## Popular Tools and Standards

-   **OpenTelemetry:** A vendor-neutral open standard and set of tools for instrumenting, generating, collecting, and exporting telemetry data (traces, metrics, and logs).
-   **Jaeger:** An open-source distributed tracing system inspired by Dapper and OpenZipkin.
-   **Zipkin:** A distributed tracing system that helps gather timing data needed to troubleshoot latency problems in microservice architectures.
-   **Google Cloud Trace, AWS X-Ray, Azure Monitor Application Insights:** Cloud-native distributed tracing services.

## Which service use it?

-   **Microservices Architectures:** Essential for understanding the interactions and performance of numerous small, interconnected services.
-   **Serverless Applications:** To trace requests across various serverless functions and managed services.
-   **Complex Web Applications:** To diagnose latency issues and errors in multi-tiered web applications.
-   **API Gateways:** Often the starting point for traces, propagating trace context to downstream services.
