
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

# 2. Generate odd numbers in the range 0 - 100 using list comprehension
lst = [i for i in range(1, 101) if i % 2 != 0]
print(lst)

#3. Generate prime numbers in the range 0-50 using list comprehension
lst = [i for i in range(2, 51) if all(i % x != 0 for x in range(2, i))]
print(lst)

# 6. Write a map function to sort these words based on the length of the word [Hello, India, Tamil, Malayalam, Delhi].
words = ["Hello", "India", "Tamil", "Malayalam", "Delhi"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)


# 7. Write a reduce function for the list [1, 2, 68, 10, 12, 14] for the expression x + y.
import functools 
lst = [1, 2, 68, 10, 12, 14]
reduced_list = functools.reduce(lambda x,y: x+y, lst)
print(reduced_list)
