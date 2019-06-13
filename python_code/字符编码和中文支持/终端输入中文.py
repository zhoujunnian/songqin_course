
a = input('请输入:')
import sys
print(sys.stdin.encoding)
print(a)

a = input(':')
import sys

print(sys.stdin.encoding)
print(a.decode('utf8'))
print('\n----------\n')
print(a.decode('gbk'))

