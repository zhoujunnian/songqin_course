from subprocess import PIPE, Popen
import time,sys

popen = Popen(
    'python s4_1.py',
    stdin  = PIPE,
    stdout = PIPE,
    stderr = PIPE,
    shell=True)


popen.stdin.write('3\n')
time.sleep(1)
sys.stdout.write(popen.stdout.read())


popen.stdin.write('4\n')
time.sleep(1)
sys.stdout.write(popen.stdout.read())