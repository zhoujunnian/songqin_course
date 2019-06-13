a = '我们这时候'
print(a)
print(type(a))
fh = open('file2.txt', 'wb')     # 二进制打开，要自己指定编码方式写入
fh.write(a.encode('utf8'))
fh.close()

a = '我们这时候'
print(a)
print(type(a))
fh = open('file1','w',encoding='utf8')      # 默认是utf8，可以不写，但是有中文的写入，加上比较好
fh.write(a) # 或者fh.write(a.encode('gbk'))
fh.close()



a = '我们这时候'
print(a)
print(type(a))
fh = open('file2.txt','w',encoding='gbk')
fh.write(a)
fh.close()


