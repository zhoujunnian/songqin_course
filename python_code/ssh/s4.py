import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")


stdin, stdout, stderr = ssh.exec_command("pwd;mkdir jcy4;cd jcy4;pwd;mkdir jcy44")

print(stdout.read())
ssh.close()


