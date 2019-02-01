import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("ci.ytesting.com",22,"stt", "stt0707")

sftp = ssh.open_sftp()
sftp.get('/home/stt/hello', 'd:/myfile1.txt')
sftp.close()


ssh.close()
