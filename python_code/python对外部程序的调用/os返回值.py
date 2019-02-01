
"""
返回值：
1、有些程序退出后会有一个退出码，表示程序是否正确实现了其功能，
比如linux命令的ls，执行之后，再用执行命令echo $? 便可以看到最新的命令的退出码；
2、linux系统，会返回一个16位的数字，低位字节表示结束进程的信号数值，
如果低位字节值为0，那么高位字节就表示退出码，如：512的退出码是2；
0代表正常退出码，2代表异常退出码，如ls 不存在的目录，
"""


#可以通过返回值来判断命令是否执行成功
import os
ret = os.system('cp /opt/file1 /home/jcy/file1')
if ret==0:
    print('file copied.')
else:
    print('copy file failed!!')

#window系统，返回值就是退出码
import os
ret = os.system('dir')
print(ret)  # 1

#linux系统
ret = os.system("ls") # 0
ret = os.system("ls /de/zjn")  #512 , 16进制 hex(512)="0x200",高位字节是2，低位字节是0，2是退出码

