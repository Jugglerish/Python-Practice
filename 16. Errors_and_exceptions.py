# 1. Write a program that asks for input from the user and incorporate value error exception handling into it.
while 1:
    try:
        n = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("You entered:", n)

# 2. Develop a program to demonstrate raising exceptions for a ZeroDivisionError.
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

try:
    num = float(input("Enter numerator: "))
    denom = float(input("Enter denominator: "))
    
    result = divide(num, denom)
    print("Result:", result)

except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")

