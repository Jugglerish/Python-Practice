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
