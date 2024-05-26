fruits = (
    "apple", 
    "banana", 
    "cherry", 
    "mango", 
    "grape"
)

first_element = fruits[0]               # apple
third_element = fruits[2]               # cherry
last_element = fruits[-1]               # grape
# Return the third, fourth, and fifth items
third_to_firth_element = fruits[2:5]    # ("cherry", "mango", "grape")
# First 3 elements
first_3_elements = fruits[:3]           # ("apple", "banana", "cherry")
# From 4th elements to the last
forth_to_last_elements = fruits[3:]     # ("mango", "grape")
# Items from index -4 (included) to index -1 (excluded)
n_4th_to_n_1st_elements = fruits[-4:-1] # ("banana", "cherry", "mango")

if "apple" in fruits:
    print("`apple` available in the fruits tuple.")


print(first_element)
print(third_element)
print(last_element)
print(third_to_firth_element)
print(first_3_elements)
print(forth_to_last_elements)
print(n_4th_to_n_1st_elements)