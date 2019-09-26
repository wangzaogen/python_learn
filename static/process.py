from multiprocessing import Process
import os

def add():
    print('run child process %d' % os.getpid())
    print(1+2)
    return 3

if __name__=='__main__':
    print(' parent process is,%d' % os.getpid())
    p = Process(target=add)
    p.start()
    p.join()
    print('Child process end.')

