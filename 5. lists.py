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
