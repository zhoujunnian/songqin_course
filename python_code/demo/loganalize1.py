# coding=utf8

filepath = 'a.log'

fd = open(filepath)
lines = fd.readlines()
fd.close()

for line in lines:
    idx1 = line.find('op takes ')
    idx2 = line.find(' ',idx1)
    responsetimestr = line[idx1:idx2]
    # print responsetimestr
    rts = float(responsetimestr)




