# coding=utf-8
"""
调用外部程序：
os函数里面的system函数，等于打开操作系统的shell，敲入一串命令；
阻塞式的跳用：
调用的程序没有退出时，python程序会一直停在哪里，直到外部程序退出了，代码才接着换下执行；

"""
# 打开 Sublime Text，这个调用的不是阻塞式的
import os
os.system('open -a "/Applications/Sublime Text.app/Contents/MacOS/Sublime Text"')
print('after call')
