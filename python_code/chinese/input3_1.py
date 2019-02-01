fh = open('file3.txt','r',encoding='utf8')
bcStr = fh.read()
fh.close()



print(bcStr)
print(len(bcStr))
print(bcStr[2])

