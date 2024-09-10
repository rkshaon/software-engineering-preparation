# Example of Currying

def curry(f):
    return lambda x: lambda y: f(x, y)


def add(x, y):
    return x + y


curried_add = curry(add)
print(curried_add(2)(3))  # Output: 5
