"""
############################################################################## 
объединяет все файлы фрагментов, имеющиеся в каталоге и созданные с помощью 
сценария split.py,воссоздавая первоначальный файл.
По своему действию этот сценарий напоминает команду ‘cat fromdir/* > tofile’
в Unix, но данная реализация более переносимая и настраиваемая; 
сценарий экспортирует операцию объединения в виде функции, доступной для 
многократного использования. 
Зависит от порядка сортировки имен файлов, поэтому все они должны быть 
одинаковой длины. 
Сценарии разрезания/объединения можно дополнить возможностью вывода диалога с 
графическим интерфейсом tkinter, позволяющего выбирать файлы. 
##############################################################################
"""


import os, sys


readsize = 1024


def join(fromdir, tofiles):
    output = open(tofile, 'wb')
    parts = os.listdir(fromdir)
    parts.sort()
    for filename in parts:
        filepath = os.path.join(fromdir, filename)
        fileobj = open(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            if not filebytes: break
            output.write(filebytes)
        fileobj.close()
    output.close()


if __name__ == '__main__':
    if (len(sys.argv) == 2) and (sys.argv[1] == '-help'):
        print('Use: join.py [from-dir-name to-file-name]')
    else:
        if len(sys.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile = input('Name of file to be recreated? ')
        else:
            interactive = False
            fromdir, tofile = sys.argv[1:]
        absfrom, absto = map(os.path.abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        try:
            join(fromdir, tofile)
        except:
            print('Error joining files:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        else:
            print('Join complete: see', absto)
        
        if interactive:
            input('Press Enter key')