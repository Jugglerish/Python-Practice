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
