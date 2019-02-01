import os
import urllib2
import winsound

def opencalc():
    os.system('calc')



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








def returnlist():
    print('** in return list ** hello')
    return [1,2,3]

def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }


def getWebInfo():
    response = urllib2.urlopen('http://mirrors.sohu.com/centos/timestamp.txt')
    html = response.read()
    return html


def  beep():
    winsound.Beep(1500, 3000)  # freqency and duration