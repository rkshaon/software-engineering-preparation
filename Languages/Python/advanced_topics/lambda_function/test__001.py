# Use lambda function to verify if 2 variables summation is equal to target

target = 8

add = lambda x, y: x + y
result = add(5, 3)
assert result == target

print("Test passed")

result = add(6, 3)
assert result == target

print("Test passed")
