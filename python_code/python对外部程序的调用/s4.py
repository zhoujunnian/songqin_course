from subprocess import PIPE, Popen
import time,sys

popen = Popen(
    'python s4_1.py',
    stdin  = PIPE,
    stdout = PIPE,
    stderr = PIPE,
    shell=True,
    encoding='utf8')

inputList = [ '3','4','37','55']
out,err = popen.communicate('\n'.join(inputList))
print(out, err)


