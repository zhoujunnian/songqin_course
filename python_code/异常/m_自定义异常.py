# coding=utf-8

# def  inputname():
#     name = raw_input('请输入姓名:')
#     if len(name)>10:
#         return 1,None
#     if len(name)<6:
#         return 2,None
#     return 0,name
#
# retcode, name = inputname()
# if retcode == 0:
#     print(name)
# elif retcode == 1:
#     print('太长了')
# elif retcode == 2:
#     print('太短了')



class NameTooLongError(Exception):
    pass
class NameTooShortError(Exception):
    pass



def  inputname():
    name = raw_input('请输入姓名:')
    if len(name)>10:
        raise NameTooLongError()
    if len(name)<6:
        raise NameTooShortError()
    return name

try:
    ret = inputname()
except NameTooShortError:
    print('太短了')
except NameTooLongError:
    print('太长了')


