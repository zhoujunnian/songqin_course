a = '我们这时候'
print(a)
print(type(a))
fh = open('file1','w')
fh.write(a.encode('utf8')) # 或者fh.write(a.encode('gbk'))
fh.close()
