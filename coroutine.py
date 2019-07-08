# -*- coding=utf-8 -*-

from collections.abc import Coroutine

def jumping_range(n):
    index = 0
    while index < n:
        # 通过send()发送的信息将赋值给jump
        jump = yield index
        # yield index 是将index return给外部调用程序
        # jump = yield 可以接收外部程序通过send()发送的信息，并赋值给jump
        if jump is None:
            jump = 1
        index += jump

async def hello(name):
    print(f'{name}')

if __name__ == '__main__':
    # itr = jumping_range(5)
    # print(next(itr))
    # print(itr.send(2))
    # print(next(itr))
    # print(itr.send(-1))
    h = hello('123')
    print(isinstance(h, Coroutine))