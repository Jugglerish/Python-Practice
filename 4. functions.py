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

#Write a function for finding whether the give nnumber is an Armstrong number or not.
def armstrongCheck(num):
    str_num = str(num)
    len_num = len(str_num)
    sum_total = 0
    
    for d in str_num:
        sum_total += int(d) ** len_num

    return num == sum_total

n = int(input("Enter a number: "))
result = armstrongCheck(n)

if result:
    print(f"{n} iz armstrng numbr")
else:
    print(f"{n} iz not armstrng numbr")


# 8. Write a function for checking whether the number is a prime number or not
def check_prime(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if i < n:
                print(f"{n} is not a Prime number")
                break
            else:
                print(f"{n} is a Prime number")

a = int(input("Enter a number: "))
result = check_prime(a)
print(result)

