from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# 绘制直方图

a = [random.randint(91, 150) for i in range(250)]

# 分组：组数=极差/组距
d = 6                                              # 组距
jc = max(a) - min(a)                               # 极差
num_bins = (max(a) - min(a)) // d + 1              # 组数
# print(a, min(a), max(a), num_bins)

group = range(min(a), max(a) + d, d)               # 设置分组
plt.figure(figsize = (120, 80))
plt.hist(a, group, density = 1)
my_font = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')

# 设置刻度
xtick_label = ['{}分钟'.format(i) for i in group]
plt.xticks(group, xtick_label, fontproperties = my_font)
plt.grid()
plt.show()
