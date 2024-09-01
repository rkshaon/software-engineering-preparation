# merge two dictionaries shorthand

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)    # {'c': 4, 'a': 1, 'b': 3}
