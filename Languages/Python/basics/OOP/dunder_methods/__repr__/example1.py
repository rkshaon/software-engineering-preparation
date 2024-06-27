class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


# Creating an instance of Person
person = Person("Rezaul", 27)
print(repr(person))  # Output: Person(name='Rezaul', age=27)
