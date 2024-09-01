# Sort a Python Dictionary by Value
- Created a dictionary x = {'a': 4, 'c': 2, 'd': 1, 'b': 3, 'e': 5} where keys are letters and values are integers.
- The dictionary `x` is printed as it is, showing the original unordered state.

## Approach 1
### Code
```
x = {'a': 4, 'c': 2, 'd': 1, 'b': 3, 'e': 5}

sx1 = sorted(x.items(), key=lambda x: x[1]) 
```

### Output
```
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

### Explain
- Used the `sorted()` function with a lambda function as the key: `key=lambda x: x[1]`.
- The `lambda` function takes each item in the dictionary and returns the value (second element) for sorting.
- `sorted()` returns a list of tuples (key-value pairs) sorted by value.
- The result `sx1` is `[('d', 1), ('c', 2), ('b', 3), ('a', 4)]`.

## Approach 2
### Code
```

import operator

x = {'a': 4, 'c': 2, 'd': 1, 'b': 3, 'e': 5}

sx2 = sorted(x.items(), key=operator.itemgetter(1))
```

### Output
```
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
```

### Explain
- Used the `sorted()` function with `operator.itemgetter(1)` as the key.
- `operator.itemgetter(1)` returns a function that fetches the second element of the item (the value in the key-value pair).
- `sorted()` again returns a list of tuples (key-value pairs) sorted by value.
- The result `sx2` is `[('d', 1), ('c', 2), ('b', 3), ('a', 4)]`.
