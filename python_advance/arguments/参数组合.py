# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。

'''
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
# 顺序一：必选参数、默认参数、可变参数、关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# 顺序二：必选参数、默认参数、命名关键字参数、关键字参数
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2) # 分别为前两个位置参数
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, 3, 'city', key='value')
# a = 1 b = 2 c = 3 args = ('city',) kw = {'key': 'value'}
f2(1, 2, 4, d='dady', key='value')
# a = 1 b = 2 c = 4 d = dady kw = {'key': 'value'}
# 通过一个tuple和dict，你也可以调用上述函数,但变量前要加上函数定义时的*，**
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
# a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}   # 注意命名关键字参数不能写在可变参数组成的tuple里，因其含有Python关键字‘=’，故只能和关键字参数共同组成dict
f2(*args, **kw)
# a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

# 练习题：可接收一个或多个数并计算乘积
def product(x, *y):
    for i in y:
        x = x * i
    print(x, y)
    return x

product(2, 3)
# 6 (3,)
print(product())
# TypeError: product() missing 1 required positional argument: 'x'