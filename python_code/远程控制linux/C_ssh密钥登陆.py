# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "zhoujunjun"

import paramiko
from config import password,username,private_key_file,hostname


private_key = paramiko.RSAKey.from_private_key_file(private_key_file, password=password)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=hostname, port=32200, username=username, pkey=private_key)

stdin, stdout, stderr = ssh.exec_command('pwd')

result = stdout.read()
print(result.decode())
ssh.close()



# keyfile = os.path.expanduser('~/.ssh/id_rsa')
# password = keyring.get_password('SSH', keyfile)
# key = paramiko.RSAKey.from_private_key_file(keyfile, password=password)