# 🧩 Message Broker

## Overview

Message brokers are middleware systems that enable reliable, asynchronous communication between distributed components.

They are part of the data infrastructure layer, just like databases and caches, and play a critical role in:

- Decoupling services  
- Handling spikes in workload  
- Guaranteeing message delivery  
- Enabling event-driven architectures  

Common implementations include:
- Redis Streams (lightweight, in-memory)
- RabbitMQ (open-source, queue-based)
- Apache Kafka (high-throughput streaming)
- AWS SQS + SNS (managed queue + pub/sub)
- Azure Service Bus (enterprise-grade broker)

## Index
- [Message Broker vs Message Queue](./message-broker-vs-message-queue.md)
- [Redis](./Redis/README.md)
- [RabbitMQ](./RabbitMQ/README.md)

