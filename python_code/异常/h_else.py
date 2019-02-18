try:
    #sdfsdf
    print('do something')
except ZeroDivisionError:
    print('handle ZeroDivisionError')
except NameError:
    print('handle NameError')
except :
    print('handle unkown exeption')
else:
    print('haha, no exception')
finally:
    print('in finally')



