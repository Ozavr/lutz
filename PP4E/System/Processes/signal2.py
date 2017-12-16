"""
установка сигналов по истечении времени ожидания и их обработка на языке Python; 
функция time.sleep некорректно ведет себя при появлении сигнала SIGALARM
(как и любого другого сигнала на моем компьютере, работающем под управлением 
Linux), поэтому здесь вызывается функция signal.pause, которая 
приостанавливает выполнение сценария до получения сигнала;
"""


import sys, signal, time


def now():
    return time.asctime()


def on_signal(signum, stackframe):
    print('Got alarm', signum, 'at', now())


while True:
    print('Setting at', now())
    signal.signal(signal.SIGALRM, on_signal)
    signal.alarm(5)
    signal.pause()