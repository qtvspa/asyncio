# -*- coding=utf-8 -*-

import asyncio


async def hello2(name):
    print(f'hello {name}')


if __name__ == '__main__':

    # 定义协程对象
    coroutine = hello2("World")

    # 定义事件循环对象容器
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine)

    # 将协程转为task任务
    task = loop.create_task(coroutine)

    # 将task任务扔进事件循环对象中并触发
    loop.run_until_complete(task)
