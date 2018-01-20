"""
От класса Process можно породить подкласс, так же, как от класса threading. 
Thread;
объект Queue действует подобно queue.Queue, но обеспечивает обмен данными между 
процессами, а не между потоками выполнения
"""


import os, time, queue
from multiprocessing import Process, Queue


class Counter(Process):
    label = ' @'

    def __init__(self, start, queue):
        self.state = start
        self.post = queue
        Process.__init__(self)

    def run(self):
        for i in range(3):
            time.sleep(1)
            self.state += 1
            print(self.label, self.pid, self.state)
            self.post.put([self.pid, self.state])





if __name__ == '__main__':
    print('start', os.getpid())
    excepted = 9

    post = Queue()
    p = Counter(0, post)
    q = Counter(100, post)
    r = Counter(1000, post)
    p.start(); q.start(); r.start()

    while excepted:
        time.sleep(0.5)
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('no data...')
        else:
            print('posted:', data)
            excepted -= 1

    p.join(); q.join(); r.join();
    print('finish', os.getppid(), r.exitcode)