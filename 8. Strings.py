# 1. Create your multiline string and show how to print it.
lyrics =  '''Cause we were just kids when we fell in love
Not knowing what it was
I will not give you up this time
But darling, just kiss me slow
Your heart is all I own
And in your eyes, you're holding mine'''
print(lyrics)
lyrics1 = "Cause we were just kids when we fell in love \n Not knowing what it was \nI will not give you up this time \nBut darling, just kiss me slow \nYour heart is all I own \nAnd in your eyes, you're holding mine"
print(lyrics1)

# 2. Create a program that accepts a string and displays each word's length and the length of the string.
stringinput = input("Enter your String here: ")
striglen = len(stringinput)
print("String character's length: ", striglen)
stringwordlist = stringinput.split( ) 
stringwordlist = list(stringwordlist)
stringwordlen = len(stringwordlist )
print("String word length: ", stringwordlen, "\n" )

for i in stringwordlist:
    print(f"{i} length: ", len(i))

# 3. Write a program that will count the number of lowercase and uppercase character in a user- supplied string.
stringinput = input("Enter your String here: ")
counterlower = 0
counterupper = 0
for i in stringinput:
    if i == i.lower():
        counterlower += 1
    elif i == i.upper():
        counterupper += 1
    else:
        print("Invalid Input")
print(f"Total lowercase character are: {counterlower}, Total uppercase characters are: {counterupper}")


# 4. Create a program that will count the length of the given string without relying on an in-built function. Given string:
given_string = "Jack and Jill went up the hill. To fetch a pail of water."
counter = 0
for i in given_string:
    counter += 1
print(f"Total characters length is: {given_string}")

word_counter = 0
wordsplit = given_string.split()
wordlist = list(wordsplit)
for j in wordlist:
    word_counter += 1

print(f"Character count: {counter} \nWord count: {word_counter}")
