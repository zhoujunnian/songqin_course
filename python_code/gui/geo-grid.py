# coding=utf8
from Tkinter import *

root = Tk()

Label(root, text="First").grid(row=0, column=0)
Entry(root).grid(row=0, column=1)


Label(root, text="Second").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)

Label(root, text="Third Cross").grid(row=2, column=0,columnspan=2, )

root.mainloop()