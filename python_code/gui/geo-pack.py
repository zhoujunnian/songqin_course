# coding=utf8
from Tkinter import *

root = Tk()
root.geometry("300x200+200+200")

frame = Frame(root)
frame.pack()
redbutton = Button(frame, text="Red1", fg="red")
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text="Red2", fg="red")
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text="Red3", fg="red")
bluebutton.pack( side = LEFT )

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM  )
blackbutton = Button(bottomframe, text="Black1", fg="black")
blackbutton.pack(side = BOTTOM)
blackbutton = Button(bottomframe, text="Black2", fg="black")
blackbutton.pack(side = LEFT)
blackbutton = Button(bottomframe, text="Black3", fg="black")
blackbutton.pack()

root.mainloop()