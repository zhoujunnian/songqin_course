vs = [('Jack',8756),('Patrick',10000)]

# add zero
fs = '''
%-10s salary: %010d $
%-10s salary: %010d $
'''

print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))



