import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# fig = plt.figure()
# ax = fig.add_subplot(111)
# fig.subplots_adjust(top=100)

fig, ax = plt.subplots(1, 1)
fig.subplots_adjust(top=0.85, hspace=1)

font = FontProperties(
    fname='C:\Windows\Fonts\simsun.ttc',
    weight='bold',
    size=15
)

# 设置整图标题和子图标题
# fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
fig.suptitle('加粗整图标题', fontsize=20, color='r')   # 由于修改了配置文件故无需设置字体
ax.set_title('axes title', fontsize=12, color='c')   # 可以直接设置颜色和大小
# 设置xy轴标签
ax.set_xlabel('x标签')
ax.set_ylabel('ylabel')

# 设置xy轴最大值和最小值，默认[0, 1]
ax.axis([0, 10, 0, 10])
# 使用text方法插入注释
ax.text(3, 8, 'boxed italics text in data coords', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
# 插入LaTeX公式用$$符号包住公式
ax.text(2, 6, r'an equation: $E=mc^2$', fontsize=15)

ax.text(3, 2, 'unicode: Institut für Festkörperphysik')

ax.text(0.95, 0.01, 'colored text in axes coords',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=15)
# 散点图
ax.plot([2], [1], 'o')
# 设置箭头
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.tight_layout()
# 设置x轴刻度线标签
ax.xaxis.set_ticks(np.linspace(0, 8, 5))
# 设置x轴旋转
ax.tick_params(axis='x', rotation=45)
plt.show()