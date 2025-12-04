# One Liners Python Code
10 Python one-liners that showcase elegance, cleverness, and real-world usefulness.

## Reverse a String
```python
text = “clcoding”
print(text[::-1])
```

`[::-1]` slices the string backward. Simple, compact, wonderful.

## Find Even Numbers From a List
```python
nums = [1, 2, 3, 4, 5, 6]
evens = [n for n in nums if n % 2 == 0]
```

List comprehensions let you *filter and transform* with grace.

## Check If Two Words Are Anagrams
```python
print(sorted(”listen”) == sorted(”silent”))
```

Sorting characters reveals structural equivalence.

## Count Frequency of Items
```python
from collections import Counter
print(Counter(”banana”))
```

The result beautifully tells how many times each item appears.


## Swap Two Variables Without Temp
```python
a, b = 5, 10
a, b = b, a
```

Python makes swapping feel like a tiny magic trick.

## Flatten a List of Lists
```python
flat = [x for row in [[1,2],[3,4]] for x in row]
```

Nested list comprehension walks down layers elegantly.

## Read a File in One Line
```python
data = open(”file.txt”).read()
```

Great for quick scripts. Just remember to close or use with for production.


## Get Unique Elements From a List
```python
unique = list(set([1,2,2,3,4,4,5]))
```

Sets remove duplicates like a digital comb.

## Reverse a List
```python
nums = [1, 2, 3, 4]
nums.reverse()
```

A one-liner that modifies the list in place.

## Simple Inline If-Else
```python
age = 19
result = “Adult” if age >= 18 else “Minor”
```

Readable, expressive, and close to natural language.


#### Reference
- [Python Coding @ SubStack.com](https://pythonclcoding.substack.com/p/10-python-one-liners-that-will-blow)
