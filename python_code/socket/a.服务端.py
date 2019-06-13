# 导入socket 库
from socket import *

# 主机地址为空字符串表示，所有的地址都绑定，
# 包括环回地址，所有网络接口的ip地址 127.0.0.1
# 客户端必须事先知道服务端的地址才能连接成功
HOST = '0.0.0.0'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 创建socket，指明协议,AF_INET表示是IPv4协议,  SOCK_STREAM表示是tcp协议
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# 绑定地址和端口，表示使用这个地址
# HOST为空字符串表示 本机所有ip， port为21567
tcpSerSock.bind(ADDR)

#使socket处于监听状态，参数大意是指，允许等待连接的客户端的最大数量
# 这个TCP 服务进程监听在 本机所有ip， port为21567，等待客户端的连接。
tcpSerSock.listen(5)





print('等待客户端连接...')


# accept <阻塞式> 等待连接请求，有客户端连接上来，
# 只有服务端程序调用了accept，
# 才会有 syn ack ，客户端收到后发送 ack， 三路握手完成， 连接才能成功

# 注意，这里返回了一个新的socket：tcpCliSock用来和这个连接上来的客户端进行通信
# 原来的 tcpSerSock 还是负责监听
tcpCliSock, addr = tcpSerSock.accept()
print('连接来自:', addr)

while True:
    # 阻塞式等待接收消息，BUFSIZ指定了一次最多获取多少byte的消息，1024个字节
    # 返回的是bytes类型，
    # 缺省是阻塞模式，可以设置socket 为nonblocking

    data = tcpCliSock.recv(BUFSIZ)

    # 当对方关闭连接的时候，返回空bytes
    if not data:
        tcpCliSock.close()
        break

    # 接受到的是bytes类型，需要解码
    rstr = data.decode()

    print(rstr)


    # 服务端把消息发送回去，发送消息 send 不一定能发送所有的数据
    # sendall 会反复尝试，直到所有的数据都发送完毕
    # 发送的也必须是bytes类型，encode 编码
    # ** 星号表示服务端回给客户端到消息
    tcpCliSock.sendall(f'** {rstr}'.encode())


tcpSerSock.close()