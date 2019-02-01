import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")


stdin, stdout, stderr = ssh.exec_command("date +%Y%m%d_%H%M%S;free")

print(stdout.read())
ssh.close()
