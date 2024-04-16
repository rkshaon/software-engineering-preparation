# "is" vs "=="

a = [1, 2, 3]
b = a

print(a is b) # True
print(a == b) # True

c = list(a)
print(a == c) # True
print(a is c) # False