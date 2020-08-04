from matplotlib import pyplot as plt
from matplotlib import font_manager

# 3月和10月每日最高气温散点图
m3 = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
m10 = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]
x3 = range(1, 32)
x10 = range(51, 82)
my_font = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
# 使用scatter方法绘制散点图
plt.figure(figsize = (240, 80))
plt.scatter(x3, m3, label = '3月份')
plt.scatter(x10, m10, label = '10月份')
_x = list(x3) + list(x10)
xtick_label = ['3月{}号'.format(i) for i in x3 ]
xtick_label += ['10月{}号'.format(i) for i in x3]
plt.xticks(_x[::3], xtick_label[::3], fontproperties = my_font, rotation = -45)
plt.xlabel('日期', fontproperties = my_font)
plt.ylabel('气温/℃', fontproperties = my_font)
plt.title('3月份与10月份每天最高气温散点图', fontproperties = my_font)
plt.legend(prop = my_font)
plt.show()
