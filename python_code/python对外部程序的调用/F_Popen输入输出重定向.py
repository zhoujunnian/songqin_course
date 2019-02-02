# coding=utf-8
"""
得到外部程序的输出，
指定一个参数 stdout = PIPE,表示一个管道，想象程序的输出存储在一个特殊的文件，
虽然不是真的保存在磁盘；

"""
from subprocess import PIPE, Popen

popen = Popen(
    'dir c:\\sdfsdfsdf',
    stdout = PIPE,
    stderr = PIPE,
    shell=True
    )


output, err = popen.communicate()  # 取2个变量保存，如果程序执行正常，就输出到output，如果异常就输出到err
print(output)
print(err)

