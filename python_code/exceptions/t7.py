try:
    ohmy
    b = 4/0
    print('hello')
except ZeroDivisionError:
    print('handle ZeroDivisionError')
except NameError:
    print('handle NameError')
except :
    print('handle unkown exeption')
finally:
    print('in finally')



