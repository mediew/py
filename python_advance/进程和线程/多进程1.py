import os
import random
import time
from multiprocessing import Process, Pool


# 1.multiprocessing是跨平台的多进程工具，multiprocessing模块提供了一个Process类来代表一个进程对象
def run_proc(name):
    print('Child process %s (PID:%s)starts!' % (name, os.getpid()))


# 创建一个进程对象
if __name__ == '__main__':
    print('Parent process (PID:%s) starts' % os.getpid())
    p = Process(target=run_proc, args=('test',))          # args要求为一个Iterable，一定要加逗号隔开，否则将test'识别为4个参数
    print('Child process will start!')
    p.start()
    p.join()        # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process stops!')


# 2.如果要启动大量的子进程，可以用进程池(Pool)的方式批量创建子进程
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process starts!')
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for all subprocess done!')
    p.close()
    p.join()
    print('All subprocesses done.')
