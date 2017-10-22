"""
запускает программы, пока не будет нажата клавиша ‘q’
"""

import os


param = 0
while True:
    param += 1
    pid = os.fork()
    if pid == 0:
        os.execlp('python', 'python', 'child.py', str(param))
        assert False, 'error starting program'

    else:
        print('Child is', pid)
        if input() == 'q': break