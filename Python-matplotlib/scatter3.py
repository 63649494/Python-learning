#coding=utf-8
#使用numpy包的random函数随机生成1000组数据，然后通过scatter函数绘制散点图，设置颜色参数c=['r','y','k','g','m']，形状参数marker=‘>'，
import numpy as np  
import matplotlib.pyplot as plt  
N = 1000  
x = np.random.randn(N)  
y = np.random.randn(N)  
color = ['r','y','k','g','m']  
plt.scatter(x, y,c=color,marker='>')  
plt.show()  