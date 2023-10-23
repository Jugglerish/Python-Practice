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

# Take a three-digit number and find the reverse of the number.
number = input("Enter a three-digit number: ")

if len(number) == 3 and number.isdigit():
    reversed_number = int(number[::-1])
    print("Reverse of the number:", reversed_number)
else:
    print("Please enter a valid three-digit number.")

# Take the customer's first name and last name and print them as last name first followed by the first name.
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
print(f"{last_name} {first_name}")

#Get the principal amount, interest, and year and find the simple interest and compound interest.
# Get the principal amount, interest, and year and find the simple interest and compound interest.
def calculate_si(p, r, t):
    si = (p * r * t) / 100
    return si

def calculate_ci(p, r, t):
    n = 1
    a = p * (1 + (r / (100 * n))**(n * t))
    ci = a - p
    return ci

p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate (in %): "))
t = float(input("Enter the time period (in years): "))

si = calculate_si(p, r, t)
ci = calculate_ci(p, r, t)

print(f"Principal: ${p}")
print(f"Rate: {r}%")
print(f"Time: {t} years")
print(f"SI: ${si}")
print(f"CI: ${ci}")
