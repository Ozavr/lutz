"""
Реализует взаимодействие с помощью объектов разделяемой памяти из пакета.
В Windows передаваемые объекты используются совместно, а глобальные объекты
 - нет. Последняя проверка здесь отражает типичный случай использования: 
 распределение заданий между процессами.
"""


import os
from multiprocessing import Process, Value, Array


procs = 3
count = 0


def showdata(label, val, arr):
    """
    выводит значения данных в этом процессе
    """
    msg = '%-12s: pid:%4s, global:%s, value:%s, array:%s'
    print(msg % (label, os.getppid(), count, val.value, list(arr)))


def updater(val, arr):
    """
    обменивается данными через разделяемую память
    """
    global count
    count += 1
    val.value += 1
    for i in range(3):
        arr[i] += 1


if __name__ == '__main__':
    scalar = Value('i', 0)
    vector = Array('d', procs)

    showdata('parent start', scalar, vector)

    p = Process(target=showdata, args=('child', scalar, vector))
    p.start(); p.join()

    # изменить значения в родителе и передать через разделяемую память,
    # ждать завершения каждого потомка
    # все потомки видят изменения, выполненные в родительском процессе и
    # переданные ввиде аргументов (но не в глобальной памяти)

    print('\nloop1 (updates in parent, serial children)...')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start(); p.join()


    print('\nloop2 (updates in parent, parallel children)...')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=(('process %s' % i), scalar, vector))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    # объекты в разделяемой памяти изменяются потомками,
    # ждать завершения каждого из них

    print('\nloop3 (updates in serial children)...')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
        showdata('parant temp', scalar, vector)

    # то же самое, но потомки запускаются параллельно
    print('‘\nloop4 (updates in parallel children)...’')
    ps = []
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    showdata('parent end', scalar, vector)





