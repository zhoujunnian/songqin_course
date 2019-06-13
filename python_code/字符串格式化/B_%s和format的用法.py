# coding=utf-8
name = 'jcy'
height = 170

# %s的用法

print('my name is %s, and I am %scm tall' % (name, height))

print("myName is %s, I'模块与包 %d years old" % ("jack", 20))

# format的用法

print('我叫{name}, 身高{height}厘米'.format(name='jcy',height='170'))

print('my name is {}, and I am {}cm tall'.format(name, height))

print('my name is {1}, and I am {0}cm tall'.format(name, height))

# 指定宽度
print('my name is {:8}, and I am {:8}cm tall'.format(name, height))

# 指定左右对齐
print('my name is {:>8}, and I am {:>8}cm tall'.format(name, height))

# 补零
print('my name is {:8}, and I am {:08}cm tall'.format(name, height))

print('my name is {}, and I am {height:010}cm tall'.format(name, height=180))   # 这个写法也可以

# 本身就有花括号,要加2个花括号，代表不是format格式的
print('她说{{你好}},my name is {}, and I am {}cm tall'.format(name, height))

# 取字典的key，value值
"""
‘%(name)s:%(score)06.1f’ %{'score':9.5, 'name':'newsim'}
这种形式只用在要输出的内容为dictionary（一种python的数据类型）时，
小括号中的(name)和(score)对应于后面的键值对中的键。前面的例子可以看到，
”格式标记字符串“中标记的顺序和"要输出的值组"中的值是一一对应的，有顺序，
一对一，二对二。而在这种形式中，则不是，每个格式标记对应哪个值由小括号中的键来指定。
这行代码的输出为：'newsim:0009.5'
"""
data = {'name': "jcy", "height": 170}
print ('我叫%(name)s, 身高%(height)scm' % data)
