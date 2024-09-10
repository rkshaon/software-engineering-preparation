# Example of Function Factories

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier


double = make_multiplier(2)
print(double(5))  # Output: 10
