"""
порождает дочерние процессы и получает коды их завершения вызовом функции 
os.wait; прием ветвления может использоваться в Unix и Cygwin, но он не работает 
в стандартной версии Python 3.1 для Windows;
примечание: порождаемые потоки выполнения совместно используют глобальные 
переменные, но каждый процесс имеет собственные копии этих переменных (однако 
при ветвлении процессов файловые дескрипторы используются совместно) --
exitstat здесь всегда имеет одно и то же значение, но может отличаться в случае 
использования потоков;
"""


import os


exitstat = 0


def child():
    global exitstat
    exitstat += 1
    print('Hello from child', os.getpid(), exitstat)
    os._exit(exitstat)
    print('Never reached')


def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q': break


if __name__ == '__main__':
    parent()