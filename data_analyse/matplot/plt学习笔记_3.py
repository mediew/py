from matplotlib import pyplot as plt
import numpy as np
import matplotlib

x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
font = {
    'family': 'simsun',
    'weight': 'bold',
    # 'size': 12.0
    }
matplotlib.rc('font', **font)
ax.plot(x, x, label='一次函数')  # Plot some data on the axes.
ax.plot(x, x**2, label='二次函数')  # Plot more data on the axes...
ax.plot(x, x**3, label='三次函数')  # ... and some more.
ax.set_xlabel('x轴')  # Add an x-label to the axes.
ax.set_ylabel('y轴')  # Add a y-label to the axes.
ax.set_title("幂函数")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
