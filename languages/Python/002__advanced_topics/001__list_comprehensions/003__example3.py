numbers = [1, 2, 3, 4, 5]
squares = [(lambda x: x ** 2)(x) for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]



numbers = [1, 2, 3, 4, 5]
squared_odd_numbers = [(lambda x: x ** 2)(x) for x in numbers if x % 2 != 0]
print(squared_odd_numbers)  # Output: [1, 9, 25]

