#Write a program to create a tuple of your favourite colours
fc = ("blue", "green", "purple", "red", "yellow")
print("Favorite colors:", fc)

#2. Write a program to create a tuple with different data types such as street address.
addr = ("45 Patel Nagar", "Flat 302", "Mumbai", "400012", "India")

print("Street Address:", addr[0])
print("Apartment:", addr[1])
print("City:", addr[2])
print("Pin Code:", addr[3])
print("Country:", addr[4])

#3. Write a program to convert a tuple to a string?
fc = ("blue", "green", "purple", "red", "yellow")
fcl = list(fc)
counter = 0
for i in range(len(fcl)):
    counter += 1
    print(f"String {counter} is: {fcl[i]}") 
#OR
fc = ("blue", "green", "purple", "red", "yellow")
result = ",".join(fc)
print("My Fav colours are", result)

# 4. Write a program to find the repeated items of a tuple.
fc = ("blue", "green", "purple", "red", "yellow", "White", "blue")
fcl = list(fc)
for i in fcl:
    if i == fc:
        print(f"Repeated items: {i}")
else:
    print("No repeated items")

#5 Check whether an element exists within a tuple
t = (1, 2, 3, 4, 5)

e = 3

if e in t:
    print(f"{e} exists in t.")
else:
    print(f"{e} does not exist in t.")

def check_identical(tup):
    if len(tup) <= 1:
        result = "Tuple is empty or has only 1 element"
        return result
    
    elif len(tup) >= 2:
        for i in range(len(tup)):

            if tup[i] != tup[i - 1]:
                return "The elements are not identical"
            else:
                return "The elements are identical"
       
my_tuple1 = (1, 1, 1, 1, 1, 1)
my_tuple2 = (1, 2, 3, 6, 4, 5, 6)

result1 = check_identical(my_tuple1)
result2 = check_identical(my_tuple2)

print(result1)
print(result2)

            
#7. Create a Python program that swaps two tuples.
def swapping(t1, t2):
    t1, t2, = list(t1), list(t2)
    for i in range(len(t1)):
        t1[i], t2[i] = t2[i], t1[i]
    swapped_tuple1 = tuple(t1)
    swapped_tuple2 = tuple(t2)
    
    return swapped_tuple1, swapped_tuple2

tuple1 = (6, 7, 8, 9, 1, 9)
tuple2 = (1, 2, 3, 4, 5, 6)

swapped_tuple1, swapped_tuple2 = swapping(tuple1, tuple2)
print(swapped_tuple1)
print(swapped_tuple2)

# Create a tuple with only one item 12 by writing a program.
empty_list = []
for i in range(12, 13):
    empty_list.append(i)

empty_tuple = tuple(empty_list)
print(empty_tuple)


#Develop a program to copy particular elements from one tuple to another.
t1 = (15, 25, 35, 45, 55, 65, 75, 85, 95, 105)
t2 = t1[2:8]
print(t2)

# Write a program to sort tuples by the third item if needed.
data = [(11, 12, 15), (13, 14, 11), (15, 16, 18), (17, 18, 13), (19, 20, 16)]
sort = sorted(data, key=lambda x: x[2])
for i in sort:
    print(f"{i}")

#11. Show how a tuple can be unpacked into three variables by writing a program

mt = (1, 2, 3)

v1, v2, v3 = mt

print("v1:", v1)
print("v2:", v2)
print("v3:", v3)

#12. Write a program to count the elements in a tuple.
t = (42, "apple", "xyz", 7, "banana", 3.14, 99)

c = len(t)

print("Count:", c)

# 13. Write a program to reverse a tuple.
t = (42, "apple", "xyz", 7, "banana", 3.14, 99)
my_list = []
for i in t:
    my_list.append(i)
my_list.reverse()
print(my_list)


#or

t = (42, "apple", "xyz", 7, "banana", 3.14, 99)
reversed_tuple = tuple(reversed(t))
print(reversed_tuple)


# 14. Write a Python program to unpack a list of tuples into individual elements.
t = [(42, "apple"), ("xyz", 7), ("banana", 3.14, 99), ("kjhgvcx")]
e1, e2, *e3 = t
print(e1)
print(e2)
print(e3)
