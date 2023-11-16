# 1. Find the odd and even elements in an array.
import numpy as np
xyz =  np.array([1,2,3,4,5,6,7,8,9])
oddele = xyz[xyz % 2!= 0]
eveele = xyz[xyz %  2 == 0]
print("Odd elements:", oddele)
print("Even elements:", eveele)



# 2. Find the sum of an array.
xyz = [1, 2, 3, 4, 5]
array_sum = sum(xyz)
print(array_sum)

#using np
import numpy as np
xyz =  np.array([1,2,3,4,5,6,7,8,9])
oddele = xyz[xyz % 2!= 0]
eveele = xyz[xyz %  2 == 0]
print("Odd elements:", oddele)
print("Even elements:", eveele)


#3. Find the duplicate elements in an array.
import numpy as np

xyz = np.array([1, 2, 3, 2, 4, 5, 3, 6, 1])

unique, counts = np.unique(xyz, return_counts=True)
dups = unique[counts > 1]

print(dups)


# 4. Using NumPy, find the five-point summary of the following list of numbers.
#A =[10 40 60 100 120 140]

import numpy as np

xyz = np.array([10, 40, 60, 100, 120, 140])

min_val = np.min(xyz)
q1 = np.percentile(xyz, 25)
med = np.median(xyz)
q3 = np.percentile(xyz, 75)
max_val = np.max(xyz)

print(min_val, q1, med, q3, max_val)




# 5. Find the matrix multiplication of these two matrices using arrays and NumPy.
A. [[1, 0, 0], [0, 1, 0], [0, 0, 1]] * z and
[[4, 3, 2], [1, 1, 7], [3, 4, 5]]
B. and
[[1, 3, 6], [1, 1, 9], [3, 2, 5]] ^ i
[[6, 3, 6], [3, 2, 9], [3, 2, 5]]
import numpy as np

A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
z = np.array([[4, 3, 2], [1, 1, 7], [3, 4, 5]])

rA_np = np.dot(A, z)

print(rA_np)


i = np.array([[1, 3, 6], [1, 1, 9], [3, 2, 5]])
ei = np.array([[6, 3, 6], [3, 2, 9], [3, 2, 5]])

ri_np = np.dot(i, ei)

print(ri_np)




# 6. Find the determinant of the following matrices using NumPy.
A. [[6, 3, 6], [3, 2, 9], [3, 2, 5]]
B. [[8, 6], [7, 2]]

import numpy as np

A = np.array([[6, 3, 6], [3, 2, 9], [3, 2, 5]])
dA = np.linalg.det(A)
print(dA)



7. #Consider the following data frame.
#Student Id                         Marks
#1                                               10
#2                                               15
#3                                               40
#4                                               60
#5                                               80
#Create a data frame using tuples and a dictionary.

import pandas as pd

dt = [
    (1, 10),
    (2, 15),
    (3, 40),
    (4, 60),
    (5, 80)
]

col = ['Student Id', 'Marks']

dd = {k: v for k, v in zip(col, zip(*dt))}

df = pd.DataFrame(dd)

print(df)

