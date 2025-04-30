# Method Chaining
**Method chaining** is a technique where each method call **returns the object itself**, so that you can call multiple methods **in a single line**.

## Example
```python
burger = BurgerBuilder().add_cheese().add_tomato().add_lettuce().build()
```

## Explain
Each method in the `BurgerBuilder` class returns `self`.
```python
def add_cheese(self):
    self.cheese = True
    return self
```

So after calling `add_cheese()`, you get back the same object and can call `add_tomato()` next — this is **[fluent interface style](https://en.wikipedia.org/wiki/Fluent_interface)**.

## Real Example: Poem
```python
class Poem:
    def __init__(self, title: str) -> None:
        self.title = title

    def indent(self, spaces: int):
        """Indent the poem with the specified number of spaces."""
        self.title = " " * spaces + self.title
        return self

    def suffix(self, author: str):
        """Suffix the poem with the author name."""
        self.title = f"{self.title} - {author}"
        return self
```

Call
```bash
>>> Poem("Road Not Travelled").indent(4).suffix("Robert Frost").title
```

Output
```bash
'    Road Not Travelled - Robert Frost'
```