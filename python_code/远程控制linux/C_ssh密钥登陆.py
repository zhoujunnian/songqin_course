# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "zhoujunjun"

import paramiko
import keyring

password = 'Aa0789351318'
private_key = paramiko.RSAKey.from_private_key_file(r'/Users/zhoujunjun/.ssh/id_rsa_saqa', password=password)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.82.51.10', port=32200, username="wb.zhoujunnian", pkey=private_key,  allow_agent=False)

stdin, stdout, stderr = ssh.exec_command('pwd')

result = stdout.read()
print(result.decode())
ssh.close()



# keyfile = os.path.expanduser('~/.ssh/id_rsa')
# password = keyring.get_password('SSH', keyfile)
# key = paramiko.RSAKey.from_private_key_file(keyfile, password=password)