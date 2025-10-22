# Security

## Core

Security in distributed systems is a multifaceted discipline aimed at protecting the system from unauthorized access, use, disclosure, alteration, or destruction. It involves implementing a combination of preventative and detective controls to ensure the confidentiality, integrity, and availability of the system and its data.

Key security concepts include:

*   **Authentication:** Verifying the identity of a user, process, or device.
*   **Authorization:** Granting or denying access to resources based on the authenticated identity.
*   **Encryption:** Encoding data to prevent unauthorized access.
*   **Auditing:** Logging and monitoring security-related events.

## Characteristics

-   **Confidentiality:** Ensuring that data is accessible only to authorized users.
-   **Integrity:** Maintaining the accuracy and completeness of data.
-   **Availability:** Ensuring that the system is accessible and usable when needed.

## Comparison

| Security Mechanism | Description                                                              | Use Case                                     |
| ------------------ | ------------------------------------------------------------------------ | -------------------------------------------- |
| **TLS/SSL**        | Encrypts data in transit between two nodes.                              | Securing communication between services.     |
| **OAuth 2.0**      | An authorization framework for delegated access.                         | Third-party application access to user data. |
| **JWT**            | A compact, self-contained way for securely transmitting information as a JSON object. | API authentication and authorization.      |

## Trade-offs

*   **Security vs. Performance:** Implementing strong security measures can sometimes introduce latency and overhead, impacting system performance.
*   **Security vs. Usability:** Overly complex security measures can make the system difficult to use, leading to user frustration and potential workarounds that compromise security.
*   **Cost:** Implementing and maintaining a robust security infrastructure can be expensive.

