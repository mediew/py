from matplotlib import pyplot as plt
from matplotlib import font_manager

# 你和同桌11到29岁每年交朋友的数量
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 1, 1, 1]                # 自己
b = [1, 0, 1, 3, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]                # 同桌
x = range(11, 30)
plt.plot(x, a, label = '自己', color = 'orange', linestyle = ':')
plt.plot(x, b, label = '同桌', color = 'cyan', linestyle = '--')             # 颜色也可用十六进制表示
xtick_labels = ['{}岁'.format(i) for i in x]
my_font = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simsun.ttc')
plt.xticks(x, xtick_labels, fontproperties = my_font)
plt.yticks(range(9))
# 绘制网格
plt.grid(alpha = 0.2, linestyle = ':')               # 设置透明度
# 添加图例
plt.legend(prop = my_font, loc = 'upper left')       # 默认选择最佳位置
plt.show()


