# -------------------------------
# 1) VARIABLES
# -------------------------------

# 1.1 Create pi and check data type
pi = 22/7
print("pi =", pi)
print("Data type of pi:", type(pi))

# 1.2 Creating variable named 'for' causes error
try:
    exec("for = 4")
except SyntaxError as e:
    print("Error: Cannot use 'for' as variable name ->", e)

# Correct alternative
for_ = 4
print("Valid variable (for_):", for_)

# 1.3 Simple Interest for 3 years
P = 10000   # principal amount (change if needed)
R = 5       # rate of interest (change if needed)
T = 3       # 3 years as per question

SI = (P * R * T) / 100
print("Simple Interest:", SI) 
#done
