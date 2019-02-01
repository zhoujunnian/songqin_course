# coding=utf-8
fh = open('file3.txt')
bcStr = fh.read() # 这里返回的是str类型
fh.close()

uc = bcStr.decode('utf8')  # 如果文件是gbk编码，则调用 bcStr.decode('gbk')

print(uc)
print(len(uc))
print(uc[2])

print(len(bcStr))
print(bcStr[2])

