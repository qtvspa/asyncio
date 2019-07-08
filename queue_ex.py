# -*- coding:utf-8 -*-

from threading import local, Thread, current_thread

local_data = local()
local_data.name = 'local_data'


class MyThread(Thread):

    def run(self):
        print('before the assignment(child thread): ', current_thread(), local_data.__dict__)

        local_data.name = self.getName()
        print('after the assignment(child thread): ', current_thread(), local_data.__dict__)


if __name__ == '__main__':

    print('before-main: ', local_data.__dict__)

    t1 = MyThread()
    t1.start()
    t1.join()

    t2 = MyThread()
    t2.start()
    t2.join()

    print('after-main: ', local_data.__dict__)
