import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


radius = 1     # 定义螺旋半径为1
Vz = 1         # 定义沿z轴方向上的速度为1
t = np.linspace(0, 10, 1000, endpoint=False)
# 对于螺旋运动，极坐标方程如下
x = radius * np.cos(2 * np.pi * t)
y = radius * np.sin(2 * np.pi * t)
z = Vz * t
# sub模式作图
fig = plt.figure()
sub = fig.add_subplot(111, projection='3d')

sub.plot(x, y, z, linewidth=2, color='C1', linestyle='--', label='line')
sub.legend(loc='lower left')

# 三维作图下的特殊关键字参数：视角
sub.view_init(elev=45, azim=45)   # elevation仰角，大于0为俯视 azimuth方位角，0为平行于x轴，45为x轴y轴中间
sub.dist = 10                   # 默认值即是10

sub.set_xticks([-1, -0.5, 0, 0.5, 1])
sub.set_yticks([-1, -0.5, 0, 0.5, 1])
sub.set_zticks([0, 2, 4, 6, 8])

sub.set_xlabel('$x$', fontsize=15)
sub.set_ylabel('$y$', fontsize=15)
sub.set_zlabel('$z$', fontsize=15)

sub.set_title('subplot', fontsize='12')   # 设置sub标题
fig.suptitle('3D plot', fontsize='16')    # 设置fig标题

plt.show()