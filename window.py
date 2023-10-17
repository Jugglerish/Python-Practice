from tkinter import *

window = Tk()  
window.geometry("425x425")  
window.title("First GUI Window")
icon = PhotoImage(file='help_large.png')
window.iconphoto(True, icon)
window.config(background="black")
window.mainloop()  

