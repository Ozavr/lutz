"""
именованные каналы; функция os.mkfifo недоступна в Windows (без Cygwin); 
здесь нет необходимости использовать прием ветвления процессов, потому что 
файлы каналов fifo являются внешними по отношению к процессам -- совместное 
использование дескрипторов файлов в родителе/потомке здесь неактуально;
"""


import os, time, sys


fifoname = '/tmp/pipefifo'


def child():
    pipeout = os.open(fifoname, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein = open(fifoname, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got %s at %s' % (os.getpid(), line, time.time()))


if __name__ == '__main__':
    if not os.path.exists(fifoname):
        os.mkfifo(fifoname)
    if len(sys.argv) == 1:
        parent()
    else:
        child()