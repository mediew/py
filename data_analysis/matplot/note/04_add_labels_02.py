import matplotlib
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0, 100)
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)

fig, axs = plt.subplots(2, 1, figsize=(5, 3), tight_layout=True)
axs[0].plot(x1, y1)
axs[1].plot(x1, y1)
ticks = np.arange(0., 8.1, 2.)    # 超出数据点的部分不显示
# list comprehension to get all tick labels...
# 设置x轴刻度线标签
axs[1].xaxis.set_ticks(ticks)
# # 更改x轴刻度线标签的格式（覆盖旧标签）
# tickla = ['%1.2f' % tick for tick in ticks]    # 保留两位小数
# axs[1].xaxis.set_ticklabels(tickla)
# 通过格式化程序更改x轴刻度线标签的格式(推荐)
formatter = matplotlib.ticker.StrMethodFormatter('{x:1.1f}')   # 保留1位小数
# 设置主定位器
locator = matplotlib.ticker.FixedLocator(ticks)
axs[1].xaxis.set_major_locator(locator)
axs[1].xaxis.set_major_formatter(formatter)
axs[1].set_xlim(axs[0].get_xlim())    # 设置x轴刻度的限度
plt.show()