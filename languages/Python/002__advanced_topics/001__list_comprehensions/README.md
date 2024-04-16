# List Comprehensions in Python

## What is list comprehensions?
- List comprehensions provide a one-line syntax to create a new list.
- List comprehensions applied on an existing list or any iterable object.
- They offer a more compact alternative to traditional for loops with `append`.
- Similar to a [generator expressions](../002__generator_expressions/) but creates a new list instead of iterator objects.

## Syntax
```
new_list = [expression for item in iterable if condition]
```
- `expression`: it represents the transformation applied to each item.
- `item`: it is the current element in the iteration.
- `iterable`:  the original list or other iterable objects (like tuple, string, or other objects).
- `if condition (optional)`: this allows to filters the items.

### Example
without condition
```
numbers = [1, 2, 3, 4]
multiplies = [num * 2 for num in numbers]
print(multiplies)   # Output: [2, 4, 6, 8]
```
- The expression `n * 2` calculates the multiplied value of each item (`n`) in the list `numbers` sequence.
- No condition applied.
- The entire expression creates a new list(`multiplies`) that generates numbers on demand when used in a loop.

with condition

```
sentence = "Say my name, it's Heisenberg."
uppercase_sentnce = [letter.upper() for letter in sentence if letter.lower()]
uppercase_sentnce = ''.join(uppercase_sentnce)
print(uppercase_sentnce)    # Output: SAY MY NAME, IT'S HEISENBERG.
```
- The expression `letter.upper()` converts the `letter` to uppercase of the string `sentence`.
- The if `letter.lower()` condition filters for lowercase letter.
- The entire expression creates a list `uppercase_sentence` that converts every lowercase letter to uppercase letter on demand when used in loop.

using lambda function
```
numbers = [1, 2, 3, 4, 5]
squared_odd_numbers = [(lambda x: x ** 2)(x) for x in numbers if x % 2 != 0]
print(squared_odd_numbers)  # Output: [1, 9, 25]
```
- `(lambda x: x ** 2)` creates a lambda function that takes `x` as an argument and returns its square.
- `(lambda x: x ** 2)(x)` applies the lambda function to each item `x` in the `numbers` list.
- `if x % 2 != 0` filters out even `numbers`.
- Only odd numbers are squared using the lambda function.

## Benefits
- Empower concise and clear expression of complex operations in one line, replacing multi-line code, more increase readability.
- Efficient, one-liners for big data.
- Functional style, focus on transformations.
- New lists, no surprises (avoid side effects).
- Filter & transform in one line (streamlined!).
- Short, sweet, and expressive code (one look, understand!).

## Test
#### 1. Find all numbers from 1 to 1000 that are divisible by 7 using list comprehensions.
```
divisible_by_7 = [num for num in range(1, 1001) if num % 7 == 0]
print(divisible_by_7)
```

#### 2. Identify all numbers from 1 to 1000 that contain the digit 3 using list comprehensions.
```
numbers_with_3 = [num for num in range(1, 1001) if '3' in str(num)]
print(numbers_with_3)
```