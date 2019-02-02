# coding=utf-8
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.211.55.9", port=22, username="zjn", password="Aa0789351318")

ssh.exec_command("pwd")
ssh.exec_command("mkdir jcy3")
ssh.exec_command("cd jcy3")
stdin, stdout, stderr = ssh.exec_command("pwd")

# exec_command 执行远程命令，每次执行命令都会新打开一个channel执行，新的环境不在上次执行的环境里面，
# 所以，我们不能在上次命令的结果，再调用，不能达到多次执行的目的，解决方法是：
# 可以多个命令一起执行，用分号隔开
stdin1, stdout1, stderr1 = ssh.exec_command("pwd;mkdir jcy4;cd jcy4;pwd;mkdir jcy44")

print(stdout.read())
print(stdout1.read())

ssh.close()
