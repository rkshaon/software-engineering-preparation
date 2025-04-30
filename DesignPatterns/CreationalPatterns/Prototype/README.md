# Prototype
The **Prototype Pattern** is used to **clone existing objects** instead of creating new ones from scratch, especially when object creation is **costly or complex**.

**Think of it like**: _"You don’t build from scratch — you copy a well-prepared template."_

## ✅ Use Cases
- When object creation is expensive (e.g., database, file I/O).

- When you need many similar objects with small differences.

- When you want to avoid building many constructors.

## 🎨 Real-Life Analogy
Think of **graphic design**:

You duplicate a shape, then tweak color or size — that’s **prototype in action**.

## Example
Python makes this super easy with copy module.

```python
import copy

class Shape:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def draw(self):
        return f"Drawing {self.color} shape at {self.position}"

    def clone(self):
        return copy.deepcopy(self)

# Usage
original_shape = Shape("Red", (10, 20))
shape_clone = original_shape.clone()
shape_clone.color = "Blue"

print(original_shape.draw())   # Drawing Red shape at (10, 20)
print(shape_clone.draw())      # Drawing Blue shape at (10, 20)
```

