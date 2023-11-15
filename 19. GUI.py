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

