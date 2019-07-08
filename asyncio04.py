# -*- coding=utf-8 -*-
"""
    协程函数的嵌套
"""
import asyncio

# 用于内部的协程函数
async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    dones, pendings = await asyncio.wait(tasks)
    for done in dones:
        print(done.result())

    # 另一种方法
    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print('Task ret: ', result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())