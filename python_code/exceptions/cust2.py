def  inputname():
    name = input('请输入姓名:')
    if len(name)>10:
        return 1,None
    if len(name)<6:
        return 2,None
    return 0,name

retcode, name = inputname()
if retcode == 0:
    print(name)
elif retcode == 1:
    print('太长了')
elif retcode == 2:
    print('太短了')
