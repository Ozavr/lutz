"""
Порядок использования: “python ...\Tools\visitor_edit.py string rootdir?”. 
Добавляет подкласс класса SearchVisitor, который автоматически запускает 
текстовый редактор. 
В процессе обхода автоматически открывает в текстовом редакторе файлы, 
содержащие искомую строку; 
в Windows можно также использовать editor=’edit’ или ‘notepad’; 
чтобы воспользоваться текстовым редактором, реализация которого будет 
представлена далее в книге, попробуйте 
r’python Gui\ TextEditor\textEditor.py’; при работе с некоторыми 
редакторами можно было бы передать команду перехода к первому совпадению 
с искомой строкой;
"""


import os, sys
from visitor import SearchVisitor


class EditVisitor(SearchVisitor):
    """
    открывает для редактирования файлы, содержащие искомую строку и 
    находящиеся в каталоге startDir и ниже
    """
    editor = r'/Applications/Sublime\ Text.app/Contents/MacOS/Sublime\ Text'

    def visitmatch(self, fpathname, text):
        os.system('%s %s' % (self.editor, fpathname))


if __name__ == '__main__':
    visitor = EditVisitor(sys.argv[1])
    visitor.run('.' if len(sys.argv) < 3 else sys.argv[2])
    print('Edited %d files, visited %d' % (visitor.scount, visitor.fcount))