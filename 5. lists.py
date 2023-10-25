world_animals = ['Anaconda', 'Platypus', 'Red panda', 'Beaver', 'Killer whale', 'Platypus', 'Camel', 'Polar bear', 'King penguin', 'Snow leopard', 'Zebra', 'Plains bison']
world_biomes = ['Tropical Rainforest', 'Temperate Forest', 'Taiga', 'Desert', 'Arctic Tundra', 'Antarctica Tundra', 'Alpine Tundra', 'Marine', 'Freshwater', 'Tropical Grassland', 'Temperate Grassland']

# Create a program to calculate and return the length of the given lists.
animals = len(world_animals)
print(animals)
bioms = len(world_biomes)
print(bioms)

# 2. Create a program to count up how many times an item appears in a given list. Given Platypus in world animals Taiga in world_biomes
animals = world_animals.count('Platypus')
print(f" Platypus occusred {animals} times")

# 2. Create a program to count up how many times an item appears in a given list. Given Platypus in world animals Taiga in world_biomes
counter = 0
for i in world_animals:
    if i == 'Platypus':
        counter += 1
print(counter)

# same for biomes

# 3. Write a program to find the index of the first matching element for 'Snow leopard' in the list of world animals
indexing = world_animals.index("Snow leopard")
print(indexing)

# 4. Write a program to examine a list for an item Anaconda in world_animals Forest in world_biomes
for i in world_animals:
    if i in "Anaconda":
        print("Found Anaconda")
        break
    else:
        print("Anaconda Not found")
        break


# 4. Write a program to examine a list for an item Anaconda in world_animals Forest in world_biomes
for i in world_animals:
    if i in "Anaconda":
        print("Found Anaconda")
        break
    else:
        print("Anaconda Not found")
        break

#easy way
if "Anaconda" in world_animals:
    print("Found Anaconda in world_animals")
else:
    print("Anaconda Not found in world_animals")

# same for Biomes

# 4. Write a program to examine a list for an item. Anaconda in world_animals Forest in world_biomes.
world_animals.reverse()
print(world_animals)

# 5. Write a program to reverse the order of the world_biomes list in Python
world_biomes.reverse
print(world_biomes)

# 6. Write a python script that concatenates the above given two lists into one.
concatenate_list  =  world_animals + world_biomes
print(concatenate_list)

# 7. Write a program to insert an item to the world animals list at a given position. Given: Item is, "Elephant" Position is 3.
world_animals.insert(3, "Elephant")
print(world_animals)

# 8. Create a program that will remove every item in the given list of world_animals.
while world_animals:
    world_animals.pop()
print(world_animals)

#or

#  Create a program that will remove every item in the given list of world_animals.
for animal in list(world_animals):  
    world_animals.remove(animal)
    print(f"Removed: {animal}")

# 9. Write some code to utilise the zip function to merge the above given two lists into a single tuple list.
merged = list(zip(world_animals, world_biomes))
print(merged)

# Given below are two lists Indian_animalsIndian Auroch","Asiatic Civet","Indian Javan Cheetah","Malabar Rhinocéros","Asiatic Cheetah"] Superstitious_numbers=[3,7,8,666] Show what will happen after using extend(Superstitious_numbers) operation on the first list.
Indian_animals = ["Indian Auroch", "Asiatic Civet", "Indian Javan Cheetah", "Malabar Rhinocéros", "Asiatic Cheetah"]
Superstitious_numbers = [3, 7, 8, 666]
Indian_animals.extend(Superstitious_numbers)
print(Indian_animals)

# 11. Write a program to reverse a list in Python Given: list1 = [101, 202, 303, 404, 505]
list1 = [101, 202, 303, 404, 505]
list1.reverse()
print(list1)

# 12. Concatenate two lists index-wise Write a program to add two lists index-wise. Create a new list containing the Oth index item from both lists, then the 1st index item, and so on until the last element. Any leftover items will get added at the end of the new list. Given: common_name= ['Carrot', 'Garlic','Onion', 'Tomato','Potato'] sample2 = botanical_name = ['Daucus carota', 'Allium sativum', 'Allium cepa','Lycopersican esculentum','Solanum tuberosum'] Expected output:[The botanical name for Carrot is Daucus carota', 'The botanical name for Garlic is Allium sativum', 'The botanical name for Onion is Allium cepa', 'The botanical name for Tomato is Lycopersican esculentum', 'The botanical name for Potato is Solanum tuberosum'
common_name = ['Carrot', 'Garlic','Onion', 'Tomato','Potato']                                                                                                                                                                                                        
botanical_name = ['Daucus carota', 'Allium sativum', 'Allium cepa','Lycopersican esculentum','Solanum tuberosum']
counter = 0
for i in common_name:
    print(f"The botanical name for {i} is {botanical_name[counter]}")
    counter += 1

#or

common_name = ['Carrot', 'Garlic', 'Onion', 'Tomato', 'Potato']
botanical_name = ['Daucus carota', 'Allium sativum', 'Allium cepa', 'Lycopersican esculentum', 'Solanum tuberosum']

for common, botanical in zip(common_name, botanical_name):
    print(f'The botanical name for {common} is {botanical}')

# Write a program to iterate both lists simultaneously and display items from listl in original order and items from list2 in reverse order.

# Given:
# listl=[10, 20, 30, 40]
# list2=[100, 200, 300, 400]

# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100

list1=[10, 20, 30, 40]
list2=[100, 200, 300, 400]
list2.reverse()
for lst, lst2 in zip(list1, list2):
    print(lst, " ", lst2)

#14. Write a program that will iterate through a list's values and indices. world_animals=['Anaconda", 'Red panda', 'Beaver', 'Killer whale', 'Platypus', 'Camel', 'Polar bear', 'King penguin', 'Snow leopard', 'Zebra', 'Plains bison']
world_animals = ['Anaconda', 'Red panda', 'Beaver', 'Killer whale', 'Platypus', 'Camel', 'Polar bear', 'King penguin', 'Snow leopard', 'Zebra', 'Plains bison']

for index, animal in enumerate(world_animals):
    print(f"Index {index}: {animal}")

# 15. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# Given list:
# listl = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "I"],
# "m", "n"] # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f, 'g', 'h', 'T', 'j'], 'k'], 'T'], 'm', 'n']
sub_list = ["h", "i", "j"]
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "I"], 'm', 'n']
list1[2][1][2].extend(sub_list)
print(list1)

# 16. Replace the list's item with a new value if found
# Given a Python list, write a program to find the value D in the list; if it is present, replace it with XYZ. Only update the first occurrence of an item. Given: listl=['A','B','C','D','E','F','G','H']
# Expected output: ['A', 'B', 'C', 'XYZ', 'E', 'F', 'G', 'H']

listl=['A','B','C','D','E','F','G','H']
for i in range(len(listl)):
    if listl[i] == 'D':
        listl[i] = 'XYZ'
        break
print(listl)

# 17. Write a program to merge all the items in a list into one long string. Given:
# Listl=["Anaconda","is", "the","animal", "inhabiting", "the", "Tropical", "Rainforest"]
list1=["Anaconda","is", "the","animal", "inhabiting", "the", "Tropical", "Rainforest"]
string = ""
for i in list1:
    string = string + " " + i

print(string)
