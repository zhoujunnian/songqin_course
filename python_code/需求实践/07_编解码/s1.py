# 根据不同的编码格式，指定参数
with open('cfiles/gbk编码.txt', 'rb') as f1, \
        open('cfiles/utf8编码.txt', 'rb') as f2:
    # read后，自动转化成unicode
    content1 = f1.read()
    content2 = f2.read()

    newContent = content1.decode('gbk').encode('utf8') + content2


newFile = input('请输入新文件的名称:')

with open(newFile, 'wb') as f:
    f.write(newContent)




