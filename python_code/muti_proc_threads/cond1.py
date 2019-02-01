# coding=utf-8
import threading,time
from random import randint

# 存放共享资源的 列表
commandList =[]

# 创建锁对象
cv = threading.Lock()

# 生产者线程
def thread_producer():
    global  commandList

    cmdNo = 0
    while True:

        cmdNo += 1

        # 这里生产的资源，就先用一个字符串来表示
        resource = f'command_{cmdNo}'

        # 随机等待一段时间,表示 生产资源的时间，就是输入命令耗费的时间
        time.sleep(randint(3,3))

        # 生产好了后，先申请锁
        cv.acquire()

        #申请锁成功后， 资源 存放入 commandList （共享对象）中
        commandList.append(resource)

        print('produce resource %s' % resource)
        # 释放锁
        cv.release()



# 消费者线程，
def thread_consumer ():
    global  commandList

    while True:
        # 先申请锁
        cv.acquire()

        resource = None
        # 拿出 生产者线程 产生的一个资源，也就是一个命令
        if commandList:
            # 表示，已经被本消费者取出该资源了
            resource =  commandList.pop(0)


        # 取出一个共享资源后释放锁(生产者线程就可以对共享资源进行操作了)
        cv.release()

        if resource != None:
            # 随机等待一段时间,表示 消费资源的时间
            time.sleep(randint(1, 3))
            print('consume resource %s' % resource)

        # 注意上面的代码，当commandList里面没有 命令的时候
        #  就会不停的执行空循环，非常耗CPU资源

if __name__=='__main__':
    t1 = threading.Thread(target=thread_producer)
    t2 = threading.Thread(target=thread_consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
