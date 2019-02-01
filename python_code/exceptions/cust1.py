class NameTooLongError(Exception):
    pass
class NameTooShortError(Exception):
    pass



def  inputname():
    name = input('请输入姓名:')
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


