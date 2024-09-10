# Example of Composition

def compose(f, g):
    return lambda x: f(g(x))


def double(x):
    return x * 2


def increment(x):
    return x + 1


composed_function = compose(double, increment)
print(composed_function(5))  # Output: 12 (5 + 1 = 6, then 6 * 2 = 12)
