import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['simsun']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(r'E:\pynote\data_analysis\pandas\流量练习数据.xls')
df['销售额'] = df['访客数'] * df['支付转化率'] * df['客单价']
y1 = df.groupby('流量来源')['销售额'].mean().reset_index()
x1 = y1['流量来源']

plt.figure()
width = 0.3
plt.subplot(221)
plt.ylim(0, 250000)
plt.bar(x1, y1['销售额'], width=width)
plt.xticks(x1, x1, rotation=45)
for a, b in zip(x1, y1['销售额']):
    plt.text(a, b + 5, '%.0f' % b, ha='center', va='bottom', fontsize=7)  # fontsize表示柱坐标上显示字体的大小
plt.xlabel('流量来源')
plt.ylabel('销售额')
plt.show()