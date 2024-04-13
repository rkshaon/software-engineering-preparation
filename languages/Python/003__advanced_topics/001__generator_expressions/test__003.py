numbers = range(1, 101)
results = (n for n in numbers if n%3==0)

for r in results:
    print(r)