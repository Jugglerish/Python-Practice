# 1. Create a GUI based window to enter data into the database of at least four attributes recursively.
import tkinter as tk

def add():
    print(f"Name: {name.get()}, Age: {age.get()}, Email: {email.get()}, Address: {address.get()}")
    name.delete(0, tk.END)
    age.delete(0, tk.END)
    email.delete(0, tk.END)
    address.delete(0, tk.END)

root = tk.Tk()
root.title("Data Entry")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name = tk.Entry(root)
name.grid(row=0, column=1)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=1, column=0)
age = tk.Entry(root)
age.grid(row=1, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0)
email = tk.Entry(root)
email.grid(row=2, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0)
address = tk.Entry(root)
address.grid(row=3, column=1)

display_button = tk.Button(root, text="Display Data", command=add)
display_button.grid(row=4, columnspan=2)

root.mainloop()


# 2. Create a simple GUI comprising two text boxes to receive input for the value of n and r and display the value of "C, in the Window itself.
import tkinter as tk
import math

def calc():
    n = int(entry_n.get())
    r = int(entry_r.get())
    result.config(text=f"Value of C: {math.comb(n, r)}")

root = tk.Tk()
root.title("Combination Calculator")

label_n = tk.Label(root, text="n:")
label_n.grid(row=0, column=0)
entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1)

label_r = tk.Label(root, text="r:")
label_r.grid(row=1, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=1, column=1)

button_calc = tk.Button(root, text="Calculate", command=calc)
button_calc.grid(row=2, columnspan=2)

result = tk.Label(root, text="Value of C: ")
result.grid(row=3, columnspan=2)

root.mainloop()


# 3. Create a simple GUI with four buttons with different foreground colours and background colours.
import tkinter as tk

def dummy():
    pass

root = tk.Tk()
root.title("Buttons")

for text, fg, bg in [("Button 1", "white", "blue"), ("Button 2", "black", "yellow"),
                      ("Button 3", "white", "green"), ("Button 4", "black", "red")]:
    tk.Button(root, text=text, fg=fg, bg=bg, command=dummy).pack()

root.mainloop()

# 4. Create a simple GUI containing a text area enabled with horizontal scrolling.
import tkinter as tk

r = tk.Tk()
r.title("Horizontal Scroll Text")

s = tk.Scrollbar(r, orient="horizontal")
s.pack(side="bottom", fill="x")

t = tk.Text(r, wrap="none", xscrollcommand=s.set)
t.pack()

s.config(command=t.xview)

r.mainloop()


# 5. Create a simple GUI to receive value of height and radius of a cylinder and calculate its volume.
import tkinter as tk
import math

def calculate():
    try:
        h = float(e_h.get())
        r = float(e_r.get())
        result.config(text=f"Volume: {math.pi * r ** 2 * h:.2f}")
    except ValueError:
        result.config(text="Enter valid numbers")

root = tk.Tk()
root.title("Cylinder Volume")

l_h = tk.Label(root, text="Height:")
l_h.grid(row=0, column=0)
e_h = tk.Entry(root)
e_h.grid(row=0, column=1)

l_r = tk.Label(root, text="Radius:")
l_r.grid(row=1, column=0)
e_r = tk.Entry(root)
e_r.grid(row=1, column=1)

b_calc = tk.Button(root, text="Calculate", command=calculate)
b_calc.grid(row=2, columnspan=2)

result = tk.Label(root, text="Volume: ")
result.grid(row=3, columnspan=2)

root.mainloop()


# 6. Create a user registration form and store the details as an object of User Class. The attributes of the User Class are first_name, last_name, address, email, contact_number and aadhaar_ number.
import tkinter as tk

class User:
    def __init__(self, first, last, address, email, contact, aadhaar):
        self.first = first
        self.last = last
        self.address = address
        self.email = email
        self.contact = contact
        self.aadhaar = aadhaar

def register():
    user = User(e_fn.get(), e_ln.get(), e_add.get(), e_email.get(), e_cn.get(), e_aadhaar.get())
    print("User Registered:")
    for attr, value in user.__dict__.items():
        print(f"{attr.capitalize()}: {value}")

r = tk.Tk()
r.title("User Registration")

labels = ["First Name:", "Last Name:", "Address:", "Email:", "Contact Number:", "Aadhaar Number:"]
entries = []

for i, label_text in enumerate(labels):
    tk.Label(r, text=label_text).grid(row=i, column=0)
    entry = tk.Entry(r)
    entry.grid(row=i, column=1)
    entries.append(entry)

tk.Button(r, text="Register", command=register).grid(row=len(labels), columnspan=2)

e_fn, e_ln, e_add, e_email, e_cn, e_aadhaar = entries

r.mainloop()

# 7. Create a GUI to Say whether the given number is a prime number or not. Note: Use Text box and use label to display the result.
import tkinter as tk

def check():
    try:
        num = int(e.get())
        is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
        res.config(text=f"{num} is {'a prime number' if is_prime else 'not a prime number'}")
    except ValueError:
        res.config(text="Please enter a valid number")

r = tk.Tk()
r.title("Prime Checker")

tk.Label(r, text="Enter a Number:").grid(row=0, column=0)
e = tk.Entry(r)
e.grid(row=0, column=1)

tk.Button(r, text="Check", command=check).grid(row=1, columnspan=2)

res = tk.Label(r, text="")
res.grid(row=2, columnspan=2)

r.mainloop()

# 8. Write a Python program to receive a text from the user and print the reversed text in the form label after clicking the reverse button in the GUI. For example, if "xyz" is given as input and "zyx" is displayed as the output.
import tkinter as tk

def reverse():
    res.config(text=e.get()[::-1])

r = tk.Tk()
r.title("Text Reversal")

tk.Label(r, text="Enter Text:").grid(row=0, column=0)
e = tk.Entry(r)
e.grid(row=0, column=1)

tk.Button(r, text="Reverse", command=reverse).grid(row=1, columnspan=2)

res = tk.Label(r, text="")
res.grid(row=2, columnspan=2)

r.mainloop()


