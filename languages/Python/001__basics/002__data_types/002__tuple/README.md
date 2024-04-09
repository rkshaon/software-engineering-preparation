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

