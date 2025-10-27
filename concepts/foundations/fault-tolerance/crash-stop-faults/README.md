# Crash-stop Faults



A crash-stop fault (also known as fail-stop) is a type of fault in distributed systems where a faulty process simply stops executing and sends no incorrect messages. It is a relatively simple and common type of fault, as it assumes that processes either work correctly or stop entirely without exhibiting malicious or arbitrary behavior.

## Characteristics

-   **Clean Failure:** A faulty node simply stops, without sending incorrect messages.
-   **Easy to Detect:** Failures are typically easy to detect through timeouts or heartbeat mechanisms.
-   **Simpler Recovery:** Recovery mechanisms are simpler compared to Byzantine faults.

