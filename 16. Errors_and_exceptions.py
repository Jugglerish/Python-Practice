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

# 3. Write a python program that access the elements of a list using range function and loop which handles index error
lst = [1, 2, 3, 4, 5]

try:
    for i in range(len(lst)):
        elem = lst[i]
        print(f"Element at index {i}: {elem}")

except IndexError:
    print("IndexError: Out of range")

# 4. Create a Python Program which has a class Biological Family and tries to access attribute using try and exception which handles Attribute Error
class BioFamily:
    def __init__(self, f, m, c):
        self.f = f
        self.m = m
        self.c = c

my_family = BioFamily("John", "Jane", ["Alice", "Bob"])

try:
    family_pets = my_family.pets
except AttributeError as e:
    print(f"AttributeError: {e}")
    print("The attribute 'pets' does not exist in the BioFamily class.")
else:
    print("Family pets:", family_pets)


# 5. Given:
#citizenship_details = {'city': 'Chennai', 'age': 22,
#'country': 'India'
#'nationality': 'Indian'}
#user_input = input('What field of data you need on citizenship?').
#Construct a Python script that accepts user input and returns results related to citizenship. Use a missing data field ("place of study and degree") to trigger a KeyError in Python and display the resulting error.

citizenship_details = {'city': 'Chennai', 'age': 22, 'country': 'India', 'nationality': 'Indian'}
user_input = input('What field of data you need on citizenship? ')

try:
    result = citizenship_details[user_input]
    print(f'{user_input}: {result}')
except KeyError as e:
    print(f'Error: {e} field not found in citizenship details.')

# 6. Clearly show using the KeyError Exception class in Python how to deal with the KeyError that was thrown by the preceding code.
my_dict = {'key1': 'value1', 'key2': 'value2'}

try:
    value = my_dict['key3']
except KeyError as e:
    print(f"Error: {e}")

print("Code continues executing...")


# 7. Write a Python script to handle a [i] ArithmeticError with a try-except statement for (67+89j)/0
# [ii] ZeroDivionError with a try-except -else statement for (491*362)/0
try:
    x = (67 + 89j) / 0
except ArithmeticError as e:
    print(f"Error1: {e}")
else:
    print(f"Result1: {x}")

try:
    y = (491 * 362) / 0
except ZeroDivisionError as e:
    print(f"Error2: {e}")
else:
    print(f"Result2: {y}")

# 8. Include a finally block and rewrite the python script (example 16.11) to handle a single value error with a try-except statement
def example_function(val):
    try:
        res = some_function(val)
        print("Result:", res)
    except ValueError as e:
        print("Error:", e)
    finally:
        print("Finally block executed")

try:
    val = int(input("Enter a number: "))
    example_function(val)
except ValueError:
    print("Invalid input. Please enter a valid number.")
