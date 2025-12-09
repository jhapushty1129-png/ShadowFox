# -------------------------------
# 1. BMI Calculator
# -------------------------------

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


print()
# -------------------------------
# 2. City to Country
# -------------------------------

australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
uae = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
india = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name: ")

if city in australia:
    print(f"{city} is in Australia")
elif city in uae:
    print(f"{city} is in UAE")
elif city in india:
    print(f"{city} is in India")
else:
    print("City not found in the list")


print()
# -------------------------------
# 3. Check if two cities belong to same country
# -------------------------------

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

def get_country(city):
    if city in australia:
        return "Australia"
    elif city in uae:
        return "UAE"
    elif city in india:
        return "India"
    else:
        return None

c1 = get_country(city1)
c2 = get_country(city2)

if c1 is None or c2 is None:
    print("One or both cities not found in the list")
elif c1 == c2:
    print(f"Both cities are in {c1}")
else:
    print("They don't belong to the same country")
