"""
Вывод списка файлов в дереве каталогов с помощью os.walk
"""

import os, sys


def lister(root):
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('[' + thisdir + ']')
        for fname in fileshere:
            path = os.path.join(thisdir, fname)
            print(path)


if __name__ == '__main__':
    lister(sys.argv[1])
