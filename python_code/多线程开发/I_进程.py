from multiprocessing import Process,Pool
import os,time

def proc1_entry(name):
    print ('Run child process 1: %s (%s)...' % (name, os.getpid()))
    time.sleep(30)

def proc2_entry(name):
    print ('Run child process 2: %s (%s)...' % (name, os.getpid()))
    time.sleep(30)

if __name__=='__main__':
    print ('Parent process %s.' % os.getpid())
    p1 = Process(target=proc1_entry, args=('p1',))
    p2 = Process(target=proc2_entry, args=('p2',))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print ('Process end.')