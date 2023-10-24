# Write a function for swapping two variables.
def swap(a, b):
    t = a
    a = b
    b = t
    return a, b

# 2. Write a Python program to print a roll number and name of a student using functions.
def info(r, n):
    print("Roll Number:", r)
    print("Name:", n)

r = input("Enter roll number: ")
n = input("Enter name: ")

info(r, n)

#3. Write an iterative version function of the factorial of a number.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    res = factorial(num)
    print(f"Factorial of {num} is {res}")

# 4. Write a Python function to compute average for variable length arguments of numbers
def avg(*args):
    if len(args) == 0:
        return 0
    total = sum(args)
    return total / len(args)

# 6. Write a Lambda function for finding the multiplication of two numbers
m = lambda a, b: a * b

r = m(5, 3)
print("Result:", r)
