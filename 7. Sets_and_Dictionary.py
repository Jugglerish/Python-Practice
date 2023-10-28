# 1. Given a pair of sets, generate a new set by collecting all of the elements from one Set that are absent from the other Set. integer_set={21,12,22,33,65,698} magic_number_set-(2, 8, 20, 28, 50, 82, 126)
integer_set={2, 21,12,22,33,65,698}
magic_number_set={2, 8, 20, 28, 50, 82, 126}
difference = integer_set.difference(magic_number_set)
print(difference)


# Given a pair of sets, generate a new set by removing all the elements from the first set that are also present in the second stet. integer_set =(21,12,22,33,65,698} magic_number_set=( 2, 8, 20, 28, 50, 82, 126)
integer_set={2, 21,12,22,33,65,698}
magic_number_set={2, 8, 20, 28, 50, 82, 126}
integer_set.difference_update(magic_number_set)
print(integer_set)


#3. Given a pair of sets, create a new set containing only the elements in both sets. setl= {116,21,12,22,23,32,45,54,33,65,698} set2={2, 8, 20, 28, 45, 50, 54, 33 ,82, 126}
set1= {116,21,12,22,23,32,45,54,33,65,698} 
set2={2, 8, 20, 28, 45, 50, 54, 33 ,82, 126}
z = set1.intersection(set2)
print(z)
#or
y = set1 & set2
print(y)


# 4. Write a program to create a new set containing all the elements from the two sets with no replicas.
set1 ={16,21,12,22,23,32,45,54,33,65,698} 
set2={2, 8, 20, 28, 45,50,54,33, 82, 126}
set3 = set1.union(set2)
print(set3)
#or
set4 = set1 | set2
print(set4)

# Create a dictionary of pulses and their calorie counts
pulses_calories = {
    "Chickpeas": 164,
    "Lentils": 116,
    "Black beans": 127,
    "Pinto beans": 115,
    "Kidney beans": 112,
    "Peas": 81
}

def calories(pulse):
    if pulse in pulses_calories:
        return pulses_calories[pulse]
    else: 
        return "Pulse not found in the dictionary."
    
input_pulse = input("Enter the pulse name here: ").capitalize()
result = calories(input_pulse)

if result != "Pulse not found in the dictionary.":
    print(f"Calories for {input_pulse} is: {result}")
else:
    print("Pulse not found in the dictionary.")


# 5. Write a Python program to eliminate elements (777,9,999) using remove(). setl={3, 4, 5, 6, 7, 8, 777, 9, 333, 999, 555, 444}
set1={3, 4, 5, 6, 7, 8, 777, 9, 333, 999, 555, 444}
set1.remove(999)
set1.remove(777)
set1.remove(9)
print(set1)

#or

set1 = {3, 4, 5, 6, 7, 8, 777, 9, 333, 999, 555, 444}
elements_to_remove = {777, 9, 999}
for element in elements_to_remove:
    if element in set1:
        set1.remove(element)

print(set1)


# 6. Write a program in Python to use discard() to remove the numbers 6, 7, and 8 from the given Set (). setl={3, 4, 5, 6, 7, 8, 555, 333, 444}
setl = {3, 4, 5, 6, 7, 8, 555, 333, 444}
setl.discard(6)
setl.discard(7)
setl.discard(8)
print(setl)


# 7. Write a Python program that analyses whether or not two sets can be considered equivalent to one another by analysing whether or not they can be considered a superset of one another.

sets = {10,20,30,40,50}
set1 = {11, 22, 33, 44, 55,77}

set2 = {22, 44}
set3 = {22, 44}

a = sets == set1
b = set2 == set3
print( a, b)

# 8. Write a program to display the growing setl. Use add() to add each new element to the given set.
set1 = {555, 777,999,333,444}
elements = (6, 7, 8,9,5,4,3)
set2 = set(elements)
for i in set2:
    set1.add(i)
    print("Added:", i)
print(set1)

# 14. Write a Python script to create and print a dictionary ( x ,x^ * x) containing a number (between 1 and n) in the form (x, x).

def power(n):
    empty_dict = {}
    for i in range(1,  n + 1):
        empty_dict[i] = i ** i 
    return empty_dict

x = int(input("Input a number: "))
calling = power(x)
print(calling)




