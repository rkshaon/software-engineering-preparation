# `__str__(self)`
Provides a human-readable string representation of the object.

The `__str__(self)` method in Python is a special method used to provide a human-readable string representation of an object. When you use the `print()` function or `str()` on an object, Python calls the `__str__()` method of that object. This method should return a string that is easy to read and suitable for end-users.

## Key Points
- `Purpose`: Provide a readable and user-friendly string representation of an object.
- `Return Value`: Must return a string.
- `Difference from __repr__()`: While `__str__()` is meant for readability, `__repr__()` is intended to provide an unambiguous representation of an object, ideally one that can be used to recreate the object.

### Example
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


# Creating an instance of Person
person = Person("Rezaul", 27)
print(person)  # Output: Rezaul, 27 years old
```

The **Person** class implements the `__str__()` method to return a formatted string with the person’s name and age.

When **print(person)** is called, the `__str__()` method is invoked, and the string "Rezaul, 27 years old" is printed.

## Usage with Built-in Functions
The `__str__()` method is automatically invoked by several built-in functions and operations:

- `print(object)`
- `str(object)`
- String formatting operations like `f"{object}"`

## Best Practices
- `Clarity and Readability`: Ensure the string returned by `__str__()` is clear and provides meaningful information about the object.
- `Avoid Overloading`: Keep the `__str__()` method focused on providing a readable string representation. Avoid adding complex logic.

### Example with `__repr__()`
```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Usage
vector = Vector(3, 4)
print(vector)  # Calls __str__: Output: Vector(3, 4)
vector  # Calls __repr__: Output: Vector(3, 4)
```
[Example 2](./example2.py)

Both `__str__()` and `__repr__()` methods return the same string for simplicity.

**print(vector)** calls `__str__()`, while simply evaluating vector in an interactive session calls `__repr__()`.

The `__str__()` method is crucial for making your custom objects more readable and user-friendly, especially when printed or converted to a string.