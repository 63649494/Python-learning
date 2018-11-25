#coding=utf-8
#使用numpy包的random函数随机生成1000组数据，然后通过scatter函数绘制了散点图，设置颜色参数c为浮点数组x，即c=x时，再设置颜色渐变参数cmap=plt.cm.get_cmap('RdYlBu')，可以使点的颜色逐渐由红变蓝，最后使用colorbar函数为图像增加颜色条
import numpy as np  
import matplotlib.pyplot as plt  
N = 1000  
x = np.random.randn(N)  
y = np.random.randn(N)  
cm=plt.cm.get_cmap('RdYlBu')  
sc=plt.scatter(x, y,c=x,cmap=cm)  
plt.colorbar(sc)  
plt.show()  