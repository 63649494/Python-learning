#coding=utf-8
#使用numpy包的random函数随机生成1000组数据，然后通过scatter函数绘制散点图，
import numpy as np  
import matplotlib.pyplot as plt  
N = 1000  
x = np.random.randn(N)  
y = np.random.randn(N)  
plt.scatter(x, y)  
plt.show()  
