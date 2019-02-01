# coding=utf-8
"""
subprocess库里面的Popen 类，可以：
被调用程序运行的时候，就获取其输出信息。
运行时，输入一些信息给被调用程序

args 参数要么是列表，要么是一个字符串，
shell=True表示 用shell去执行，args参数应该是字符串，
shell=False表示 不是用shell去执行，args参数应该是一个列表

非阻塞式调用外部程序，调用外部程序后，Python程序本身不停留，继续执行
"""
from subprocess import  Popen
popen = Popen(
        args='mspaint',  # 打开画图工具
        shell=True
    )
print('done')

