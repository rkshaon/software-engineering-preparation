# `__repr__(self)`
Provides an official string representation of the object, useful for debugging.

The `__repr__(self)` method in Python is a special method used to provide an unambiguous string representation of an object. This representation is mainly intended for developers to understand the object’s state and should ideally be a string that can be used to recreate the object.

## Key Points
- `Purpose`: Provide an unambiguous and developer-friendly string representation of an object.
- `Return Value`: Must return a string.
- `Difference from __str__()`: `__repr__()` aims at being clear and precise for debugging and logging, whereas `__str__()` focuses on being readable and user-friendly.

### Example
```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


# Creating an instance of Person
person = Person("Rezaul", 27)
print(repr(person))  # Output: Person(name='Rezaul', age=27)
```
[Example 1](./example1.py)

The **Person** class implements the `__repr__()` method to return a string that includes the class name and its attributes in a format that could be used to recreate the object.

`repr(person)` calls the `__repr__()` method and outputs the detailed string representation.

## Usage with Built-in Functions
The `__repr__()` method is automatically used by several built-in functions and operations:
- The built-in `repr()` function.
- When an object is inspected in the interactive interpreter.
- For debugging and logging purposes.

### Example with `__str__()` for Comparison
```
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

# Usage
vector = Vector(3, 4)
print(vector)  # Calls __str__: Output: Vector(3, 4)
print(repr(vector))  # Calls __repr__: Output: Vector(x=3, y=4)
```
[Example 2](./example2.py)

`__str__()` provides a concise and user-friendly representation.

`__repr__()` provides a detailed and unambiguous representation, suitable for debugging.

## Best Practices
- `Precision and Clarity`: Ensure the string returned by `__repr__()` is precise and clear, aiding in debugging and logging.
- `Recreatable`: Aim to make the string representation returned by `__repr__()` capable of recreating the object if passed to `eval()`, although this is not a strict requirement.

The `__repr__()` method is essential for providing clear and informative representations of objects, especially useful for developers during debugging and logging.

