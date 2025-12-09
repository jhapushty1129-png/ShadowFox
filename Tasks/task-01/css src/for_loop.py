import random

# -------------------------------
# 1. Roll a die 20 times
# -------------------------------

rolls = [random.randint(1, 6) for i in range(20)]

count_6 = rolls.count(6)
count_1 = rolls.count(1)

two_6_in_row = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        two_6_in_row += 1

print("Rolls:", rolls)
print("Times rolled 6:", count_6)
print("Times rolled 1:", count_1)
print("Two 6s in a row:", two_6_in_row)


print()
# -------------------------------
# 2. Jumping jacks workout
# -------------------------------

total = 100
done = 0

while done < total:
    done += 10
    print(f"You completed {done} jumping jacks.")

    tired = input("Are you tired? (yes/no) ")

    if tired.lower() in ["yes", "y"]:
        skip = input("Do you want to skip remaining sets? (yes/no) ")
        if skip.lower() in ["yes", "y"]:
            print(f"You completed a total of {done} jumping jacks.")
            break
        else:
            print(f"You have {100 - done} remaining.")
    else:
        print(f"You have {100 - done} remaining.")

    print()

if done >= 100:
    print("Congratulations! You completed the workout.")
