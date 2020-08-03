# -*- coding: utf-8 -*-
#问题：测试程序执行时间
import time, functools
#我的作业
'''
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1=time.time()
        result=fn(*args,**kw)
        t2=time.time()
        print('%s executed in %s ms' % (fn.__name__, (t2-t1)*1000))
        return result
    return wrapper
'''
#当装饰器需要接受text时
#'''
def log(text):
    def metric(fn):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            print('Start to execute %s' % (fn.__name__))
            print(text)
            t1=time.time()
            result=fn(*args,**kw)
            t2=time.time()
            print('%s executed in %s ms' % (fn.__name__, (t2-t1)*1000))
            return result
        return wrapper
    return metric
#'''
# 测试1(不接受text)
'''
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
'''
#测试2（接受text）

@log('hello,world!')
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log('hello,world!')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
