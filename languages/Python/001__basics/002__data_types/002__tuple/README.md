# Tuple
<!-- https://realpython.com/python-tuple/ -->
A `tuple` is a built-in data type that allows to create immutable sequences of values. The values or items in a tuple can be of any type. `Tuples` are sequences of objects. They’re commonly called `containers` or `collections` because a single tuple can contain or collect an arbitrary number of other objects.

## Characteristics of `Tuple` objects
- `Ordered`: They contain elements that are sequentially arranged according to their specific insertion order.
- `Lightweight`: They consume relatively small amounts of memory compared to other sequences like lists.
- `Indexable through a zero-based index`: Indexing start from zero.
- `Immutable`: They don’t support in-place mutations or changes to their contained elements. They don’t support growing or shrinking operations.
- `Heterogeneous`: They can store objects of different data types and domains, including mutable objects.
- `Nestable`: They can contain other tuples, so you can have tuples of tuples.
- `Iterable`: They support iteration, so traverse them using a loop or comprehension while performing operations with each of their elements.
- `Sliceable`: They support slicing operations, meaning that you can extract a series of elements from a tuple.
- `Combinable`: They support concatenation operations.
- `Hashable`: They can work as keys in dictionaries when all the tuple items are immutable.

## Constructing `Tuple`
- `Tuple` can be created using parentheses `()` or the `tuple()` constructor.
- `Tuple` can contain items of any data type (strings, integers, floats, booleans, or even other tuples), including mixed types.
- `Tuple` elements separated by commas.
- `Tuple` have to be construct at once, because after constructing `Tuple` value can not be added.

### Example
```
my_tuple1 = ()                                  # empty tuple
my_tuple2 = tuple()                             # empty tuple
my_tuple3 = (1, "hello", 3.14, True)            # A tuple with mixed data types
my_tuple4 = ((1, 2), ('a', 'b'), (True, False)) # A tuple with nested tuples
my_tuple5 = (42,)                               # Single element tuple (note the trailing comma)
my_tuple6 = "Hello",                            # Single element tuple (note the trailing comma)

```
`my_tuple5 = (42, )`
Without trailing comma Python iterprets it as `Integer` not `Tuple`, becaure there is single value.

## Access `Tuple`
- `Tuple` elements accessed by their index within square brackets.
- `List`s are indexed starting from 0. The first element has index 0, the second element has index 1, and so on.
- Negative indexing starts from -1 for the last item.

### Example
```
fruits = (
    "apple", 
    "banana", 
    "cherry", 
    "mango", 
    "grape"
)

first_element = fruits[0]               # apple
third_element = fruits[2]               # cherry
last_element = fruits[-1]               # grape
# Return the third, fourth, and fifth items
third_to_firth_element = fruits[2:5]    # ("cherry", "mango", "grape")
# First 3 elements
first_3_elements = fruits[:3]           # ("apple", "banana", "cherry")
# From 4th elements to the last
forth_to_last_elements = fruits[3:]     # ("mango", "grape")
# Items from index -4 (included) to index -1 (excluded)
n_4th_to_n_1st_elements = fruits[-4:-1] # ("banana", "cherry", "mango")

if "apple" in fruits:
    print("`apple` available in the fruits tuple.")
```

## Modify `Tuple`
As earlier mentioned `Tuple` is immutable, which means neither item can be removed, updated or added in a `Tuple`, so any `Tuple` can not be modfied.

But there is a few other ways do do so.

- Using `+` operations, but this will create a new `tuple`.
- Repeating tuples using the `*` operator, but this will creates a new `tuple`.
- And last, convert the `tuple` into `list` and perform all the list modification operations and convert back to `tuple`
.


## Slicing `Tuple`
- Slicing creates a new `tuple` containing elements from the original `tuple`.
- The start parameter specifies the index from which to start the slice (inclusive).
- The stop parameter specifies the index at which to end the slice (exclusive).
- The step parameter specifies the increment between elements to include in the slice.
- Omitting any of these parameters defaults to using the beginning, end, and a step of 1, respectively.
- Negative indices can also be used to slice from the end of the `tuple`.
- Slicing operations do not modify the original `tuple`; they create a new `tuple` with the selected elements.

### Example
```
fruits = ("apple", "banana", "cherry", "mango", "grape")

# Basic slicing: [start:stop:step]
# Extract elements from index 1 to index 3 (not including index 4)
subset = fruits[1:4]            # ('banana', 'cherry', 'mango')

# Omitting start parameters
subset_start = fruits[2:]       # Extract elements starting from index 2 to the end

# Omitting stop parameters
subset_stop = fruits[:3]        # Extract elements from the beginning up to index 2 (not including index 3)

# Negative indexing
subset_negative = fruits[-3:-1] # Extract elements from the third-last to the second-last

# Step parameter
every_other = fruits[::2]   # Extract every other element
```

## `Tuple` Operations
- `len(tuple)`: returns the length of the `Tuple`.
- `max(tuple)`: returns the largest item from the `Tuple`.
- `min(tuple)`: returns the smallest item from the `Tuple`.
- `sorted(tuple)`: creates a new `list` which is will be sorted.
- `reverse(tuple)`: reverses the order of elements in the tuple.

### Example
```
fruits = ("apple", "banana", "cherry", "mango", "grape")

fruits_length = len(fruits)                 # 5
max_item = max(fruits)                      # mango
min_item = min(fruits)                      # apple

numbers = (99, 33, 66, 44)
sorted_numbers = sorted(numbers)            # [33, 44, 66, 99]
sorted_numbers = tuple(sorted_numbers)      # (33, 44, 66, 99)

numbers = (99, 33, 66, 44)
reversed_numbers = tuple(reversed(numbers)) # (44, 66, 33, 99)

```

## Unpacking `Tuple`
- Packing is creating a new `tuple`.
- Unpacking is extracting values from a `tuple`.
- For unpacking, the number of variables must match the number of values of the `tuple`.
- Operator (*) helps to unpack `tuple` while number of variable could be less than number of values in `tuple`. And the variable which will hold multiple value from the `tuple` will be `list`.

### Example
```
points = (10, 5, 20, 99, 32)        # packing
a, b, c, d, e = points              # unpacking

*a, b, c = points                   # a: [10, 5, 20], b: 99, c: 32, a is list type

a, *b, c = points                   # a: 10, b: [5, 20, 99], c: 32

a, b, *c = points                   # a: 10, b: 5, c: [20, 99, 32]
```

## Traversing `Tuple`
- Loop
- Unpacking tuple
- List comprehensions
- Generator expressions

### Example
[See all the examples of traversing `Tuple`](007__traversing_tuple.py)