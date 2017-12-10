"""
использует сокеты для обмена данными между заданиями: запускает потоки 
выполнения, взаимодействующие с помощью сокетов; независимые программы также 
могут использовать сокеты для взаимодействий, потому что они принадлежат
системе в целом, как и именованные каналы; смотрите части книги, посвященные 
разработке графических интерфейсов и сценариев для Интернета, где приводятся 
более практичные примеры использования сокетов; некоторым серверам может 
потребоваться взаимодействовать через сокеты с клиентами в виде потоков 
выполнения и процессов; данные через сокеты передаются в виде строк байтов, но 
точно так же через них можно передавать сериализованные объекты или кодированный 
текст Юникода;
ВНИМАНИЕ: при обращении к функции print в потоках выполнения может потребоваться 
синхронизировать их, если есть вероятность перекрытия по времени;
"""


from socket import socket, AF_INET, SOCK_STREAM


port = 5008
host = 'localhost'


def server():
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        reply = 'Server got: [%s]' % data
        conn.send(reply.encode())


def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send(name.encode())
    reply = sock.recv(1024)
    sock.close()
    print('Client got: [%s]' % reply)


if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True
    sthread.start()
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()