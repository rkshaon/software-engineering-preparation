# 📦 Message Queue

## 🧩 Overview

A **Message Queue (MQ)** is a communication mechanism that allows different components of a system to **exchange data asynchronously**.

It temporarily stores messages in a queue until the receiving service is ready to process them — ensuring **reliability**, **decoupling**, and **fault tolerance** in distributed architectures.

Message Queues are widely used in **microservices**, **event-driven systems**, and **background job processing**.

---

## ⚙️ How It Works

A Message Queue follows a simple flow:

1. **Producer** — sends (publishes) a message into the queue.  
2. **Broker** — stores the message until it’s processed.  
3. **Consumer** — retrieves (consumes) the message from the queue.  
4. **Acknowledgment (ACK)** — once processed successfully, the consumer acknowledges; the broker removes the message.  
5. **Retry / DLQ (optional)** — if a consumer fails to process the message, it can be retried or sent to a *dead-letter queue*.

```text
Producer  →  [ Message Queue ]  →  Consumer
                ↑    ↓
             Stored  ACK
