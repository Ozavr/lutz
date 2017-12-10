"""
тоже сокет, но теперь для общения независимых программ, а не только потоков 
выполнения; сервер в этом примере обслуживает клиентов, выполняющихся в виде 
отдельных процессов и потоков; сокеты, как и именованные каналы, являются 
глобальными для компьютера: для их использования не требуется совместно 
используемая память
"""


from socket_preview import server, client
import sys, os
from threading import Thread


mode = int(sys.argv[1])
if mode == 1:
    server()
elif mode == 2:
    client('client:process=%s' % os.getpid())
else:
    for i in range(5):
        Thread(target=client, args=('client:thread=%s' % i,)).start()