import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")


stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.read()


sftp = ssh.open_sftp()
sftp.put('ftp1.py', '/home/stt/ftp1.py')

sftp.get('aaa.tar', 'e:/aaa.tar')
sftp.close()

stdin, stdout, stderr = ssh.exec_command("free")
print stdout.read()


ssh.close()
