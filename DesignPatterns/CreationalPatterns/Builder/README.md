# Builder
The Builder Pattern separates the construction of a complex object from its representation so that the same construction process can create different representations.

**Think of it like**: _"Making a burger or building a house — you want to build it part by part, not all at once."_

## 🍔 Real-Life Analogy: Building a Burger
You don’t want one messy `Burger(bun, lettuce, tomato, cheese, pickles, bacon, ketchup...)` constructor.

Instead, you do:
```python
burger = BurgerBuilder().add_bun().add_patty().add_cheese().build()
```

## Example
```python
class Burger:
    def __init__(self, bun=True, lettuce=False, cheese=False, tomato=False):
        self.bun = bun
        self.lettuce = lettuce
        self.cheese = cheese
        self.tomato = tomato

    def __str__(self):
        return f"Burger(bun={self.bun}, lettuce={self.lettuce}, cheese={self.cheese}, tomato={self.tomato})"

class BurgerBuilder:
    def __init__(self):
        self.bun = True
        self.lettuce = False
        self.cheese = False
        self.tomato = False

    def add_lettuce(self):
        self.lettuce = True
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_tomato(self):
        self.tomato = True
        return self

    def build(self):
        return Burger(self.bun, self.lettuce, self.cheese, self.tomato)

# Usage
burger = BurgerBuilder().add_cheese().add_tomato().build()
print(burger)
```

Output:
```python
Burger(bun=True, lettuce=False, cheese=True, tomato=True)
```
