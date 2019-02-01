# coding=utf8
from Tkinter import *

root = Tk()
root.geometry("300x200+200+200")

button = Button(root, text='Hello')
button.place(height=50, width=80,relx=0.5, rely=0.5,)

root.mainloop()