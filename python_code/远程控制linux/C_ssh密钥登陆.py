# !/usr/bin/python
# -*- coding:utf-8 -*-
__author__ = "zhoujunjun"

import paramiko

private_key = paramiko.RSAKey.from_private_key_file(r'/Users/zhoujunjun/.ssh/id_rsa_saqa')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='10.82.51.10', port=32200, username="wb.zhoujunnian", pkey=private_key)

stdin, stdout, stderr = ssh.exec_command('ifconfig')

result = stdout.read()
print(result.decode())
ssh.close()
