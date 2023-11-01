
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

#4. Use iterators for printing a list. Score = [ 80 90 87 76 55 44]
Score = [80, 90, 87, 76, 55, 44]
for score in Score:
    print(score)


#5. Write a map function to convert a string to lowercase letters [Hello, India, Tamil, Malayalam, Delhi].
s = ["Hello", "India", "Tamil", "Malayalam", "Delhi"]
mappedused = list(map(lambda x: x.lower(), s))
print(mappedused)

# 6. Write a map function to sort these words based on the length of the word [Hello, India, Tamil, Malayalam, Delhi].
words = ["Hello", "India", "Tamil", "Malayalam", "Delhi"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)


# 7. Write a reduce function for the list [1, 2, 68, 10, 12, 14] for the expression x + y.
import functools 
lst = [1, 2, 68, 10, 12, 14]
reduced_list = functools.reduce(lambda x,y: x+y, lst)
print(reduced_list)

#8. Generate permutations in the range (0, 50).
a = 0
b = 5
permutaion_range = range(a, b)
permutaion_list = list(permutations(permutaion_range))
print(permutaion_list)

# 9. Write a recursive program to find the GCD of two integer numbers.
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
xy = GCD(x, y)
print(xy)

# Python3 program to  find n'th Lucas number 
def lucas(n): 
	if n == 0: 
		return 2; 
	if n == 1: 
		return 1; 
	return lucas(n - 1) + lucas(n - 2); 
n = 9; 
print(lucas(n)); 
