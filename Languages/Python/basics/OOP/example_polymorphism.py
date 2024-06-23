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
    

animals = [Bird("Tweety"), Fish("Goldy")]

for animal in animals:
    print(animal.speak())