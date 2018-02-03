"""
Отыскивает наибольший файл с исходным программным кодом на языке Python
в единственном каталоге.
Поиск выполняется в каталоге стандартной библиотеки Python для Windows, если 
в аргументе командной строки не был указан какой-то другой каталог.
"""


import os, glob, sys


dirname = r'/Users/Ozavr/Desktop/projects/lutz/env/lib/python3.5/site-packages/django/contrib/gis' if len(sys.argv) == 1 else sys.argv[1]
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')


for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])