# -------------------------------------
# 3) LIST – JUSTICE LEAGUE OPERATIONS
# -------------------------------------


# Initial list
justice_league = [
"Superman", "Batman", "Wonder Woman",
"Flash", "Aquaman", "Green Lantern"
]
print("Initial list:", justice_league)


# 3.1 Count members
print("Number of members:", len(justice_league))


# 3.2 Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl & Nightwing:", justice_league)


# 3.3 Move Wonder Woman to the start
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman as leader:", justice_league)


# 3.4 Place Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Green Lantern placed between Aquaman & Flash:", justice_league)


# 3.5 Replace entire list
justice_league = [
"Cyborg", "Shazam", "Hawkgirl",
"Martian Manhunter", "Green Arrow"
]
print("New team list:", justice_league)


# 3.6 Sort and identify new leader
justice_league.sort()
print("Sorted team:", justice_league)
print("New leader:", justice_league[0])