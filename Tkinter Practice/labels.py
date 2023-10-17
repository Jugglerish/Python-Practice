from tkinter import *
window = Tk()
icon = PhotoImage(file='help_large.png')
window.geometry("425x425")  
label = Label(window, text="Hellow World",
               font=('Arail', 40, 'bold'),
                 fg='purple', bg='grey',
                 relief=RAISED,
                 bd = 20,
                 padx = 10,
                 pady = 30,
                 image=icon,
                 compound='bottom')
label.pack()
#label.place(x=200, y= 100)
window.mainloop()