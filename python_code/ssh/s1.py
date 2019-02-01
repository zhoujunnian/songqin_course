import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("120.26.96.231",22,"stt", "stt")
stdin, stdout, stderr = ssh.exec_command("free")
print(stdout.read())
ssh.close()
input()