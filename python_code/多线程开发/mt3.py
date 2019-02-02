# coding=utf8
import threading
from time import sleep

def thread_entry():

    # 注意 局部变量 var 的值 ，会被两个线程搞乱吗？
    var = 1
    for i in range(10):
        print('th #{} :{}'.format(threading.currentThread().ident, var))
        sleep(1)
        var += 1


if __name__=='__main__':
    print('main thread start.')
    t1 = threading.Thread(target=thread_entry)
    t2 = threading.Thread(target=thread_entry)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main thread end.')
