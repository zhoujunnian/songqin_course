# coding=utf-8
"""
os.system的返回值是返回码，如果想得到屏幕显示的内容，就可以用subprocess库里面的check_output方法，
subprocess.check_output 需要等到被调用程序退出，才能返回；

"""

import subprocess

# shell=True表示使用终端shell执行程序,windows下面就是cmd.exe
# 就是我们python程序调用cmd.exe 再由cmd.exe 执行 参数命令
ret = subprocess.check_output('dir', shell=True, encoding='gbk') # window系统返回的是byte类型，不是字符串，是字节串，需要自己解码
# encoding的默认值是none

# 如果有中文，需要decode，因为是中文os，所以cmd.exe输出是gbk编码
print(ret)
# print(ret.decode('gbk')) # 指定正确的解码方式

