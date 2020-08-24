import time


# time模块的计时函数


def f():
    pass


start = time.perf_counter()
f()
stop = time.perf_counter()
t = stop - start
