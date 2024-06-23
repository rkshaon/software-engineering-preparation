class Rectangle:
    def __init__(self, width=1, height=1):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Creating instances of Rectangle
rect1 = Rectangle(3, 4)
rect2 = Rectangle()  # Uses default values

print(rect1.area())  # Output: 12
print(rect2.area())  # Output: 1
