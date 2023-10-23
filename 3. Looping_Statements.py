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



