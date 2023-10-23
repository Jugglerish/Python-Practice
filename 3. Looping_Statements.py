# Write a program to use a for loop and a continue statement to go through all of the entered numbers one by one. The subsequent elements in the sequence are activated when a particular element in the sequence has a value of 16. Given x=[23,43,56,78,16,9,7,12,14,15]
x = [23,43,56,78,16,9,7,12,14,15]
for i in x:
    print("Processing:", i)
    if i == 16:
        print("Found 16")

# 2. Write a Python program that handles the following situation with while and if-else statements."Gourmande patrons a restaurant on a regular basis. The Gourmande can place an order from the restaurant's menu. If the order is identical to the "Signature dish", the server notes it and takes it down; otherwise, they may recommend the "Signature dish" instead of the favourite dish."
menu = ["pizza", "burger", "pasta", "tacos"]
signature_dish = "pasta"
favorite_dish = ""

while True:
    order = input("Enter your order: ")

    if order == signature_dish:
        print("Order noted by server.")
    else:
        print("You might like our signature dish instead of your favorite dish.")

#3. Make use of for-loop statements in the code to deal with the following scenario. "Books can be checked out as many times as needed, but the library only allows 10 visitors per day. Find out how many books were asked for in total."
total = 0

days = int(input("Enter how many days the library is open: "))

for d in range(1, days + 1):
    print(f"Day {d}:")
    
    total_daily = 0
    
    visitors_day = int(input(f"How many visitors on Day {d}? "))
    
    for v in range(1, visitors_day + 1):
        books = int(input(f"How many books did Visitor {v} want? "))
        total_daily += books
    
    print(f"Total books wanted on Day {d}: {total_daily}")


#4 ake use of a for-else loop and break statements in the code to deal with the following scenario.Due to pandemic regulations, an online store 12 can only ship to a maximum of 6 USERS and up to 50 accessories at a time. Users 1 and 2 each place an order of INR 78 and INR 54. As stock runs out, deny the third request.
a_c = 50

for x in range(6):
    y = int(input("Enter the money in INR: "))
    z = int(input("Enter the number of add-ons you want to buy: "))
    
    if z > a_c:
        print("You can't buy more than 50 add-ons")
        break
    elif x == 2:
        print("Sorry, we're out of stock")
        break
else:
    print("Too many customers. No more orders.")


# 5. Exhibit how Pass can be used as a placeholder for future code in a (i) for loop in range(3,7). (ii) for loop in range(12).
for i in range(12):
    x = 1
for x in range(3, 7):
    z = 1

#6. Write a for loop for this scenario, "In this game, you have FIVE chances to win. The player will get what he wants if his request is granted. If the program continues, he can play again."
n = 5  # Number of chances
w = "win"  # What player wants

for i in range(n):
    p = input("Enter your request: ")
    if p == w:
        print("You got it!")
        break
    else:
        print("Sorry, try again.")
#7. Create a program to check whether movie tickets are available or not.
a = 50
t = int(input("Enter number of tickets: "))
if t > 0:
    if t <= a:
        print("Tickets available.")
    else:
        print("Not enough tickets.")
else:
    print("Invalid input.")

# 8. Iterate through the given string printing each letter using the for loop.
s = "Hello, world!"
for c in s:
    print(c)
#9. Iterating through fibonacci_series= a (1,1,2,3,5,8,13,21,34,55,89) by using the for loop as the primary control structure
fibonacci_series = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

for number in fibonacci_series:
    print(number)
    
#10. Write a program to use Python for loops for the fibonacci_series= (1,1,2,3,5,8,13,21,34,55,89)
f = [1, 1]
n = 9

for i in range(2, n):
    nt = f[i - 1] + f[i - 2]
    f.append(nt)

for num in f:
    print(num)
# 11. Write a program using the for loop that outputs each word in the list. rice= ["Arborio", "Wehani", "Basmati" ] Also, print each word's characters instead. str="Hakuna Matata"



