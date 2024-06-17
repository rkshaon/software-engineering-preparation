# Define class
class Dog:
    # class attributes
    species = 'Canis familaries'

    # Initializer / Instance attributes
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # Instance methods
    def description(self) -> None:
        return f"{self.name} is {self.age} years old."

    def speak(self, sound):
        return f"{self.name} says {sound}"



# Create objects
dog1 = Dog("Buddy", 9)
dog2 = Dog("Lucy", 3)

# Accessing attributes and methods
print(dog1.description())
print(dog2.speak("Woof"))
