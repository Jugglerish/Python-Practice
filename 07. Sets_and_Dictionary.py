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

# 15. Find the highest three values of matching dictionary keys using the Python program. my_dict = { 'Ether':  233, 'Bitcoin': 4854, 'Litecoin': 789, 'Gaslimit': 13325}
my_dict = { 'Ether':  233, 'Bitcoin': 4854, 'Litecoin': 789, 'Gaslimit': 13325}
result_dict = sorted(my_dict.items(), key= lambda x: x[1], reverse = True)
print(result_dict)
final_dict = result_dict[:3]
print(final_dict)

# 16. Make a replica of the sample dictionary with the dict() function:
sampledict = {
"brand": "HP",
"model": "Pavilion",
"year": 2022 
}

replica_dict = dict(sampledict)
print(replica_dict)

# 17. Using Python, write a program that removes all elements from a given dataset. set1 = {"Ether","Bitcoin","Litecoin"}
set1 = {"Ether","Bitcoin","Litecoin"}
set1.remove("Ether")
set1.remove("Bitcoin")
set1.remove("Litecoin")
print(set1)

# 17. Using Python, write a program that removes all elements from a given dataset. set1 = {"Ether","Bitcoin","Litecoin"}
set1 = {1, 2, 3, 4, 4, 5}
set2 = {5, 6, 7, 8, 9}
if set1.isdisjoint(set2):
    print("The sets have no elements in common.")
else:
    print("The sets have some elements in common.")

# 19. Remove the Intersection of a second setl ={16,21,12,22,23,32,65,698} set2={ 2, 8, 20, 21,28,45,50,54,33, 82, 126} set from the first set using a Python program.
set1 = {16, 21, 12, 22, 23, 32, 65, 698}
set2 = {2, 8, 20, 21, 28, 45, 50, 54, 33, 82, 126}

set2.difference_update(set1)
print(set2)

# 20. If you want to construct a dictionary with the relevant fundamental values: 21-30; 31-40;41-50; and 51-60, write a Python program. Using the dictionary, get the fifth value of each of the keys.
my_dictionary = {
    '21-30': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    '31-40': [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    '41-50': [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    '51-60': [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
}

empty_dict = {}

for key, value in my_dictionary.items():
    empty_dict[key] = value[4]

for key, value in empty_dict.items():
    print(f"{key} fifth value is: {value}")



# Write a program that updates the created dictionary with the contents given below. Print the contents of the dictionary before and after the update operation.
# Pulses
# Calories
# Pinto beans  115
# Kidney beans 112
# Peas 81

pulses_calories = {
    "Chickpeas": 164,
    "Lentils": 116,
    "Black beans": 127
}

for key, value in pulses_calories.items():
    print(f"{key}: {value} Calories.")

while True:
    pulse_input =input("Enter the pulse name: ").capitalize()
    if pulse_input == "Quit":
        break
    try:
        calorie_input = int(input(f"Enter the number of Calories {pulse_input} contain: "))
        pulses_calories[pulse_input] = calorie_input
    except ValueError:
        print("It must be Number.")
    
for key, value in pulses_calories.items():
    print(f"{key}: {value}")
        

# 22. Given myDict={'FF012':296,'GG013':426,'H H014':683,'LL015':964).Write a program to delete the element 'GG013' from the myDict.
myDict={'FF012':296,'GG013':426,'H H014':683,'LL015':964}

if 'GG013' in myDict:
    myDict.pop("GG013")

print(myDict)


#or
if 'GG013' in myDict:
    del myDict["GG013"]
print(myDict)

#25. Using the given sets, write a Python program to determine the LESSER THAN OR EQUAL TO and GREATER THAN OR EQUAL TO operations on Set.
# third Set of Pomegranate fruits Set3={'Dholka',' Kandhari','Vadki','Kabul"','Muskati Red','Paper Shelled'}
# fourth Set of Mangoes Set4={'Banganapalli','Payri','Kesar', 'Neelum', 'Alphonso','Dasheri "','Totapuri"," Chausa'}

set_a = {'Dholka', 'Kandhari', 'Vadki', 'Kabul', 'Muskati Red', 'Paper Shelled'}
set_b = {'Banganapalli', 'Payri', 'Kesar', 'Neelum', 'Alphonso', 'Dasheri', 'Totapuri', 'Chausa'}

is_subset = set_a <= set_b
is_superset = set_a >= set_b

if is_subset:
    print("set_a is less than or equal to set_b")
else:
    print("set_a is not less than or equal to set_b")

if is_superset:
    print("set_a is greater than or equal to set_b")
else:
    print("set_a is not greater than or equal to set_b")



#Write a program to show the addition of elements to a set one by one.
fruits = {"Allahabad Safeda", "Pant Prabhat", "Dhareedar", "Chittidar"}

print("Current fruits in the set:", fruits)

while True:
    entry = input("Add a fruit (or type 'quit' to stop): ")

    if entry == 'quit':
        break

    fruits.add(entry)

    print("Updated fruits in the set:", fruits)

print("Final fruits in the set:", fruits)


