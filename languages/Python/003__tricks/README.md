# Python Tricks

## 0001: `is` vs `==`
`is`: This operator checks for object identity. In other words, it checks if both variables refer to the exact same object in memory.

`==`: This operator checks for object equality. It checks if the values of the objects on both sides of the operator are equal.

#### Example
```
a = [1, 2, 3]
b = a

print(a is b) # True
print(a == b) # True

c = list(a)

print(a == c) # True
print(a is c) # False
```

#### Explain
- Created a list `a = [1, 2, 3]`
- Assigned `b = a`
- So, `a` and `b` refered the same list object in memory.
- `a is b` returns `True`.
- `a == b` is `True` because both `list` contains the same value.
- Create a new list `c = list(a)`, `c` creates a new object in memory but contains the same value as `a`.
- `a == c` returns `True` because both `list` contains same value.
- `a is c` returns `False` because they are not refering same object in memory.
