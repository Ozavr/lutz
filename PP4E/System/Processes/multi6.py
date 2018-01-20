"""
Плюс многое другое: пулы процессов, менеджеры, блокировки, 
условные переменные,.
"""


import os
from multiprocessing import Pool


def power(x):
    print(os.getppid())
    return 2 ** x


if __name__ == '__main__':
    workers = Pool(processes=5)

    results = workers.map(power, [2] * 100)
    print(results[:16])
    print(results[-2:])

    results = workers.map(power, range(100))
    print(results[:16])
    print(results[-2:])