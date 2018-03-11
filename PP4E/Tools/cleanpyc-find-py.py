"""
отыскивает и удаляет все файлы “*.pyc” с байт-кодом в дереве каталогов, имя 
которого передается в виде аргумента командной строки;
использует утилиту find, написанную на языке Python, за счет чего 
обеспечивается переносимость;
запустите этот сценарий, чтобы удалить файлы .pyc, скомпилированные старой 
версией Python;
"""


import os, sys, find


count = 0
for filename in find.find('*.pyc', sys.argv[1]):
    count += 1
    print(filename)
    os.remove(filename)

print('Removed %d .pyc files' % count)