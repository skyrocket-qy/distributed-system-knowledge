# Chaos Engineering

## Core

**Chaos Engineering** is the discipline of experimenting on a distributed system in order to build confidence in that system's capability to withstand turbulent conditions in production. Instead of waiting for failures to occur, Chaos Engineering proactively injects controlled failures into a system to identify weaknesses and improve its resilience. It's about learning from failure before it impacts customers.

### Principles of Chaos Engineering

-   **Hypothesize about steady-state behavior:** Define a measurable output that indicates normal operation.
-   **Vary real-world events:** Introduce events that reflect actual failures (e.g., server crashes, network latency, resource exhaustion).
-   **Run experiments in production:** The most accurate way to understand system behavior under stress is to test where the system operates.
-   **Automate experiments:** Automate the execution and analysis of chaos experiments to run them continuously.
-   **Minimize blast radius:** Design experiments to limit the impact of failures to a small subset of users or services.

### Key Challenges

-   **Complexity of Distributed Systems:** Understanding the potential impact of injecting failures in a highly interconnected system.
-   **Safety:** Ensuring that experiments do not cause irreversible damage or prolonged outages.
-   **Measurement and Observability:** Having robust monitoring and tracing in place to accurately observe the system's response to injected failures.
-   **Buy-in:** Gaining organizational support for intentionally breaking things in production.

## Common Chaos Experiments

-   **Server Shutdowns:** Randomly terminating instances to test resilience to node failures.
-   **Network Latency/Partitioning:** Introducing delays or blocking communication between services to simulate network issues.
-   **Resource Exhaustion:** Injecting CPU, memory, or disk pressure to test how services handle resource contention.
-   **Dependency Failures:** Simulating the failure of a critical downstream service or database.
-   **Time Skew:** Introducing clock drift between nodes to test time-sensitive operations.

## Which service use it?

-   **Netflix (Chaos Monkey):** Pioneered Chaos Engineering with tools like Chaos Monkey, which randomly terminates instances in their production environment.
-   **Amazon:** Uses similar practices to ensure the resilience of AWS services.
-   **Google:** Employs fault injection to test the robustness of its large-scale distributed systems.
-   **Financial Institutions:** To ensure the resilience of critical trading and banking systems.

## Related Concepts

-   **Fault Tolerance:** Chaos Engineering is a proactive approach to validating and improving the fault tolerance of distributed systems. [Understand Fault Tolerance](../README.md).
-   **Observability:** Robust observability (metrics, logs, traces) is essential for conducting chaos experiments and understanding their impact. [Explore Observability ../../observability/README.md].
-   **Resilience Engineering:** Chaos Engineering is a key practice within the broader field of resilience engineering, focusing on building and maintaining resilient systems. [Related to Fault Tolerance](../README.md).
-   **System Modes:** Different system architectures (e.g., microservices, serverless) present unique challenges and opportunities for applying chaos engineering principles. [Discover System Modes ../../system-mode/README.md].

## Comparison

## Trade-offs
