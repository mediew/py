import matplotlib
from matplotlib import pyplot as plt
from matplotlib import font_manager
import math
import random

'''
plt.figure(figsize = (120, 80), dpi = 100)                        # 默认设置最好
x = range(0, 24, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]
plt.plot(x, y)
# plt.savefig('temp1.svg')

# 调整x轴尺度
xticks_labels = [i / 2 for i in range(0, 48)]
plt.xticks(xticks_labels)
yticks_labels = range(math.floor(min(y)), math.ceil(max(y)))
plt.yticks(yticks_labels)
plt.show()
'''

# 构造xy数据，绘制折线图
x = range(120)
y = [random.randint(20, 25) for i in x]
# 设置图片大小和清晰度
plt.figure(figsize = (120, 30))
_x = list(x)[::10]                                                # 每隔10个
# 设置xy轴刻度对应的标签
xticks_labels = ['10点{}分'.format(i) for i in range(60)]         # 若使用第二种设置字体的方法，则需要添加参数fontproperties = my_font
xticks_labels += ['11点{}分'.format(i) for i in range(60)]        # 若使用第二种设置字体的方法，则需要添加参数fontproperties = my_font
# 设置字体
font = {
    'family': 'simsun',
    'weight': 'bold',
    # 'size': 'large'
    }
matplotlib.rc('font', **font)
'''
# 第二种设置字体的方法
my_font = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
'''
# 设置数据点
plt.plot(x, y)
# 应用xy轴的刻度
plt.xticks(_x, xticks_labels[::10], rotation = -45)
# 设置和应用标签
plt.xlabel('时间')                                                # 若使用第二种设置字体的方法，则需要添加参数fontproperties = my_font
plt.ylabel('温度')                                                # 若使用第二种设置字体的方法，则需要添加参数fontproperties = my_font
plt.title('10点到12点每分钟的气温变化图')                           # 若使用第二种设置字体的方法，则需要添加参数fontproperties = my_font
plt.show()
plt.savefig('temp2.png')

