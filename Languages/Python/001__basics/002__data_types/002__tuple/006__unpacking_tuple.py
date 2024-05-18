points = (10, 5, 20, 99, 32)        # packing
a, b, c, d, e = points              # unpacking

print(points)
print(a, b, c, d, e)

*a, b, c = points                   # a: [10, 5, 20], b: 99, c: 32, a is list type
print(a, b, c, type(a))

a, *b, c = points                   # a: 10, b: [5, 20, 99], c: 32
print(a, b, c)

a, b, *c = points                   # a: 10, b: 5, c: [20, 99, 32]
print(a, b, c)