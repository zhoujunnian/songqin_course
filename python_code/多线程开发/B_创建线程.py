# coding=utf8

print('main thread start.')

import threading
from time import sleep

def thread1_entry():
    print('child thread 1, start')
    sleep(15)
    print('child thread 1, end')

t1 = threading.Thread(target=thread1_entry)  # 实例化，创建线程对象

t1.start()  # start()开始执行新的线程
# 主线程继续往下执行
sleep(10)
print('main thread end.')
# 当系统中所有的线程代码都执行完后，整个进程就结束了

"""
threading.Thread只是创建线程对象
start 才是创建

注意：t1 = threading.Thread(target=thread1_entry()),
        括号里面的thread1_entry()如果这样加了括号，就是调用了
        这个函数，而这个函数没有return，就是返回none，target=none
"""