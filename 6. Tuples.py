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

