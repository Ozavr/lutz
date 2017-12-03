"""
аналогичен сценарию pipe1.py, но обертывает входной дескриптор канала 
объектом файла для обеспечения построчного чтения данных,
и в обоих процессах закрывает неиспользуемый дескриптор канала
"""


import os, time


def child(pipout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Span %03d\n' % zzz).encode()
        os.write(pipout, msg)
        zzz = (zzz + 1) % 5


def parent():
    pipein, pipeout = os.pipe()
    if os.fork() == 0:
        os.close(pipein)
        child(pipeout)
    else:
        os.close(pipeout)
        pipein = os.fdopen(pipein)
        while True:
            line = pipein.readline()[:-1]
            print('Parent %d got [%s] at %s' % (os.getpid(), line, time.time()))


parent()