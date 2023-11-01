
# 1. Write a lambda function to find the result for the following expressions.
# a. x ^ 4
# b. 4x + 8
# C. x ^ 3 + x ^ 2
# d. x ^ 2 + y ^ 2
# e. x ^ 2 + y ^ 2 + 18

def functiona(x):
    result = lambda x: x ** 4
    return result

def functionb(x):
    result1 = lambda x: (4 * x) + 8
    return result1

def functioc(x):
    result2 = lambda x: (x**3) + (x**2)
    return result2

def functiond(x, y):
    result3 = lambda x,y: (x**2) + (y**2)
    return result3

def functione(x, y):
    result4 = lambda x,y: (x**2) + (y**2) + 18
    return result4
