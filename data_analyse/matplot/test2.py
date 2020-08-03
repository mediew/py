import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import random


plt.figure()
font = FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.subplot(221)
x1 = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x1)
plt.plot([2], [3], 'o', label='散点')
plt.plot(x1, y1, label='正弦')
plt.xlabel('x轴', fontproperties=font)
x_ticks = np.pi * np.arange(0, 2.5, 0.5)
x_ticks_label = ['0', '0.5π', 'π', '1.5π', '2π']
plt.xticks(x_ticks, x_ticks_label)
plt.ylim(-1.5, 4)
plt.title('散点图和正弦函数', fontproperties=font)
plt.legend(prop=font)
# plt.show()

plt.subplot(222)
# random.seed(81)
np.random.seed(81)
a = np.random.randn(1000)
mu = 100
std = 15
sample = mu + std * a
# group
plt.hist(sample)
plt.title('频数分布直方图', fontproperties=font)
plt.show()