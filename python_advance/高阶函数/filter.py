"""
filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
故Python内建的filter()函数用于过滤序列。
s[::-1]为字符串的reverse操作！
"""


# 删掉空字符串
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']

# 计算素数的一个方法是埃氏筛法
def primes():
    yield 2
    # 定义一个从3开始的奇数数列
    def _odd_iter():
        n = 1
        while True:
            n += 2
            yield n
    iter = _odd_iter()
    def filter_iter(n):
        return lambda x: x % n != 0
    while True:
        n = next(iter)
        yield n
        iter = filter(filter_iter(n), iter)
n = 1
p = primes()
while n < 100:
    print(next(p))
    n += 1

# 筛选回文序列
def is_palindrome(n):
    sn = str(n)
    l = len(sn)
    s = ''
    for i in range(l):
        s += sn[-(i + 1)]
    # 也可sn[::-1],为reverse操作
    if s == sn:
        return True
    else:
        return False

output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')