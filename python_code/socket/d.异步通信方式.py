# coding=utf8
import asyncore
import socket,traceback

HOST = ''
PORT = 21567
BUFSIZ = 1024


# 创建继承自asyncore.dispatcher 的子类，处理连接请求
class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        # 调用dispatcher 的 create_socket方法，
        # 创建用于监听的socket，这个socket是非阻塞的
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    # 定义 handle_accept 函数，当有客户端连接请求过来的时候，库会自动调用
    def handle_accept(self):

        # 接受连接请求
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print(f'从 {addr} 来的连接' )
            # 创建EchoHandler实例， 初始化函数会设置 sock为非阻塞的
            handler = EchoHandler(sock,addr)


# 创建继承自asyncore.dispatcher 的子类，处理连接后的socket消息
class EchoHandler(asyncore.dispatcher):
    def __init__(self,sock,addr):
        asyncore.dispatcher.__init__(self,sock)
        self.addr = addr

    # 定义 handle_read 函数，当有消息过来的时候，库会自动调用
    def handle_read(self):
        data = self.recv(BUFSIZ)
        if data:
            print('%s:%s' % (self.addr, data.decode()))
            self.send(data)
        else:
            print(f'客户端{self.addr}关闭了连接')
            self.close()


server = EchoServer(HOST, PORT)
# 主循环，查看 所有的 sock上是否有 相应的事件，如果有，调用对应的函数
asyncore.loop()