# -------------------------------
# 1. Friends list → tuples
# -------------------------------

friends = ["Aditi", "Rohan", "Meera", "Kavya", "Sam"]
friend_tuples = []

for name in friends:
    friend_tuples.append((name, len(name)))

print("Friend tuples:", friend_tuples)


print()
# -------------------------------
# 2. Trip expenses
# -------------------------------

your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner total expenses:", partner_total)

# Who spent more?
if your_total > partner_total:
    print("You spent more.")
elif partner_total > your_total:
    print("Your partner spent more.")
else:
    print("Both spent the same amount.")

print()
# Check expense with biggest difference

max_diff_category = None
max_diff_value = 0

for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff_value:
        max_diff_value = diff
        max_diff_category = category

print("Category with biggest difference:", max_diff_category)
print("Difference:", max_diff_value)
