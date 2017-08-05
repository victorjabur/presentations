from multiprocessing import Process
import multiprocessing
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':

    #spawn (windows - fresh process - slow) / fork (unix - identical parent) / forkserver
    multiprocessing.set_start_method('spawn')

    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
