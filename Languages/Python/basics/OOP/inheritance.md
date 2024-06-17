# Inheritance
Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class). It promotes code reuse and establishes a relationship between classes.

## Define class
```
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
```

## Create object
```
dog = Dog("Buddy")
```

## Access attributes/methods
```
print(dog.speak())
```