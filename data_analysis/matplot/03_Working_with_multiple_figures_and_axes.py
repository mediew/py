import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 50)
y1 = np.sin(x)
y2 = np.exp(x) * np.cos(x)

figures = [plt.figure(1), plt.figure(2)]
plt.figure(1)

plt.subplot(221)
lines = plt.plot(x, y1, x, y2)
plt.subplot(224)
plt.plot(x)

# ax = [plt.subplot(221), plt.subplot(224)]  # 设置两个子图
ax = plt.subplot(221)   # 设置第一个子图的背景颜色
plt.setp(figures, facecolor='w')
plt.setp(ax, facecolor='c')
plt.setp(lines, linestyle='dashdot')

plt.show()
