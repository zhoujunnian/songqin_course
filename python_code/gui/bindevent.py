# coding=utf-8

from Tkinter import *

root = Tk()

def key(event):
    print "pressed", repr(event.char)

def callback(event):
    print "clicked at", event.x, event.y

frame = Frame(root, width=200, height=200)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()