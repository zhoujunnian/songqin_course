import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")

ssh.exec_command("pwd")
ssh.exec_command("mkdir jcy3")
ssh.exec_command("cd jcy3")
stdin, stdout, stderr = ssh.exec_command("pwd")
print(stdout.read())

ssh.close()
