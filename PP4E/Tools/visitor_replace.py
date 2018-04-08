"""
Использование: “python ...\Tools\visitor_replace.py rootdir fromStr toStr”. 
Выполняет глобальный поиск с заменой во всех файлах в дереве каталогов: 
заменяет fromStr на toStr во всех текстовых файлах; 
это мощный, но опасный инструмент!! 
visitor_edit.py запускает редактор, чтобы дать возможность проверить и 
внести коррективы, и поэтому он более безопасный; 
чтобы просто получить список соответствующих файлов, используйте 
visitor_collect.py; 
режим простого вывода списка здесь напоминает SearchVisitor и 
CollectVisitor;
"""


import sys
from visitor import SearchVisitor


class ReplaceVisitor(SearchVisitor):
    """
    Заменяет fromStr на toStr в файлах в каталоге startDir и ниже; 
    имена изменившихся файлов сохраняются в списке obj.changed
    """

    def __init__(self, fromStr, toStr, listOnly=False, trace=0):
        self.changed = []
        self.toStr = toStr
        self.listOnly = listOnly
        SearchVisitor.__init__(self, fromStr, trace)

    def visitmatch(self, fname, text):
        self.changed.append(fname)
        if not self.listOnly:
            fromStr = self.context
            toStr = self.toStr
            text = text.replace(fromStr, toStr)
            open(fname, 'w').write(text)


if __name__ == '__main__':
    listonly = input('List only?') == 'y'
    visitor = ReplaceVisitor(sys.argv[2], sys.argv[3], listonly)
    if listonly or input('Proceed with changes?') == 'y':
        visitor.run(startDir=sys.argv[1])
        action = 'Changed' if not listonly else 'Found'
        print('Visited %d files' % visitor.fcount) 
        print(action, '%d files:' % len(visitor.changed)) 
        for fname in visitor.changed: print(fname)