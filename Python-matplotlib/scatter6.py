#coding=utf-8
#使用numpy包的random函数随机生成1000组数据，然后通过scatter函数绘制了散点图，设置透明度参数linewidth=[1]*1000，设置边缘颜色edgecolors='r'
import numpy as np  
import matplotlib.pyplot as plt  
N = 1000  
x = np.random.randn(N)  
y = np.random.randn(N)  
plt.scatter(x, y,linewidth=[1]*1000,edgecolors=['r','y','g','pink'])  
plt.show()  