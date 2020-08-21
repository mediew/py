from multiprocessing import Process, Queue
import os, time, random

"""
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
"""


# 写数据进程执行的代码
def write(q):
    print('Process %s to write' % os.getpid())
    for i in ['A', 'B', 'C']:
        q.put(i)
        print('Put %s to queue' % i)
        time.sleep(random.random())


# 读数据进程执行的代码
def read(q):
    print('Process %s to read' % os.getpid())
    while True:
        value = q.get(True)
        print('Read %s from queue' % value)


if __name__ == '__main__':
    q = Queue()  # 创建用于进程间通信的通道对象Queue
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))  # 注意args必须传入Iterable，单个元素的tuple必须加逗号
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()  # pr进程是死循环需手动终止
