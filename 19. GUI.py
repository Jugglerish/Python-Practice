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

