# Python Tricks: Merge 2 dictionaries
Python merges dictionary keys in the order listed in the expression, overwriting duplicates from left to right.

## Example
```
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}

print(z)    # {'c': 4, 'a': 1, 'b': 3}
```

## Explain
- Created a dictionary `x = {'a': 1, 'b': 2}` with keys 'a' and 'b'.
- Created another dictionary `y = {'b': 3, 'c': 4}` with keys 'b' and 'c'.
- Used the `**` operator to merge both dictionaries into a new dictionary `z = {**x, **y}`.
- The `**` operator expands the dictionary into key-value pairs. When merging, if there are overlapping keys, the values from the second dictionary (`y`) override those from the first dictionary (`x`).
- `z` now contains the merged result: `{'c': 4, 'a': 1, 'b': 3}`.
- Notice that the key `'b'` from dictionary `y` (with value `3`) overrides the value from dictionary `x` (which had value `2`).
