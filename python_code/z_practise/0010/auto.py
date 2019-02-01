# coding=utf8
import paramiko,time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("120.26.96.231",22,"stt", "stt0707")


# 创建自己名字的目录
dirName =  "jcy"

# 先检查 是否已经存在同名目录了， 如果没有则创建
stdin, stdout, stderr = ssh.exec_command("ls")
# exec_command 返回的是bytes类型，需要解码
dircontent =  stdout.read().decode()

print(dircontent)
if dirName in dircontent.splitlines():
    print('{} already exists'.format(dirName))
else:
    print('make dir {}'.format(dirName))
    ssh.exec_command("mkdir {}".format(dirName))

# 传输文件
sftp = ssh.open_sftp()
sftp.put('memory.py', '{}/memory.py'.format(dirName))
sftp.close()


# 检查文件是否传输成功，可以将检查文件是否存在机器，做成一个函数。。。


# 执行脚本


# 考虑到长时间没有消息，网络连接可能会被断开。 到网上搜索一番后。
# 设置一个保持连接的参数
transport = ssh.get_transport()
transport.set_keepalive(30)

print('remote exec python memory.py')
ssh.exec_command("cd %s; python memory.py" % dirName)

print('wait for 30 seconds...')
time.sleep(30)


# 传输文件
sftp = ssh.open_sftp()
sftp.get('{}/ret.txt'.format(dirName),'ret.txt')
sftp.close()

ssh.close()
