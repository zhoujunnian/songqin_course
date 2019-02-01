# coding=utf-8
from Tkinter import *
import tkMessageBox

root = Tk()              # 创建主窗口
root.title('test')       # 设置主窗口 标题
root.geometry("300x200+200+200") # 设置主窗口 大小和位置


def hello():
    tkMessageBox.showinfo('Message', 'Hello, world' )

# 创建按钮
button = Button(root, text='Hello', command=hello)
# 指定button在父窗口的布局方式
button.pack()

# 进入消息循环处理
root.mainloop()

