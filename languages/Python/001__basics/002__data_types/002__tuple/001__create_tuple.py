my_tuple1 = ()                                  # empty tuple
my_tuple2 = tuple()                             # empty tuple
my_tuple3 = (1, "hello", 3.14, True)            # A tuple with mixed data types
my_tuple4 = ((1, 2), ('a', 'b'), (True, False)) # A tuple with nested tuples
my_tuple5 = (42,)                               # Single element tuple (note the trailing comma)
my_tuple6 = "Hello",                            # Single element tuple (note the trailing comma)

print(my_tuple1)
print(my_tuple2)
print(my_tuple3)
print(my_tuple4)
print(my_tuple5, type(my_tuple5))
print(my_tuple6, type(my_tuple6))