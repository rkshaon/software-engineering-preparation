class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


dog = Dog("Buddy")
print(dog.speak())