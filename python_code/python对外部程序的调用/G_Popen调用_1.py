# coding=utf8
from subprocess import PIPE, Popen
import time,sys

popen = Popen(
    'python开发 s4_1.py',
    stdin  = PIPE,
    stdout = PIPE,
    stderr = PIPE,
    shell=True)

inputList = [ '3','4','37','55']
#out,err = popen.communicate('\n'.join(inputList))
out,err = popen.communicate("3")
print(out, err)


