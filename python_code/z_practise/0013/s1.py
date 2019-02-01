# coding=utf8

import requests
import threading


url_list = [
'http://mirrors.163.com/centos/6.8/isos/x86_64/README.txt',
'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt',
'http://mirrors.163.com/centos/6.9/isos/i386/md5sum.txt'
]

thread_num = len(url_list)

ret_list = range(thread_num)

lock = threading.Lock()

def thread_entry(url,idx):

    res = requests.get(url)

    lock.acquire()
    ret_list[idx] = res.text
    lock.release()


# 创建两个线程获取网页内容



th_pool = []
for i in range(thread_num):
    t1 = threading.Thread(target=thread_entry,args=(url_list[i], i))

    t1.start()
    th_pool.append(t1)

for th in th_pool:
    th.join()

merge_text = '\n\n\n----------------------------\n\n\n'.join(ret_list)



print merge_text