# !/usr/bin/python开发
# -*- coding:utf-8 -*-
__author__ = "zhoujunjun"
#
import paramiko
import time
from detect_config import password,username,private_key_file,hostname,root_pwd

private_key = paramiko.RSAKey.from_private_key_file(private_key_file, password=password)

# 这个方法不能切换到root
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# ssh.connect(hostname=hostname[1], port=32200, username=username, pkey=private_key)
#
# stdin, stdout, stderr = ssh.exec_command('pwd')
# result = stdout.read()
# print(result.decode()+stderr.read())
# ssh.close()

# 切换到root，然后再执行命令
def verification_ssh(cmd):
    s=paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname[1], port=32200, username=username, pkey=private_key)
    if username != 'root':
        ssh = s.invoke_shell()
        time.sleep(0.1)
        ssh.send('su - \n')
        buff = ''
        while not buff.endswith('Password: '):      # 输入su - 后，buff变量以''进入循环，以'Password'结尾，退出循环
            resp = ssh.recv(9999)   # .recv(bufsize)通过recv函数获取shell终端的输出显示
            print(resp.decode('utf8'))      # resp 返回的是byte格式，要用decode解码
            buff += resp.decode('utf8')     # 解码后再和 '' 相加，重新赋值给buff
        ssh.send(root_pwd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            print(resp)
            buff += resp.decode('utf8')
        ssh.send(cmd)
        ssh.send('\n')
        buff = ''
        while not buff.endswith('# '):
            resp = ssh.recv(9999)
            buff += resp.decode('utf8')
        s.close()
        result = buff
    else:
        stdin, stdout, stderr = s.exec_command(cmd)
        result = stdout.read()
        print(result.decode() + stderr.read())
        s.close()
    return result
a = verification_ssh('pwd;cd /home/wb.zhangxiaojun/detect/detect-server;''pwd;'       # 以分号分隔为一个命令,可以一个引号里面分隔，也可以多个引号之间分隔
                     'bash update_detect.sh master master;'
                     'docker ps -a')
print (a)