"""
запускает параллельно 10 копий child.py; для запуска программ в Windows 
использует spawnv (как fork+exec); флаг P_OVERLAY обозначает замену, 
флаг P_DETACH перенаправляет stdout потомка в никуда; можно также 
использовать переносимые инструменты из модуля subprocess 
или из пакета multiprocessing!
"""


import os, sys


for i in range(10):
    if sys.platform[:3] == 'win':
        pypath = sys.executable
        os.spawnv(os.P_NOWAIT, pypath, ('python', 'child.py', str(i)))
    else:
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            os.execlp('python', 'python', 'child.py', str(i))

print('Main process exiting')