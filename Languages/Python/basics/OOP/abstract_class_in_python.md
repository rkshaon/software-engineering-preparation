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
- Inherit class `ABC` used as the base class whichs stands for `Abstract Base Class`.
- The `@abstractmethod` decorator used to declare abstract method, which means methods that must be implemented by subclasses.

In this example, the `Animal` class is abstract, and its `sound()` method must be implemented by any subclass, like `Dog`.

## Need to Know about Abstract Classes
### Instantiation Restriction
You cannot instantiate an abstract class directly; trying to do so will raise a `TypeError`.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# This will raise a TypeError
# animal = Animal()  # Uncommenting this will result in an error
```

### Partially Implemented Classes
Abstract classes can have concrete methods in addition to abstract methods. Subclasses can inherit concrete methods, but they must implement all abstract methods.

```python
class Bird(Animal):
    def fly(self):
        return "Flying high!"
```

### Multiple Inheritance
Abstract classes can be used with multiple inheritance, allowing subclasses to inherit methods from more than one abstract base class.

```python
class FlyingCreature(ABC):
    @abstractmethod
    def fly(self):
        pass

class Bat(Animal, FlyingCreature):
    def sound(self):
        return "Screech"
    
    def fly(self):
        return "Flying like a bat"
```

### `@abstractmethod` decorator
You can also define abstract properties using the `@abstractmethod` decorator with `@property`.

```python
class Vehicle(ABC):
    @property
    @abstractmethod
    def max_speed(self):
        pass

class Car(Vehicle):
    @property
    def max_speed(self):
        return 120
```

## When to Use Abstract Classes
1. Enforcing Implementation: Ensure that all subclasses implement specific methods.
2. Providing a Template: Serve as a blueprint for other classes.
3. Managing Complex Systems: Structure large, multi-class systems with common behaviors.

## Real-World Use Cases
- Creating a base class for different types of vehicles (car, bike, airplane) where each must have specific methods like move().
- Designing a plugin system where every plugin must implement certain required functions.
