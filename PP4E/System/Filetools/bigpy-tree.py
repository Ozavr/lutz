"""
Отыскивает наибольший файл с исходным программным кодом на языке Python в дереве 
каталогов.
Поиск выполняется в каталоге стандартной библиотеки, отображение результатов 
выполняется с помощью модуля pprint.
"""


import os, sys, pprint


trace = False


# if sys.platform.startswith('win'):
#     dirname = r'C:\Python31\Lib'
# else:
#     dirname = '/usr/lib/python'

dirname = '/Users/Ozavr/Desktop/projects/lutz/env/lib/python3.5'

allsizes = []

for (thisDir, subsHere, filesHere) in os.walk(dirname):
    if trace:
        print(thisDir)
    for filename in filesHere:
        if filename.endswith('.py'):
            if trace:
                print('...', filename)
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
