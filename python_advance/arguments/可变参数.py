# 可变参数
def calc(*args):
    sum = 0
    for n in args:
        sum += n * n
    return sum

# 可以直接传入多个数据，Python解释器会自动转换为tuple
# print(calc(1,2,3,4))

# 若为list，则需加上*
print(calc(*[1,2,3,4]))
nums = [1,2,3,4]
print(calc(*nums))

# numpy数组也可
import numpy as np
a = np.arange(1,5)
print(calc(*a))