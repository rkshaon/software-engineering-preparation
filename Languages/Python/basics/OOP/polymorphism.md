# Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It provides a way to perform a single action in different forms.

## Define class
```
class Bird:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        return f"{self.name} chirps!"


class Fish:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        return f"{self.name} does not make a sound."
```

## Create objects
```
animals = [Bird("Tweety"), Fish("Goldy")]
```

## Access methods
```
for animal in animals:
    print(animal.speak())
```