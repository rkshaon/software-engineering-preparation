fruits = ["apple", "banana", "cherry", "mango", "grape"]

fruits[1] = "strawberry"  # Changes the second element
fruits.append("orange")  # Adds "orange" to the end
fruits.insert(1, "mango")  # Inserts "mango" at index 1
fruits.remove("cherry")  # Removes the first occurrence of banana
removed_item = fruits.pop()  # Removes and stores the last element in removed_item
fruits.extend(["avacado", "blueberry", "peach"]) # Add all elements of another list
new_fruits = fruits + ["Pineapple", "Papaya"]
new_fruits2 = fruits * 2
fourth_item = new_fruits2.pop(3)
new_fruits.clear()