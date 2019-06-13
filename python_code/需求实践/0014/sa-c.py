# coding=utf-8
from socket import *
import traceback,sys

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


class CloseSocketError(Exception):
    pass

class ConnectionHandler:
    # 0008|1|nickname
    LEN_MSG_LEN_FIELD = 4
    LEN_MSG_LEN_TYPE_FIELD = 7



    def __init__(self,sock):
        # 消息缓存区
        self._readbuffer = b''
        self.sock = sock
        self.customername = ''


    # msgBody 是 unicode
    @staticmethod
    def encode(msgType,msgBody):
        rawMsgBody = msgBody.encode('utf8')

        msgLenth = '{:04}' \
        .format(len(rawMsgBody)+ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD) \
        .encode()

        msgType = f'{msgType}'.encode()
        return b'|'.join([msgLenth,msgType,rawMsgBody])

    @staticmethod
    def decode(rawmsg):
        msgType = int(rawmsg[5:6])
        msgbody = rawmsg[ConnectionHandler.LEN_MSG_LEN_TYPE_FIELD:].decode('utf8')
        return [msgType,msgbody]

    def readMsg(self):
        bytes = self.sock.recv(BUFSIZ)

        # ** 用不同的返回值表示不同的含义

        # 当对方关闭连接的时候，抛出异常
        if not bytes:
            self.sock.close()
            raise CloseSocketError()

        self._readbuffer += bytes

        buffLen = len(self._readbuffer)

        # 如果已经获取了消息头部 (包括 消息长度，消息类型)
        if buffLen >= self.LEN_MSG_LEN_TYPE_FIELD:
            msgLen = int(self._readbuffer[:self.LEN_MSG_LEN_FIELD])
            # 缓存区消息 已经包含了一个整体的消息(包括 消息长度，消息类型，消息体)
            if buffLen >= msgLen:
                # 从缓存区，截取整个消息
                msg = self._readbuffer[0:msgLen]
                # 缓存区变成剩余的消息部分
                self._readbuffer = self._readbuffer[msgLen:]

                return self.decode(msg)

        # 如果已经获取的消息还不包括一个完整的消息头部, 不做处理等待下面继续接受消息
        else:
            return None

        print('--> %s' % bytes)

    # msgBody 是 unicode
    def sendMsg(self,msgType,msgBody):
        self.sock.sendall(self.encode(msgType,msgBody))

    def handleMsg(self,msgType,msgBody):
        # 客户名称
        if msgType == 2:
            print(msgBody)
            print('---------------')

    def userinputAndSend(self):
        msgSend = input('>>')
        self.sendMsg(2, msgSend)

    # 主循环，不断的接受消息发送消息
    def mainloop(self):
        # 先发送客户名称
        userName = '***'
        if len(sys.argv) > 1:
            userName = sys.argv[1].decode(sys.stdin.encoding)
        self.sendMsg(1,userName)
        while True:
            try:
                self.userinputAndSend()
                # print('reading...')
                msg = self.readMsg()
                if msg:
                    msgType,msgBody= msg
                    self.handleMsg(msgType,msgBody)
            except CloseSocketError:
                print('对方断开了连接,程序退出')
                return
            except IOError:
                print('对方断开了连接,程序退出')
                return




#创建socket，指明协议
tcpCliSock = socket(AF_INET, SOCK_STREAM)

#连接远程地址和端口
tcpCliSock.connect(ADDR)

handler = ConnectionHandler(tcpCliSock)
handler.mainloop()