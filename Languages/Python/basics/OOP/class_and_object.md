# Class and Object
A `class` is user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.

## Define Class
```
class Dog:
    species = 'Canis familaries'
    
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
    def description(self) -> None:
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}."
```

## Create objects
```
dog1 = Dog("Buddy", 9)
dog2 = Dog("Lucy", 3)
```

## Accessing attributes and methods
```
print(dog1.description()) # Output: Buddy is 9 years old.
print(dog2.speak("Woof")) # Output: Lucy says Woof.
```