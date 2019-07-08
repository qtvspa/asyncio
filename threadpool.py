# -*- coding=utf-8 -*-

import time
import threading
from concurrent.futures import ThreadPoolExecutor


def target():
    for i in range(5):
        print(f'running thread-{threading.get_ident()}:{i}')
        time.sleep(1)


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)

    for i in range(100):
        pool.submit(target)