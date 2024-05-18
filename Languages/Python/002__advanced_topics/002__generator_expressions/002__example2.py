numbers = range(1, 11)
squares = (x * x for x in numbers if x % 2 == 0)

for num in squares:
  print(num)  # Output: 4 16 36 64 100
