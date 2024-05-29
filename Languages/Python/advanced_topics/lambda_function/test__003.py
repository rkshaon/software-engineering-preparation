numbers = [1, 2, 3, 4, 5]
is_even = lambda n: n % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)
