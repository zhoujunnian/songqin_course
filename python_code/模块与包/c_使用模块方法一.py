
print('***  in test1  begin *** ')
import b_a     # python解析器去找这个文件，如果找到了，就会 执行完 里面所有的代码，然后再往下执行
import sys
print(sys.path)
print(sys.stdout.encoding)
print(type(b_a))
print(type(b_a.calc_s_c))   # b_a也是对象，模块对象

b_a.calc_s_c(20)

print(b_a.var1)

print('***  in test1  end *** ')