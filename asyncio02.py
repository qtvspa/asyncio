# -*- coding=utf-8 -*-

import asyncio
import time

async def _sleep(x):
    time.sleep(x)
    return f'暂停了{x}秒！'

def callback(future):
    print(f'这里是回调函数，获取返回结果是：{future.result()}' )


if __name__ == '__main__':
    coroutine = _sleep(1)

    loop = asyncio.get_event_loop()

    task = asyncio.ensure_future(coroutine)
    task.add_done_callback(callback)
    loop.run_until_complete(task)

    # print(f'返回结果：{task.result()}')
