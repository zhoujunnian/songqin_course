fh = open('file3.txt', 'rb')     # 指定二进制方式打开
bcStr = fh.read()
bcStr = bcStr.decode('utf8')    # 对读取的字符串解码
fh.close()
print(bcStr)
print(len(bcStr))
print(bcStr[2])


fh = open('file3.txt','r',encoding='utf8')
bcStr = fh.read()
fh.close()
print(bcStr)
print(len(bcStr))
print(bcStr[2])


