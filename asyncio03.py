# -*- coding=utf-8 -*-
"""
    协程函数的并发
"""
import asyncio

# 协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

# 协程对象
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

# 将协程转成task，并组成list
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    # 另一种方法
    # loop.run_until_complete(asyncio.gather(*tasks))
    for task in tasks:
        print(task.result())