class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


# Creating an instance of Person
person = Person("Rezaul", 27)
print(person)  # Output: Rezaul, 27 years old

