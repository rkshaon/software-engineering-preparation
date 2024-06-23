class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Creating an instance of Person
person1 = Person("Rezaul", 27)
person1.greet()  # Output: Hello, my name is Rezaul and I am 27 years old.
