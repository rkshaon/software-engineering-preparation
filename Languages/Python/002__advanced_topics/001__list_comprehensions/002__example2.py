letters = ['a', 'b', 'c', 'd']
uppercase = [letter.upper() for letter in letters]
print(uppercase)  # Output: ['A', 'B', 'C', 'D']



sentence = "Say my name, it's Heisenberg."
uppercase_sentnce = [letter.upper() for letter in sentence if letter.lower()]
uppercase_sentnce = ''.join(uppercase_sentnce)
print(uppercase_sentnce)    # Output: SAY MY NAME, IT'S HEISENBERG.

