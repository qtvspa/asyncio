# -*- coding:utf-8 -*-

import threading
import time

num = 1
t_obj = []
start_time = time.time()
event = threading.Event()


def run():
    global num
    num = num * 2


for i in range(50):

    t = threading.Thread(target=run)
    t.start()
    t_obj.append(t)


for i in t_obj:
    i.join()
    # print(num)


def light():
    count = 0
    event.set()  # 对标志进行设置
    while True:
        if 3 < count <= 5:
            event.clear()  # 清除标志的设置
            print('Red light')
        elif count > 5:
            event.set()
            print('Green light')
            count = 0
        else:
            print ('runing....')
        count += 1


def car(name):
    while True:
        if event.is_set():  # 判断是否被标志
            print(f'car{name}is run.....')
        else:
            print(f'car{name}is wait.....')
            event.wait()  # 等待标志被设置


if __name__ == '__main__':

    # print(t_obj)
    l1 = threading.Thread(target=light)
    l1.start()
    c1 = threading.Thread(target=car, args='123')
    c1.start()
