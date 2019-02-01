# coding=utf8
import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()

# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器  地址、端口、用户名密码
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")

# # 创建目录
# cmd = 'mkdir aaaaaaaaaaaaaaa'
# ssh.exec_command(cmd)

# 如果命令跨行
cmd = '''echo '1234
5678
90abc' > myfile
'''
ssh.exec_command(cmd)


# 获取命令的执行结果
cmd = 'free'
stdin, stdout, stderr = ssh.exec_command(cmd)
memInfo = stdout.read()


print memInfo.splitlines()[2]

ssh.close()