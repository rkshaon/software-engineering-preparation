# Factory Method
The **Factory Method Pattern** defines an interface for creating objects, but **lets subclasses decide which class to instantiate**.

**Think of it like**: _"You don’t new things directly — you ask a factory to build it for you."_

## ✅ Use Cases
- When the exact type of object isn’t known until runtime.

- To delegate object creation to subclasses.

- To follow the **Open/Closed Principle** (open for extension, closed for modification).

## 💡 Real-Life Analogy
Imagine a **logistics company**: You call their factory to get a transport.

The factory decides: 🚛 Truck for land, 🚢 Ship for sea.

## Example
```python
from abc import ABC, abstractmethod

# Product interface
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Concrete Products
class Truck(Transport):
    def deliver(self):
        return "Delivering by land in a truck."

class Ship(Transport):
    def deliver(self):
        return "Delivering by sea in a ship."

# Creator
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return transport.deliver()

# Concrete Creators
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Usage
delivery1 = RoadLogistics().plan_delivery()
delivery2 = SeaLogistics().plan_delivery()

print(delivery1)  # "Delivering by land in a truck."
print(delivery2)  # "Delivering by sea in a ship."
```



