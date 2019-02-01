a = '我们这时候'
print(a)
print(type(a))
fh = open('file2','wb')
fh.write(a.encode('gbk'))
fh.close()
