# Higher Order Function
A **higher-order function** is a function that either:
1. Takes one or more functions as arguments.
2. Returns a function as its result.

**Higher-order function**s allow functions to be treated like any other value, enabling more flexible, reusable, and modular code. This concept is foundational in functional programming and is used extensively in many programming languages, including Python.

## Key Characteristics
- **Accepts functions as arguments:** This allows for dynamic behavior and code reuse.
- **Returns functions:** This allows for the creation of customized functions on the fly, often used for decorators or function factories.

### Examples
#### Taking Function as Argument
```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

result = apply_function(square, 5)
print(result)           # Output: 25
```

Here, `apply_function` is a higher-order function because it takes another function (`square`) as an argument and applies it to the provided value.

#### Returning a Function
```python
def multiplier(factor):
    def multiply_by_factor(x):
        return x * factor
    return multiply_by_factor

double = multiplier(2)
triple = multiplier(3)

print(double(5))        # Output: 10
print(triple(5))        # Output: 15
```

Here, `multiplier` is a higher-order function that returns a new function, which multiplies by a specific factor. Functions like `double` and `triple` are created on the fly using this higher-order function.

## Common Types of Higher Order Functions
1. Map
2. Filter
3. Reduce
2. Decorators

### Map
Applies a given function to each item in an iterable (e.g., list) and returns a map object (an iterator).

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))        # Output: [1, 4, 9, 16, 25]
```

### Filter
