#coding=utf-8
'''
Python文档：
http://docs.python.org/2/library/functions.html#abs 
也可以在交互式命令行通过 help(abs) 查看abs函数的帮助信息。
'''

'''
sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100。
'''
L = []
x=1
while x<=100:
    L.append(x*x)
    x = x + 1
print sum(L)
