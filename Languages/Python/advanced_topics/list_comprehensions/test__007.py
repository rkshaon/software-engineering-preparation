import re

sentence = """
In 1984, there were 13 instances of a protest 
with over 1000 people attending.
"""

numbers = re.findall(r'\d+', sentence)
# Convert strings to integers if needed
numbers = [int(num) for num in numbers]

print(numbers)
