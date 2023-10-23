"""
A. Write logical expressions for the following: A. Either A is greater than B or A is less than C 
B. The favourite city is either Mumbai or Chennai
C. Either the place is Bengaluru or Chennai and not Hyderabad
D. Mark is either greater than 60 but not less than 90 
"""
x = (a > b) or (a < c)
y = (city == "Mumbai") or (city == "Chennai")
z = (location == "Bengaluru" or location == "Chennai") and location != "Hyderabad"
w = (score > 60) and (score < 90)

# Write a python program to find the roots of a quadratic equation.
import math

def find_roots(a, b, c):
    d = b**2 - 4 * a * c

    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2 * a)
        r2 = (-b - math.sqrt(d)) / (2 * a)
        return r1, r2
    elif d == 0:
        r = -b / (2 * a)
        return r
    else:
        rp = -b / (2 * a)
        ip = math.sqrt(abs(d)) / (2 * a)
        r1 = complex(rp, ip)
        r2 = complex(rp, -ip)
        return r1, r2

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

roots = find_roots(a, b, c)
if isinstance(roots, tuple):
    print("Roots are:", roots[0], "and", roots[1])
else:
    print("Root is:", roots)

# Write a program to find whether the given number is odd or even and positive or negative.
n = float(input("Enter a number: ")

if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Write a program to calculate bonuses for employees based on grade and basic pay. (Given name, grade, basic pay, dearness allowance, HRA, CCA, conveyance, etc.)
n = input("Enter employee's name: ")
g = input("Enter employee's grade: ")
bp = float(input("Enter employee's basic pay: ")

da = bp * 0.10
hra = bp * 0.15
cca = bp * 0.05
conveyance = 1000.0

bonus = da + hra + cca + conveyance

print("Employee Name:", n)
print("Grade:", g)
print("Basic Pay:", bp)
print("Bonus Amount:", bonus)

# Write a program to display the day's name, given the date of a specific month.
import datetime

x = input("Enter a date (YYYY-MM-DD): ")
d = datetime.datetime.strptime(x, "%Y-%m-%d")
w = d.weekday()
n = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("The day for", x, "is", n[w])


