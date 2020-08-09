def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
'''
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
调用函数f时，才真正计算求和的结果：
>>> f()
25
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
f1()和f2()的调用结果互不影响。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：
>>> f1()
9
>>> f2()
9
>>> f3()
9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f())
    return fs

f1, f2, f3 = count()
print(f1, f2, f3)

# 定义一个递增的计数器：
def createCounter():
    c = 0
    def counter():
        nonlocal c
        c = c + 1
        return c
    return counter
# 闭包函数引用的是外部函数绑定来的临时变量。要修改外部函数变量需要用nonlocal来声明变量是上层空间的变量，从而改变外部函数变量的值。

def createCounter():
    c = []
    def counter():
        c.append('whatever')
        return len(c)
    return counter
# 如果闭包函数引用的外部函数变量是可变数据类型，就可以在闭包函数中改变外部函数的变量值。
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')