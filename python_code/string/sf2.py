vs = [('Jack',8756),('Patrick',10000)]

fs = '''
%10s salary: %10d $
%10s salary: %10d $
'''

print(fs % (vs[0][0], vs[0][1], vs[1][0], vs[1][1]))
