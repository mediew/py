from functools import reduce

'''
map函数作用于Iterable，返回一个Iterator，所以结果需要用list函数才能显示出来。
reduce把一个函数作用在一个Iterable上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算。
下面的函数把str转换为float
'''
def str2float(s):
    index = s.index('.')
    rs = s.replace('.', '')
    l = len(rs)

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def l2int(x1, x2):
        return x1 * 10 + x2

    ri = reduce(l2int, map(char2num, rs))
    return ri / (10 ** (l - index))

print('str2float(\'123.456\') =', str2float('123.456'))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    if not isinstance(name, str):
        print('please input str')
    else:
        return name[0].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))     # map返回一个Iterator，所以结果需要用list函数变为list
print(L2)