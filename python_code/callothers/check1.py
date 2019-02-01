import subprocess

# shell=True表示使用终端shell执行程序,windows下面就是cmd.exe
# 就是我们python程序调用cmd.exe 再由cmd.exe 执行 参数命令
ret = subprocess.check_output('dir', shell=True, encoding='gbk')

# 如果有中文，需要decode，因为是中文os，所以cmd.exe输出是gbk编码
print(ret)
# print(ret.decode('gbk'))

