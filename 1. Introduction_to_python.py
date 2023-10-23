# Write a Python program to get the values for a, b, c and evaluate the following expression delta = √b2-4ac.

import math

a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))
c = float(input("Enter the value of 'c': "))

def calculate_the_delta(a, b, c):
    delta = b**2 - 4 * a * c
    return delta

delta = calculate_the_delta(a, b, c)

if delta >= 0:
    square_root_of_delta = math.sqrt(delta)
    print("Square Root of Delta (√Δ) =", square_root_of_delta)
else:
    print("The discriminant is negative, so there are no real solutions.")

# Find out the temperature for 12 months of the year and find out the year's average temperature

temps = []

for i in range(1, 13):
    while True:
        try:
            t = float(input(f"Enter temperature for {i} month: "))
            temps.append(t)
            break
        except ValueError:
            print("Please enter a valid temperature (a number).")

a = sum(temps) / len(temps)

print("Monthly Temperatures:")
for i, t in enumerate(temps, start=1):
    print(f"Month {i}: {t}°C")

print(f"Yearly Avg Temp: {a:.2f}°C")

