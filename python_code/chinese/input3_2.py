fh = open('file3.txt','rb')
bcStr = fh.read()
# bcStr = bcStr.decode('utf8')
fh.close()



print(bcStr)
print(len(bcStr))
print(bcStr[2])

