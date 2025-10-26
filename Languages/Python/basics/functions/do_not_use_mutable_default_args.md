# Why You Should Never Use Mutable Default Arguments in Python (and What to Do Instead)

Avoid one of Python’s most subtle and dangerous gotchas — the mutable default argument trap.

## 💡 Introduction

If you’ve been writing Python for a while, you might’ve stumbled upon strange behavior like this:

```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))
print(add_item("cherry"))
```

You probably expect:

```bash
["apple"]
["banana"]
["cherry"]
```

But instead, you get:

```bash
['apple']
['apple', 'banana']
['apple', 'banana', 'cherry']
```

😳 Wait, what? Why does the list keep growing when the function should start fresh every time?

Welcome to one of Python’s most infamous pitfalls:
mutable default arguments.

## ⚙️ The Root Cause: How Python Handles Defaults

In Python, default parameter values are evaluated only once — at function definition time, not every time the function is called.

That means when you write:

```python
def add_item(item, items=[]):
```

Python creates **one list in memory** when this line runs, and every future call uses the same list object.

You can confirm this with `id()`:

```python
def add_item(item, items=[]):
    print(id(items))
    items.append(item)
    return items

add_item("apple")
add_item("banana")
```

You’ll see the same memory address printed twice — meaning it’s literally the same list.

## 🚫 Why This Is Dangerous

- The function behaves unpredictably — data “leaks” between calls.

- Bugs are hard to detect, especially in large codebases.

- This affects all mutable types: list, dict, set, custom objects, etc.

## ✅ The Correct Way

Use `None` as the default value and initialize inside the function:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

Now it behaves as expected:
```python
print(add_item("apple"))   # ['apple']
print(add_item("banana"))  # ['banana']
```

Each call gets a fresh list — safe and predictable.

### 💡 The Rule of Thumb
| Type | Safe Default | Example                      |
| ----------------------------------------- | ------------ | ---------------------------- |
| Mutable (`list`, `dict`, `set`)           | `None`       | `def f(x=None): x = x or []` |
| Immutable (`int`, `str`, `tuple`, `bool`) | Direct value | `def f(x=0): ...`            |

So this is perfectly fine:

```python
def greet(name="Guest"):
    return f"Hello, {name}!"
```

…but this is not:

```python
def add_item(item, items=[]):  # ❌
    ...
```

## 🧩 Real-World Example: Access Control

Let’s take a practical example from a system:

### ❌ Wrong way
```python
def has_access(base_id=[], id_checking_list=[]):
    return not base_id or base_id in id_checking_list
```

Here, `base_id` and `id_checking_list` are shared lists across all calls.
This can cause unexpected access mismatches between users.

### ✅ Correct way
```python
def has_access(base_id=None, id_checking_list=None):
    id_checking_list = id_checking_list or []
    return not base_id or base_id in id_checking_list
```

Now each call is independent, safe, and bug-free.

## 🔍 Why This Happens (Under the Hood)
When you define a function:

```python
def f(x=[]): ...
```

Python internally does something like this:

```python
_x_default = []
def f(x=_x_default): ...
```

That `_x_default` is stored in memory for the lifetime of the program — it’s reused across all calls.

That’s why mutating it once mutates it for all.

## 🧠 Pro Tip: Use None for Optional Parameters Everywhere

Even if you think your function won’t modify the list, using None is a clean, future-proof habit.

### ✅ Good habit:
```python
def process_data(data=None):
    data = data or []
```

## 🚀 Quick Recap
| Concept | Wrong | Right             |
| --------------- | --------------------------------------- | ----------------- |
| Mutable default | `def f(x=[])`                           | `def f(x=None)`   |
| Evaluation time | Once (on define)                        | Every call (safe) |
| Side effects    | Shared state                            | Independent state |
| Applies to      | list, dict, set, custom mutable objects | same rule applies |

## 🧩 Conclusion

Mutable default arguments are one of Python’s most common and subtle bugs — even experienced developers have been burned by them.

So next time you’re defining a function, remember this one simple rule:

> “Never use mutable objects as default arguments — use `None` instead.”

It’ll save you hours of debugging and keep your functions pure, predictable, and professional.

## ✍️ Bonus Tip

If you’re working in a team, consider adding this rule to your ***flake8*** or ***pylint*** configuration:
```bash
B006: Do not use mutable data structures for argument defaults
```

