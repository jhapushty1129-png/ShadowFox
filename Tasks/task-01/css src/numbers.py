# 2.1 Convert 145 to octal (using format)
value = 145
octal_str = format(value, 'o')   # 'o' => octal representation
print("2.1 -> format(145, 'o')  =>", octal_str)
print("Explanation: 'o' means octal (base 8)\n")

# 2.2 Circular pond: radius = 84 m
# Use pi = 3.14 and water requirement = 1.4 liters per sq.m
pi = 3.14
r = 84
area = pi * (r ** 2)                 # area in square meters
water_per_sqm = 1.4                  # liters per square meter
total_water_liters = area * water_per_sqm

print("2.2 -> Pond calculations")
print("Radius (m):", r)
print("Area (sq.m):", area)                     # float
print("Total water (liters) (float):", total_water_liters)
# Print without decimal point (integer / truncated)
print("Total water (liters) (no decimal):", int(total_water_liters))
print()  # blank line

# 2.3 Speed: cross 490 meters in 7 minutes -> m/s
distance_m = 490
time_minutes = 7
time_seconds = time_minutes * 60

speed_m_per_s = distance_m / time_seconds

print("2.3 -> Speed calculation")
print("Distance (m):", distance_m)
print("Time (s):", time_seconds)
print("Speed (m/s) (float):", speed_m_per_s)
# Print without decimal point (integer / truncated)
print("Speed (m/s) (no decimal):", int(speed_m_per_s))