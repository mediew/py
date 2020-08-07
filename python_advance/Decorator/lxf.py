def now():
    print('2020-8-7')

now()
# 2020-8-7
print(now.__name__)
# now
# 定义一个装饰器，打印函数名称
def log(func):
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2020-8-7')

now()
'''
call now()
2020-8-7
'''
print(now.__name__)
# wrapper
'''
函数也是对象，它有__name__等属性，但经过decorator装饰之后的函数，它们的__name__已经从原来的'now'
变成了'wrapper';因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性
复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
'''
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
# functools.wraps也是一个装饰器，把func的属性赋给要装饰的函数

# 如果是针对带参数的decorator：
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('装饰后的函数')
def product(x, *args):
    for i in args:
        x = x * i
    print(x)

product(1)
print(product.__name__)
'''
装饰后的函数 product():
1
product
'''