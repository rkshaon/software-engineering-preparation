# Abstract Class in Python
An abstract class is a class that cannot be instantiated directly and is used to define common methods or attributes that must be implemented by its subclasses. Abstract classes serve as blueprints for other classes.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"
```

Here,
- `ABC` used as the base class.
- The `@abstractmethod` decorator used for methods that must be implemented by subclasses.

In this example, the `Animal` class is abstract, and its `sound()` method must be implemented by any subclass, like `Dog`.