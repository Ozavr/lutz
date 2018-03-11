"""
удаляет все файлы .pyc с байт-кодом в дереве каталогов: аргумент командной 
строки, если он указан, интерпретируется как корневой каталог, в противном 
случае корневым считается текущий рабочий каталог
"""


import os, sys


findonly = False
if len(sys.argv) == 1:
    rootdir = os.getcwd()
else:
    rootdir = sys.argv[1]


found = removed = 0


for (thisDirLevel, subsHere, filesHere) in os.walk(rootdir):
    for filename in filesHere:
        if filename.endswith('.pyc'):
            fullname = os.path.join(thisDirLevel, filename)
            print('=>', fullname)
            if not findonly:
                try:
                    os.remove(fullname)
                    removed += 1
                except:
                    type, inst = sys.exc_info()[:2]
                    print('*' * 4, 'Failed:', filename, type, inst)
            found += 1

print('Found', found, 'files, removed', removed)
