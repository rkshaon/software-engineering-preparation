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
