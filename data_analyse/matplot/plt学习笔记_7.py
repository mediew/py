from matplotlib import pyplot as plt
from matplotlib import font_manager

# 绘制条形图
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90, 150]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]
print(len(interval), len(width), len(quantity))
plt.bar(range(12), quantity, width = 1)          # 注意width设为1和width结果不同
x = [i - 0.5 for i in range(13)]
plt.xticks(x, interval)
plt.grid()
plt.show()
