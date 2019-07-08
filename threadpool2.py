# -*- coding=utf-8 -*-
import time
import threading
from queue import Queue


def target(q):
    while True:
        msg = q.get()
        for i in range(5):
            print(f'running thread-{threading.get_ident()}:{i}')
            time.sleep(1)

def pool(workers, queue):
    for n in range(workers):
        t = threading.Thread(target=target, args=(queue, ))
        t.daemon = True
        t.start()


if __name__ == '__main__':
    queue = Queue()
    pool(5, queue)

    for i in range(30):
        queue.put('start')

    queue.join()