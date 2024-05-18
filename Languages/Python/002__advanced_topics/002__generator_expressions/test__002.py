def fibonacci_generator(n):
  """
  Generates the Fibonacci sequence up to a specified number `n`.

  Args:
      n: The maximum value in the sequence (exclusive).

  Yields:
      Each subsequent Fibonacci number in the sequence.
  """
  a, b = 0, 1

  for _ in range(n):
    yield a
    a, b = b, a + b


limit = 10
fibonacci_sequence = fibonacci_generator(limit)

for num in fibonacci_sequence:
  print(num)  # Output: 0 1 1 2 3 5 8 13 21 34
