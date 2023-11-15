# Use the following text files for the programming exercise.

# specimenl.txt
# Fintech, a combination of the terms "financial" and technology," refers to businesses that use technology to enhance or automate financial services and processes.

# specimen2.txt
# Python is one of the famous programming language.
# Python is used in the Financial Analyses and other processing.

# specimen3.txt
# Python is useful in storing and retrieving data into a file including database.
# The data analysis is made easier in Python which make add fuels to its popularity.
# Python adopts to any upcoming trend in IT industry.




# Create a text file and then display it using a Python script
content = """Python is useful in storing and retrieving data into a file including database.
The data analysis is made easier in Python which make add fuels to its popularity.
Python adopts to any upcoming trend in IT industry."""

with open("sample.txt", "w") as file:
    file.write(content)
with open("sample.txt", "r") as file:
    print(file.read())



# 2. Create a Python program that generates a file containing a list of all English alphabet letters arranged in a specific order.
order = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

with open('alphabet.txt', 'w') as file:
    file.write(order)

# 3. Create a Python program that reads the named specimen2.txt file line-by-line and count the number of lines.
file_name = "specimen2.txt"

with open(file_name, "r") as file:
    count = sum(1 for line in file)

print(f"The total lines in the file '{file_name}' are: {count}")

# 4. Create a Python program that reads a random line from a file (specimen2.txt file)and outputs it.
import random

file = "specimen2.txt"

with open(file, "r") as f:
    lines = f.readlines()
    rand_line = random.choice(lines)

print("Random line:", rand_line)



# 5. Create a Python program to merge each line from the first file(specimenl.txt file) with the equivalent line from the second file (specimen3. txt file).
f1 = "specimen1.txt"
f2 = "specimen3.txt"

with open(f1, "r") as a, open(f2, "r") as b:
    lines_a = a.readlines()
    lines_b = b.readlines()

    min_lines = min(len(lines_a), len(lines_b))
    md_lines = [f"{lines_a[i].strip()} {lines_b[i]}" for i in range(min_lines)]

for line in merged_lines:
    print(line)
