# Abstraction
Abstraction means hiding the complex implementation details and showing only the essential features of the object. It reduces programming complexity and effort.

## Define class
```
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
```

## Create objects
```
dog = Dog()
cat = Cat()
```

## Access objects attributes and methods
```
print(dog.sound()) # Bark
print(cat.sound()) # Meow
```