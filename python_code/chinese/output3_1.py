a = '我们这时候'
print(a)
print(type(a))
fh = open('file1','w',encoding='gbk')
fh.write(a)
fh.close()
