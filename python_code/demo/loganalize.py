# coding=utf8

filepath = 'a.log'

fd = open(filepath)
lines = fd.readlines()
fd.close()

# 100ms以下的
list100 = []
# 100ms-500ms
list100_500 = []
# 500_1000ms
list500_1000 = []
# 1000ms以上的
list1000 = []

keyword = 'op takes '
for line in lines:

    # 获取响应时间
    idx1 = line.find(keyword)
    idx1 += len(keyword)
    idx2 = line.find(' ',idx1)
    responsetimestr = line[idx1:idx2]
    rts = float(responsetimestr)

    # 存入容器
    if rts < 0.1:
        list100.append(rts)
    elif  0.1 <= rts < 0.5:
        list100_500.append(rts)
    elif  0.5 <= rts < 1:
        list500_1000.append(rts)
    elif  rts >= 1:
        list1000.append(rts)

print list100

print list100_500

print list500_1000

print list1000




