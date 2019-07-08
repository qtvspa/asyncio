# -*- coding=utf-8 -*-
import time
import asyncio
from queue import Queue
from threading import Thread


def start_loop(loop):

    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_sleep(x, q, m=""):
    await asyncio.sleep(x)
    q.put(m)



if __name__ == '__main__':
    queue = Queue()

    new_loop = asyncio.new_event_loop()

    t = Thread(target=start_loop, args=(new_loop, ))
    t.start()

    print(time.ctime())
    # 动态添加两个协程
    # 这种方法，在主线程是异步的
    asyncio.run_coroutine_threadsafe(do_sleep(6, queue, "第一个"), new_loop)
    asyncio.run_coroutine_threadsafe(do_sleep(3, queue, "第二个"), new_loop)

    while True:
        msg = queue.get()
        print("{} 协程运行完..".format(msg))
        print(time.ctime())