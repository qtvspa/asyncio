# -*- coding=utf-8 -*-

import asyncio01
from collections.abc import Coroutine, Generator

"""
    只要在一个生成器函数头部用上 @asyncio.coroutine 装饰器
    就能将这个函数对象，【标记】为协程对象。注意这里是【标记】，划重点。
    实际上，它的本质还是一个生成器。
    标记后，它实际上已经可以当成协程使用。后面会介绍。
"""
@asyncio01.coroutine
def hello():
    yield from asyncio01.sleep(1)
    # print(f'hello {name}')


if __name__ == '__main__':
    coroutine = hello()
    print(isinstance(coroutine, Coroutine)) # False
    print(isinstance(coroutine, Generator)) # True

