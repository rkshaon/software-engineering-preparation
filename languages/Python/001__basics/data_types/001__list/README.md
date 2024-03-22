# List

Lists are one of the fundamental data structures in Python. They are used to store collections of items and are ordered and changeable, meaning you can modify the list after it's created.

## Define `List`

- **`List`** can be created using square brackets `[]` or keyword `list()`.
- **`List`** can contain items of any data type (strings, integers, floats, booleans, or even other lists), including mixed types.
- **`List`** elements separated by commas.

#### Example:
```
my_list1 = [] # empty list
my_list2 = list() # empty list
my_list3 = [1, "hello", 3.14, True]  # A list with mixed data types
```

## Access `List`
- **`List`** elements accessed by their index within square brackets.
- **`Lists`** are indexed starting from `0`. The first element has index `0`, the second element has index `1`, and so on.
- Negative indexing starts from `-1` for the last item.

#### Example:
```
fruits = ["apple", "banana", "cherry", "mango", "grape"]

first_element = fruits[0]
third_element = fruits[2]
last_element = fruits[-1]
```

## Modify `List`
- **`Lists`** are mutable.
- Can be update an indexed value by assigning a new one.
- Can append new elements using the `append()` method.
- Can be inserted elements at a specific index using the `insert()` method.
- Can be remove elements using the `remove()` method (removes the first occurrence) or `pop()` method (removes and returns the element at a specific index or the last element by default).

#### Example
```
fruits = ["apple", "banana", "cherry", "mango", "grape"]

fruits[1] = "strawberry"  # Changes the second element
fruits.append("orange")  # Adds "orange" to the end
fruits.insert(1, "mango")  # Inserts "mango" at index 1
fruits.remove("cherry")  # Removes the first occurrence of banana
removed_item = fruits.pop()  # Removes and stores the last element in removed_item
```