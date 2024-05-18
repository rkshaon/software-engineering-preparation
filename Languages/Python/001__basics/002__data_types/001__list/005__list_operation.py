fruits = ["apple", "banana", "cherry", "mango", "grape", "banana"]

length_of_fruits = len(fruits)
banana_appears = fruits.count("banana")
grape_index = fruits.index("grape")
is_mango_exist = "mango" in fruits
is_mango_not_exist = "manngo" not in fruits
sorted_fruits = fruits.sort()
reverse_sorted_fruits = fruits.sort(reverse=True)

fruits = ["apple", "banana", "cherry", "mango", "grape", "banana"]

fruits.reverse()
new_fruits = fruits.copy()

numbers = [20, 21, 39, 13, 62]
max_number = max(numbers)       # 62
max_fruits = max(fruits)        # mango
min_number = min(numbers)       # 13
min_fruits = min(fruits)        # apple

new_list = [True, False]
print(all(new_list))            # False
print(any(new_list))            # True
new_list = []                   
print(all(new_list))            # True
print(any(new_list))            # False
new_list = [True, True, True]
print(all(new_list))            # True
new_list = [False, False, False]
print(any(new_list))            # False