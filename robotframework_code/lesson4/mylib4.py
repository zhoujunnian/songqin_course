import os
import requests
import winsound

def printarg(*args,**kwargs):
    if len(args) == 0:
        print('** no args **')
    else:
        print('** args are **')
        print('-----------------')
        for one in args:
            print(repr(one))
        print('-----------------')

    if len(kwargs) == 0:
        print('** no kwargs **')
    else:
        print('** kwargs are **')
        print('-----------------')
        for k,v in kwargs.items():
            print(repr(k) + ':' + repr(v))
        print('-----------------')




def opencalc():
    os.system('calc')



def returnlist():
    print('** in return list ** hello')
    return [1,2,3]

def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }


def getWebInfo():
    response = requests.get(
        'http://mirrors.sohu.com/centos/timestamp.txt')
    return response.text


def  beep():
    winsound.Beep(1500, 3000)  # freqency and duration