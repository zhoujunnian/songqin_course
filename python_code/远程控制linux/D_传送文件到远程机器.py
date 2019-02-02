import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")


sftp = ssh.open_sftp()
sftp.put('D_传送文件到远程机器.py', '/home/stt/D_传送文件到远程机器.py')
sftp.close()

ssh.close()
