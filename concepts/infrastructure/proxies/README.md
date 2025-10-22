# Proxies

## Core

A **proxy** is a server that acts as an intermediary for requests from clients seeking resources from other servers. Proxies provide a gateway between users and the internet, and they can be used for a variety of purposes, including load balancing, security, and caching.

## Comparison

| Type | How it works | Use Case |
|---|---|---|
| **Forward Proxy** | Forwards requests from a private network to the internet. | Controlling access to the internet. |
| **Reverse Proxy** | Forwards requests from the internet to a private network. | Load balancing, caching, and SSL termination. |
| **Open Proxy** | A proxy server that is accessible to any internet user. | Anonymizing traffic. |

## Trade-offs

| Type | Advantages | Disadvantages |
|---|---|---|
| **Forward Proxy** | Security and control. | Can be a single point of failure. |
| **Reverse Proxy** | Scalability and flexibility. | Can be more complex to configure. |
| **Open Proxy** | Anonymity. | Can be abused for malicious purposes. |
