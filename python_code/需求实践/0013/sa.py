# coding=utf8
import requests
import threading


urls = [
'http://mirrors.163.com/centos/6.9/isos/x86_64/README.txt',
'http://mirrors.163.com/centos/7.3.1611/isos/x86_64/0_README.txt'
]

# 对应urls 依次存储网页文件内容, 先创建同样个数的元素占位
fileContentList = [None for one in urls]

# 锁对象，用来控制访问 fileContentList
lock = threading.Lock()

def thread_entry(idx,url):
    print('thread #%s start' % idx)
    r = requests.get(url)

    # 注意上面的代码不应该放在获取锁的代码中
    lock.acquire()
    # 注意 r.text的类型是unicode，可以在文档中查到
    fileContentList[idx] = r.text
    lock.release()

    print('thread #%s end' % idx)


if __name__ == '__main__':
    print('main thread start.')

    threadpool = []

    for idx,url in enumerate(urls):
        t = threading.Thread(target=thread_entry,
                          args=(idx,url))
        t.start()

        threadpool.append(t)


    # 等所有 线程结束
    for t in threadpool:
        t.join()

    # 所有线程结束后，所有内容都获取到了，合并内容

    mergeTxt = '\n\n----------------------\n\n'.join(fileContentList)
    print(mergeTxt)

    with open('readme89.txt','w',encoding='utf8') as f:
        f.write(mergeTxt)

    print('main thread end.')




