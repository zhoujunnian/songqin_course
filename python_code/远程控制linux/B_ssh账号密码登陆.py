# coding=utf8
import paramiko

# 创建SSHClient 实例对象
ssh = paramiko.SSHClient()  

# 调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程机器  地址、端口、用户名密码
ssh.connect(hostname="10.211.55.9", port=22, username="zjn", password="Aa0789351318")

# 创建目录
cmd1 = 'mkdir zjn3'
ssh.exec_command(cmd1)

# 如果命令跨行
cmd2 = '''echo '1234
5678
90abc' > myfile
'''
ssh.exec_command(cmd2)

# 获取命令的执行结果
cmd4 = 'cat myfile'
stdin, stdout, stderr = ssh.exec_command(cmd4)
print(stdout.read()+ stderr.read())

cmd = "date +%Y%m%d_%H%M%S;free"
stdin, stdout, stderr = ssh.exec_command(cmd)
memInfo = stdout.read()
print [memInfo.splitlines()[0],memInfo.splitlines()[2]]


ssh.close()

"""
stdin,显示输入的信息
stdout,显示输出的信息
stderr,显示错误信息
是文件对象，用read()可以读取出来
"""
