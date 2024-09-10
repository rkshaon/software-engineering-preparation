# Example of Closures

def make_multiplier(n):
    def multiplier(x):
        return x * n  # `n` is captured from the outer scope
    return multiplier


double = make_multiplier(2)
print(double(5))  # Output: 10
