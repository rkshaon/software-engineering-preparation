class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


# Usage
vector = Vector(3, 4)
print(vector)  # Calls __str__: Output: Vector(3, 4)
vector  # Calls __repr__: Output: Vector(3, 4)
