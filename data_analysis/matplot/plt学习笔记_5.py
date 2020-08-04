from matplotlib import pyplot as plt
from matplotlib import font_manager

x = ['猩球崛起3：终极之战', '敦刻尔克', '蜘蛛侠：英雄归来', '战狼2']
y14 = [2358, 399, 2358, 362]
y15 = [12357, 156, 2045, 168]
y16 = [15746, 312, 4497, 319]

# 设置条形宽度
bar_width = 0.2                       # 必须是一个乘以一后比一小的数

x14 = list(range(len(x)))
x15 = [i + bar_width for i in x14]
x16 = [i + bar_width for i in x15]

plt.bar(x14, y14, width = bar_width, label = '9月14日')
plt.bar(x15, y15, width = bar_width, label = '9月15日')
plt.bar(x16, y16, width = bar_width, label = '9月16日')

my_font = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')

plt.xticks(x15, x, fontproperties = my_font)
plt.legend(prop = my_font)
plt.show()
