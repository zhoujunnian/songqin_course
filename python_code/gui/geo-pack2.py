# coding=utf8
from Tkinter import *

root = Tk()
root.geometry("300x200+200+200")

redbutton = Button(root, text="Red1", fg="red")
redbutton.pack(expand=TRUE,fill=BOTH)
greenbutton = Button(root, text="Red2", fg="red")
greenbutton.pack()

root.mainloop()