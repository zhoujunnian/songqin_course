# coding=utf8
import threading
from time import sleep, ctime

"""
join方法，表示主线程等待子线程执行结束，再继续往下执行，等待t1线程结束，此时主线程睡眠
"""
def thread1_entry(nsec):
    print('child thread 1, start at:', ctime())
    sleep(nsec)
    print('child thread 1, end at:', ctime())


def thread2_entry(nsec):
    print('child thread 2, start at:', ctime())
    sleep(nsec)
    print('child thread 2, end at:', ctime())


if __name__=='__main__':
    print('main thread start.')
    # 创建线程对象， 指定了新线程的入口函数
    t1 = threading.Thread(target=thread1_entry, args=(1,))   # 线程里面可以带参数，args指函数的参数，后面是个元组，只有一个元素，要加逗号
    t2 = threading.Thread(target=thread2_entry, args=(2,))

    # 启动新线程
    t1.start()
    t2.start()

    # 等t1 线程结束
    t1.join()
    # 等t2 线程结束
    t2.join()
    print('main thread end.')
