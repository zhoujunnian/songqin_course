# coding=utf8
from Tkinter import *
import time

root = Tk()

Label(root, text="input a number").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="result").grid(row=1, column=0)
e2Text = StringVar()
e2 = Entry(root, textvariable=e2Text)
e2.grid(row=1, column=1,columnspan=2,sticky='w',pady=5 )

def showSquare():
    val = e1.get().strip()
    time.sleep(3) # 阻塞操作，睡眠3秒钟
    resultStr =  'square is %s' % int(val)**2
    e2Text.set(resultStr)

Button= Button(root, text="OK",command=showSquare).grid(row=0, column=2,padx=5,pady=5)

root.mainloop()