a = raw_input(':')
import sys

print(sys.stdin.encoding)
print(a.decode('utf8'))
print('\n----------\n')
print(a.decode('gbk'))
