# Example of Closures and State Management

def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment


count_up = counter()
print(count_up())  # Output: 1
print(count_up())  # Output: 2
