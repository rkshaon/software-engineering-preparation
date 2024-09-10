# Higher Order Function
A **higher-order function** is a function that either:
1. Takes one or more functions as arguments.
2. Returns a function as its result.

**Higher-order functions** allow functions to be treated like any other value, enabling more flexible, reusable, and modular code. This concept is foundational in functional programming and is used extensively in many programming languages, including Python.

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
4. Decorators

### map()
Applies a given function to each item in an iterable (e.g., list) and returns a map object (an iterator).

```python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))        # Output: [1, 4, 9, 16, 25]
```

### filter()
Applies a function to each item and returns an iterator with items that evaluate to `True`.

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))   # Output: [2, 4]
```

### reduce()
Reduces an iterable to a single value using a given function. It's part of the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)              # Output: 120
```

### Decorator
A **decorator** in Python is a higher-order function that allows you to modify or enhance the behavior of another function or method without changing its actual code. They are typically used for adding functionality, logging, authentication, caching, etc., around functions in a clean and reusable way.

```python
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output
# ======
# Before the function call
# Hello!
# After the function call
```

## Benefits
- **Code Reusability:** You can reuse the same logic on different data by passing different functions.
- **Abstraction:** They allow for more abstract code, reducing boilerplate and focusing on behavior instead of implementation details.
- **Modularity:** Higher-order functions encourage the separation of concerns by isolating different behaviors into their own functions.
- **Flexibility:** They enable dynamic behavior where the logic can be passed in as an argument or returned as a function.

## Real-World Examples
- **Event Handling in UI Development:** In many UI frameworks, functions are passed as callbacks for events like `onClick`. These functions are examples of higher-order functions because they accept other functions (handlers) to trigger when an event occurs.
- **Middleware in Web Development:** In frameworks like Flask or Django, middleware functions act as higher-order functions, intercepting HTTP requests and responses, modifying them before or after other functions.

## Functional Programming with Higher-Order Functions
In functional programming, higher-order functions are central to paradigms like,
- Currying
- Composition
- Event Handlers

### Currying
This is when a function is transformed into a sequence of functions, each taking a single argument.

```python
def curry(f):
    return lambda x: lambda y: f(x, y)

def add(x, y):
    return x + y

curried_add = curry(add)
print(curried_add(2)(3))        # Output: 5
```

### Composition
You can compose multiple functions to create new behavior.

```python
def compose(f, g):
    return lambda x: f(g(x))

def double(x):
    return x * 2

def increment(x):
    return x + 1

composed_function = compose(double, increment)
print(composed_function(5))     # Output: 12 (5 + 1 = 6, then 6 * 2 = 12)
```

### Event Handler
Event handlers are higher-order functions that react to events like button clicks.

```python
import tkinter as tk

def on_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=on_click)  # Event handler: on_click
button.pack()
root.mainloop()
```

### Callbacks
Callbacks are widely used in asynchronous programming. In Python, a callback could be a function passed to handle the result of another function.

```python
def fetch_data(callback):
    data = {"name": "Alice", "age": 25}
    callback(data)

def handle_data(data):
    print(f"Data received: {data}")

fetch_data(handle_data)  # Handle data after fetching it
```

### Closures
A closure occurs when a nested function captures variables from its enclosing scope even after the outer function has finished execution.

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n  # `n` is captured from the outer scope
    return multiplier

double = make_multiplier(2)
print(double(5))  # Output: 10
```
Here, multiplier() retains access to n even after make_multiplier() has returned, demonstrating a closure.

These real-world applications of higher-order functions show their power in asynchronous programming, event-driven systems, and encapsulating state with closures.

A higher-order function is a versatile and powerful concept that forms the backbone of many functional programming techniques. Whether you're using them for decorators, callback functions, or functional programming techniques like currying and composition, higher-order functions help make code more modular, reusable, and expressive.