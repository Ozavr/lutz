"""
Основы ветвления: запустить 5 копий этой программы параллельно оригиналу; каждая 
копия считает до 5 и выводит счетчик в тот же поток stdout -- при ветвлении 
копируется память процесса, в том числе дескрипторы файлов; в настоящее время 
ветвление не действует в Windows без Cygwin: запускайте программы в Windows
с помощью функции os.spawnv или пакета multiprocessing; функция spawnv примерно 
соответствует комбинации функций fork+exec;
"""


import os, time


def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting')