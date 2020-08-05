import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib


font = {
    'family': 'simsun',
    'weight': 'bold',
    # 'size': 'large'
    }
matplotlib.rc('font', **font)
fig, ax = plt.subplots(2, 2)    # 返回含有4个子图的列表
ax_0, ax_1 = ax[0]
ax_2, ax_3 = ax[1]
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x)
ax_0.plot(y)
ax_0.set_title('正弦函数')
fig.subplots_adjust(top=100)
fig.suptitle('三角函数')
plt.show()