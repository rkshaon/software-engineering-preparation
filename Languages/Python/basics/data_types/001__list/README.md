# Python List
<!-- https://realpython.com/python-list/ -->
Lists are one of the fundamental data structures in Python. They are used to store collections of items and are ordered and changeable, meaning you can modify the list after it's created.

## Characteristics of `Tuple` objects
- `Ordered`: They contain elements that are sequentially arranged according to their specific insertion order.
- `Zero-based`: Zero based index for access elements.
- `Mutable`: They support in-place mutations or changes to their contained elements. They support growing or shrinking operations.
- `Heterogeneous`: They can store objects of different types.
- `Nestable`: They can contain other lists, so you can have lists of lists.
- `Iterable`: They support iteration, so traverse them using a loop or comprehension while performing operations on each of their elements.
- `Sliceable`: They support slicing operations.
- `Combinable`: They support concatenation operations.
- `Copyable`: They allows make copies of their content using various techniques.

## Constructing `List`

- **`List`** can be created using square brackets `[]` or keyword `list()`.
- **`List`** can contain items of any data type (strings, integers, floats, booleans, or even other lists), including mixed types.
- **`List`** elements separated by commas.

#### Example:
```
my_list1 = []                       # empty list
my_list2 = list()                   # empty list
my_list3 = [1, "hello", 3.14, True] # A list with mixed data types
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
- `extend(other_list)` adds all elements of another list.
- Add to list using `+` operator.
- Repeat lists using `*`.
- `pop(index)` removes and returns the item at the given index.
- `clear()` removes all items. Equivalent to _`del a[:]`_.

#### Example
```
fruits = ["apple", "banana", "cherry", "mango", "grape"]

fruits[1] = "strawberry"                            # Changes the second element
fruits.append("orange")                             # Adds "orange" to the end
fruits.insert(1, "mango")                           # Inserts "mango" at index 1
fruits.remove("cherry")                             # Removes the first occurrence of banana
removed_item = fruits.pop()                         # Removes and stores the last element in removed_item
fruits.extend(["avacado", "blueberry", "peach"])    # Add all elements of another list
new_fruits = fruits + ["Pineapple", "Papaya"]       # Concatenate
new_fruits2 = fruits * 2                            # Repeats

```

## Slicing
- Can be extracted a portion of a **`List`** using slicing with square brackets and colons.
- The syntax is `[start:end:step]`.
- `start` (inclusive) indicates the index where the slice begins.
- `end` (exclusive) indicates the index where the slice ends (the element at this index won't be included).
- `step` (optional) specifies the step size for extracting elements. Defaults to 1 (every element).

#### Example
```
fruits = ["apple", "banana", "cherry", "mango", "grape"]

using_steps = fruits[0:5:3]     # Output ["apple", "mango"]
first_two_items = fruits[0:2]   # Output ["apple", "banana"]
except_last_item = fruits[:-1]  # Output ["apple", "banana", "cherry", "mango"]
every_other_item = fruits[::2]  # Output ["apple", "cherry", "grape"]
```

## `List` Operations
- `len(list)`: Returns the length of the `list`.
- `count(item)`: Returns the number of of times a specific item appears in the `list`.
- `index(item)`: Returns the index of the first occurrence of an item in the `list`.
- `in` operator: Return boolean value if item exist or not.
- `not in` operator: Return boolean value if if item does not exist.
- `sort(list)`: Sorts the list.
- `reverse()`: Reverses the order of elements in the list.
- `copy()`: Return a shallow copy of the list. Equivalent to _`a[:]`_.
- `max(list)`: Returns the largest item in a list.
- `min(list)`: Returns the smallest item in a list.
- `all(list)`: Returns True if all elements in the list are true (or if the list is empty).
- `any(list)`: Returns True if any element in the list is true. If the list is empty, returns False.

#### Example
```
fruits = ["apple", "banana", "cherry", "mango", "grape", "banana"]

length_of_fruits = len(fruits)              # 6
banana_appears = fruits.count("banana")     # 2
grape_index = fruits.index("grape")         # 4
is_mango_exist = "mango" in fruits          # True
is_mango_not_exist = "mango" not in fruits  # False
fruits.sort()                               # ['apple', 'banana', 'banana', 'cherry', 'grape', 'mango']
fruits.sort(reverse=True)                   # ['mango', 'grape', 'cherry', 'banana', 'banana', 'apple']

fruits = ["apple", "banana", "cherry", "mango", "grape", "banana"]
fruits.reverse()                            # ['banana', 'grape', 'mango', 'cherry', 'banana', 'apple']
new_fruits = fruits.copy()

numbers = [20, 21, 39, 13, 62]
max_number = max(numbers)       # 62
max_fruits = max(fruits)        # mango
min_number = min(numbers)       # 13
min_fruits = min(fruits)        # apple

new_list = [True, False]
print(all(new_list))            # False
print(any(new_list))            # True
new_list = []                   
print(all(new_list))            # True
print(any(new_list))            # False
new_list = [True, True, True]
print(all(new_list))            # True
new_list = [False, False, False]
print(any(new_list))            # False
```