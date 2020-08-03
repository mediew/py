import numpy as np

# numpy数组属性
array = np.array([[1, 2, 3], [3, 4, 5]])
print(array.ndim)    # 秩，即轴(axis)的数量或维度(dimention)的数量,运行结果为2
print(array.shape)   # 数组的维度，对于矩阵，n 行 m 列，运行结果为(2,3)
print(array.size)    # 数组元素的总个数，相当于 array.shape 中 n*m 的值，运行结果是2*3=6
print(array.dtype)   # ndarray 对象的元素类型，可作为参数指定，如dtype = np.int

# 创建numpy数组并设置基本属性
array = np.array([[1, 2, 3], [3, 4, 5]], dtype = np.float32)   # 设置数据类型为浮点型
print(array)
a = np.zeros((3, 4), dtype = np.int32)      # 设置数据类型为int32，即32位整数型，大数据运算时应减少位数，降低内存消耗
print(a)
a = np.ones((3, 3), dtype = np.int32)
print(a)
a = np.empty((3, 4))
print(a)
a = np.arange(10, 20, 2)   # 这里设置步长为2，默认为1
print(a)
a = np.arange(12)
a = a.reshape((3, 4))      # 更改shape为(3, 4)
print(a)
a = np.linspace(1, 10, 20)
print(a)

# numpy基本运算
a = np.array([1, 2, 3, 4])
b = np.arange(5, 9)
print(b, a + b, a - b, a * b, a ** b, a * 4, a > 3, a == 3)     # 相应位置的元素做运算
print(np.sum(a), np.min(a), np.max(a))
c = np.random.random((2, 4))
print(c)
x = np.sum(c, axis = 1)
y = np.sum(c, axis = 0)
# axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。注意生成的还是numpy数组对象！
print(x, y)
a_average = np.average(a)
a_median = np.median(a)
print(a_average, a_median)    # 注意返回的是一个数

'''
a = np.array([1, 2, 3, 4, 5], dtype = np.int32)
median = np.median(a)
print(median)
'''

print(np.cumsum(a))           # 累加操作
t = a.reshape(2, 2)           # 结果为[[1, 2], [3, 4]]
print(t.T)                    # 转秩操作，结果为[[1, 3], [2, 4]]
print(np.transpose(t))        # 也是转秩操作

# 索引和切片
a = np.arange(10)
print(a[2])
a = a.reshape(2, 5)
print(a[1])
print(a[1][0], a[1, 0])       # 两者等效
print(a[1, 2:])               # 结果为[7, 8, 9]
print(a[1, 0: 2])
print(a[a > 5], a[a < 3])     # 筛选数据

# 合并、分割、复制
x = a[0]
y = a[1]
vst = np.vstack((x, y))             # 垂直合并，vertical stack
print(vst)
hst = np.hstack((x, y))             # 水平合并，horizal stack
print(hst)
c = np.arange(12).reshape((3, 4))
vsp = np.split(c, 2, axis = 1)      # 垂直分割，vertical stack
print(vsp)
hsp = np.split(c, 3, axis = 0)      # 水平分割，horizal stack
print(hsp)
vsp_1 = np.vsplit(c, 3)             # 等效于 np.split(c, 3, axis = 0)
hsp_1 = np.hsplit(c, 2)             # 等效于 np.split(c, 2, axis = 1)
print(vsp_1, hsp_1)
nonequal_sp0 = np.array_split(c, 2, axis = 0)     # 不等量分割
nonequal_sp1 = np.array_split(c, 3, axis = 1)
print(nonequal_sp0, nonequal_sp1)
# 复制操作
a = np.arange(4)
b = a
print(a, b)
a[1] = 100
print(a, b)    # 结果是a, b仍然一样，原因是a = b只是b引用了a，仍然指向原来的内存地址，当a改变后，b也随之发生变化。
b = a.copy()
print(a, b)
a[1] = 1
print(a, b)    # a.copy()后，b有了独立的内存地址，不因为a的变而变化

# 数组元素的添加和删除
# 追加
a = np.array([[1, 2, 3], [4, 5, 6]])
j = np.append(a, [7, 8, 9])                            # axis默认为None，此时为横向加成，并返回一维数组，结果为
k = np.append(a, [[7, 8, 9]], axis = 0)                # axis = 0, 表示对每一列进行追加操作，结果为
i = np.append(a, [['x'], ['y']], axis = 1)             # axis = 1, 表示对每一行进行追加操作，结果为
print(a, j, k, i)                                      # 以上函数作用于a，并不改变a的大小！
# 插入
a = [[1, 2], [3, 4], [5, 6]]
k = np.insert(a, 3, [7, 8])                            # 3表示索引值，即把[7, 8]插入到索引为3的位置，axis参数为None，返回一个一维数组
j = np.insert(a, 1, [11], axis = 0)                    # axis = 0, 表示按列操作，把[11]插入到索引为1的地方，并把[11]扩充为[11, 11]
i = np.insert(a, 1, 11, axis = 1)                      # axis = 1, 表示按行操作，把11插入到每一行索引为1的地方
print(a, j, k, i)
# 删除和去重
a = np.arange(12).reshape(3, 4)
k = np.delete(a, 5)                                    # 5为索引值，删除之后返回一个一维数组
j = np.delete(a, 1, axis = 1)                          # 删除索引为2的列
print(a, k, j)
# 切片删除
a = np.arange(1, 11)
k = np.delete(a, np.s_[3:6])                           # 删除4，5，6
print(a, k)
# 去重
a = np.array([1, 1, 2, 3, 1, 4])
k = np.unique(a)                                       # 去重
j = np.unique(a, return_index = True)                  # 返回去重后的数组，及其中每个元素第一次出现的索引
i = np.unique(a, return_counts = True)                 # 返回去重后的数组，及其中每个元素出现的次数
print(a, k, j, i)

# 对数组的元素进行字符串拼接
print('对数组的元素进行字符串拼接')
a = np.char.add(['hello'], ['world'])                      # helloworld
b = np.char.add(['hello', 'hi'], ['老王', '老陈'])
print(a, b)
# 重复生成字符串
print('重复生成字符串')
a = np.char.multiply('对不起', 10)
print(a)
# 字符串居中
print('字符串居中')
a = np.char.center('helloworld', 30, fillchar = ' ')
print(a)
# 字符串分割
print('字符串分割')
a = np.char.split('www.baidu.com', sep = '.')
b = np.char.split('http://www.baidu.com/news/guoneixinwen', sep = '/')
c = np.char.splitlines('i \nlove \nyou')
print(a, b, c)
# 去除开头和结尾的特定字符
print('去除开头和结尾的特定字符')
a = np.char.strip('     老牛      ', ' ')
print(a)
# 拼接字符串
print('拼接字符串')
a = np.char.join('/', 'laoniu')
print(a)
# 替换
print('替换')
a = np.char.replace('i like laoniu', 'laoniu', 'caixukun')
print(a)

# 数学函数
a = np.array([0, 30, 45, 60, 90])
sin = np.sin(a * np.pi / 180)
cos = np.cos(a * np.pi / 180)
tan = np.tan(a * np.pi / 180)
print(a, sin, cos, tan)
a = np.array([1.01, 2.67, 3.45, 1.0, 67, 2.1111])
ar = np.around(a, 1)                                   # 四舍五入,1表示保留1位小数
fl = np.floor(a)                                       # 向下取整
ce = np.ceil(a)                                        # 向上取整
print(a, ar, fl, ce)

# 统计函数
# 极差
print('最大值、最小值、极差')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
min = np.amin(a, 1)                                          # 计算最小值，1代表按行计算，0代表按列
max = np.amax(a, 0)                                          # 计算最大值
all_range = np.ptp(a)                                        # 计算全部元素的极差
range_1 = np.ptp(a, 1)                                       # 按行计算极差
print(a, min, max, all_range, range_1)
# 中位数
print('中位数')
medi = np.percentile(a, 50)                                  # 计算全部元素的中位数，50表示50%分位
m1 = np.percentile(a, 50, axis = 1)                          # 按列计算中位数
m = np.median(a)                                             # 直接计算全部元素中位数
m0 = np.median(a, axis = 0)                                  # 按列计算中位数
print(medi, m1, m, m0)
# 平均数
print('平均数')
aver = np.mean(a)                                            # 全部元素的平均数
a0 = np.mean(a, axis = 0)                                    # 按列计算平均数
print(aver, a0)
# 标准差和方差
print('标准差和方差')
std = np.std(a)
var = np.var(a)
print(std, var)




