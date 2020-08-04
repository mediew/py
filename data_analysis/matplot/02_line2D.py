import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(0, 5, 0.5)
y1 = np.cos(x1) * 50
x2 = x1
y2 = np.exp(x2)

# 使用line2D设置曲线的属性, line2D对象即为l1,l2
# 方法1：使用关键字参数定义线宽
# plt.plot(x1, y1, x2, y2, linewidth=3.0)   # linewidth值越大线条宽度越大
# plt.show()
# 方法2：通过调用Line2D对象line的set_antialiased方法，关闭对象的反锯齿效果
# plt.plot(x1, y1, x2, y2)
# l1, l2= plt.plot(x1, y1, x2, y2)
# l1.set_antialiased(False)
# plt.show()
# 方法3：
l1, l2 = plt.plot(x1, y1, x2, y2)
plt.setp(l1, c='r', lw=1.0)
plt.setp(l2, c='b', lw=2.5)
plt.show()

'''
要获取可设置的线属性列表, 调用setp()函数，并只传入Line2D对象（或列表）作参数。
参见：https://sijiji.gitbooks.io/matplotlib/content/%E6%8E%A7%E5%88%B6%E7%BA%BF%E5%B1%9E%E6%80%A7.html
'''