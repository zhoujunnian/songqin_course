# coding=utf8
from Tkinter import *
import time,threading

root = Tk()

Label(root, text="input a number").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="result").grid(row=1, column=0)
e2Text = StringVar()
e2 = Entry(root, textvariable=e2Text)
e2.grid(row=1, column=1,columnspan=2,sticky='w',pady=5 )


def showSquare():
    def threadentry():
        val = e1.get().strip()
        print 'get value',val
        time.sleep(3)
        resultStr =  'square is %s' % int(val)**2
        e2Text.set(resultStr)
    # 创建新的线程执行带有阻塞操作的函数
    t1 = threading.Thread(target=threadentry, args=())
    t1.start()

Button= Button(root, text="OK",command=showSquare).grid(row=0, column=2,padx=5,pady=5)

root.mainloop()