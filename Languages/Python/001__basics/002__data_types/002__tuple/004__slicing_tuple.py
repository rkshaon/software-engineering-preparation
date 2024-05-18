fruits = ("apple", "banana", "cherry", "mango", "grape")

# Basic slicing: [start:stop:step]
# Extract elements from index 1 to index 3 (not including index 4)
subset = fruits[1:4]
print(subset)           # Output: ('banana', 'cherry', 'mango')

# Omitting start or stop parameters
subset_start = fruits[2:]  # Extract elements starting from index 2 to the end
# Extract elements from the beginning up to index 2 (not including index 3)
subset_stop = fruits[:3]
print(subset_start)        # Output: ('cherry', 'mango', 'grape')
print(subset_stop)         # Output: ('apple', 'banana', 'cherry')

# Negative indexing
# Extract elements from the third-last to the second-last
subset_negative = fruits[-3:-1]
print(subset_negative)           # Output: ('cherry', 'mango')

# Step parameter
every_other = fruits[::2]   # Extract every other element
print(every_other)          # Output: ('apple', 'cherry', 'grape')
