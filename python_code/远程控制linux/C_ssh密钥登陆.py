# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "zhoujunjun"

import paramiko
import keyring


private_key = paramiko.RSAKey.from_private_key_file(r'', password=password)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='', port=32200, username="", pkey=private_key)

stdin, stdout, stderr = ssh.exec_command('pwd')

result = stdout.read()
print(result.decode())
ssh.close()



# keyfile = os.path.expanduser('~/.ssh/id_rsa')
# password = keyring.get_password('SSH', keyfile)
# key = paramiko.RSAKey.from_private_key_file(keyfile, password=password)