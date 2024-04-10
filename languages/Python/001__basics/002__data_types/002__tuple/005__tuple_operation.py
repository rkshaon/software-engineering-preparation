fruits = ("apple", "banana", "cherry", "mango", "grape")

fruits_length = len(fruits)                 # 5
print(fruits_length)

max_item = max(fruits)                      # mango
print(max_item)

min_item = min(fruits)                      # apple
print(min_item)

numbers = (99, 33, 66, 44)
sorted_numbers = sorted(numbers)            # [33, 44, 66, 99]
sorted_numbers = tuple(sorted_numbers)      # (33, 44, 66, 99)

numbers = (99, 33, 66, 44)
reversed_numbers = tuple(reversed(numbers)) # (44, 66, 33, 99)
print(reversed_numbers)