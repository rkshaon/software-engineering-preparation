
monthly_incomes = (
    ("January", 5000),
    ("February", 5500),
    ("March", 6000),
    ("April", 5800),
    ("May", 6200),
    ("June", 7000),
    ("July", 7500),
    ("August", 7300),
    ("September", 6800),
    ("October", 6500),
    ("November", 6000),
    ("December", 5500)
)

# Traverse nested tuple using loop
total_income = 0

for income in monthly_incomes:
    total_income += income[1]

print(total_income)


# Traverse nested tuple using loop and tuple unpacking
quarter_income = 0

for index, (month, income) in enumerate(monthly_incomes, start=1):
    print(f"{month:>10}: {income}")
    quarter_income += income
    if index % 3 == 0:
        print("-" * 20)
        print(f"{'Quarter':>10}: {quarter_income}", end="\n\n")
        quarter_income = 0

numbers_in_str = ("2", "9", "5", "1", "6")

# Traverse using list comprehension
numbers1 = tuple([int(number) for number in numbers_in_str])    # (2, 9, 5, 1, 6)

# Traverse using generator expressoin
numbers2 = tuple(int(number) for number in numbers_in_str)      # (2, 9, 5, 1, 6)



