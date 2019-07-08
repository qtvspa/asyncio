# -*- coding=utf-8 -*-

# 子生成器
def average_gen():
    total, count, average = 0, 0, 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total/count


# 委托/代理生成器(在调用方与子生成器之间建立一个双向通道)
def proxy_gen():
    while True:
        yield from average_gen()


# 调用方
if __name__ == '__main__':

    a = proxy_gen()
    next(a)
    print(a.send(10))
    print(a.send(20))
    print(a.send(30))
