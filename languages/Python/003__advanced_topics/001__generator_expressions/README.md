# Generator Expressions in Python

## What is generator expressions?
- Generator expressions are a concise way to create iterators in Python.
- They look similar to list comprehensions, but instead of creating a list that holds all the elements at once, they generate elements on demand.

## Syntax
```
generator_expression = (expression for item in iterable if condition)
```
- `expression`: This defines what value will be produced for each item in the iterable.
- `item in iterable`: This iterates over the elements in the sequence (like a list, tuple, or string).
- `if condition (optional)`: This allows you to filter elements based on a condition.

### Example
```
numbers = range(1, 11)
multiply_numbers = (n*10 for n in numbers)

for n in multiply_numbers:
    print(n)    # Output: 10 20 30 40 50 60 70 80 90 100
```
- The expression `n * 10` calculates the multiplied value of each item (`n`) in the list `numbers` sequence.
- No condition applied.
- The entire expression creates an iterator (`multiply_numbers`) that generates numbers on demand when used in a loop.
```
numbers = range(1, 11)
squares = (x * x for x in numbers if x % 2 == 0)

for num in squares:
  print(num)  # Output: 4 16 36 64 100
```
- The expression `x * x` calculates the square of each item (x) in the list `numbers` sequence.
- The if `x % 2 == 0` condition filters for even numbers only.
- The entire expression creates an iterator (`squares`) that generates the `squares` of even numbers on demand when used in a loop.

## Benefits
- `Memory Efficiency`: Generator expressions are memory-efficient because they don't store all elements at once like lists. This is particularly useful for large datasets.
- `Readability`: They can improve code readability by providing a concise way to create iterators within expressions.
- `Performance`: For certain operations, they can be more performant than traditional loops due to the on-demand generation.
- Generator expressions can be used for various tasks like filtering, transforming, or creating infinite sequences.
- You can use them with different iterables like strings or custom iterators.

## Test
#### 1. Write a generator expression to create a list of all uppercase letters in a string.
```
text = """
In the 16th century, an age of great marine and terrestrial exploration, 
Ferdinand Magellan led the first expedition to sail around the world. As 
a young Portuguese noble, he served the king of Portugal, but he became 
involved in the quagmire of political intrigue at court and lost the king’s 
favor. After he was dismissed from service by the king of Portugal, he 
offered to serve the future Emperor Charles V of Spain.
"""

result = (t for t in text if t.isupper())

for r in result:
    print(r)
```

#### 2. Generate an iterator that produces the Fibonacci sequence up to a certain number.
```
def fibonacci_generator(n):
  """
  Generates the Fibonacci sequence up to a specified number `n`.

  Args:
      n: The maximum value in the sequence (exclusive).

  Yields:
      Each subsequent Fibonacci number in the sequence.
  """
  a, b = 0, 1

  for _ in range(n):
    yield a
    a, b = b, a + b


limit = 10
fibonacci_sequence = fibonacci_generator(limit)

for num in fibonacci_sequence:
  print(num)  # Output: 0 1 1 2 3 5 8 13 21 34
```

#### 3. Filter a list of numbers and keep only those divisible by 3.
```
numbers = range(1, 101)
results = (n for n in numbers if n%3==0)

for r in results:
    print(r)
```