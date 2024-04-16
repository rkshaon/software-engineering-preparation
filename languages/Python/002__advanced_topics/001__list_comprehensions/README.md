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

#### 3. Given a string, count the number of spaces it contains using list comprehensions.
```
text = """
In the 16th century, an age of great marine and terrestrial exploration, 
Ferdinand Magellan led the first expedition to sail around the world. As 
a young Portuguese noble, he served the king of Portugal, but he became 
involved in the quagmire of political intrigue at court and lost the king’s 
favor. After he was dismissed from service by the king of Portugal, he 
offered to serve the future Emperor Charles V of Spain.
"""

space_count = sum([1 for char in text if char == ' '])
print(space_count)
```

#### 4. Create a list of all consonants (non-vowels) from a string.
```
text = """
In the 16th century, an age of great marine and terrestrial exploration, 
Ferdinand Magellan led the first expedition to sail around the world. As 
a young Portuguese noble, he served the king of Portugal, but he became 
involved in the quagmire of political intrigue at court and lost the king’s 
favor. After he was dismissed from service by the king of Portugal, he 
offered to serve the future Emperor Charles V of Spain.
"""

consonants = [char for char in text if char.isalpha() and char.lower()
              not in 'aeiou']
print(consonants)
```

#### 5. From a list, generate tuples containing the index and value for each item.
```
my_list = ["hi", 4, 8.99, 'apple', ('t,b', 'n')]

indexed_values = [(index, value) for index, value in enumerate(my_list)]
print(indexed_values)
```

#### 6. Find the common numbers between 2 lists (without using a tuple or set).
```
list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]

common_numbers = [num_a for num_a in list_a if num_a in list_b]
print(common_numbers)
```

#### 7. Extract all numbers from a sentence.
```
import re

sentence = "In 1984, there were 13 instances of a protest with over 1000 people attending."

numbers = re.findall(r'\d+', sentence)
numbers = [int(num) for num in numbers]
print(numbers)
```