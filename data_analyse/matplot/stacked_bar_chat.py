import matplotlib.pyplot as plt
import numpy as np
import matplotlib


x_label = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']
width = 0.35
boy_means = np.random.randint(28, 35, 6)
girl_means = np.random.randint(26, 30, 6)
boy_std = np.random.random(6) * 3        # 创建含有6个元素的一维数组
girl_std = np.random.random(6) * 3

font = {
    'family': 'simsun',
    'weight': 'bold',
    # 'size': 'large'
    }
matplotlib.rc('font', **font)
'''
fig, ax = plt.subplots()
ax.bar(x_label, boy_means, width, yerr=boy_std, label='男生')
ax.bar(x_label, girl_means, width, yerr=girl_std, bottom=boy_means, label='女生')
ax.set_ylabel('分数/Score')
ax.set_xlabel('组别/Group')
ax.set_title('scores by group and gender')
ax.legend()
'''

plt.figure()
plt.plot()
plt.show()
