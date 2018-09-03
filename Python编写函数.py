#coding=utf-8
'''
在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，
然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。
'''

'''
任务
请定义一个 square_of_sum 函数，它接受一个list，返回list中每个元素平方的和。
'''

def square_of_sum(L):  #有冒号
    sum=0
    for i in L:
        sum=sum+i*i
    return sum

print square_of_sum([1,2,3,4,5])
print square_of_sum([-5,0,5,15,25])

#函数返回多个值
'''
可以返回多个值，但其实这只是一种假象，Python函数返回的仍然是单一值；
用print打印返回结果，原来返回值是一个tuple
但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''

'''
任务
一元二次方程的定义是：ax² + bx + c = 0

请编写一个函数，返回一元二次方程的两个解。

注意：Python的math包提供了sqrt()函数用于计算平方根。
'''

import math

def quadratic_equation(a,b,c):
    t=math.sqrt(b*b-4*a*c)
    x1=(-b+t)/(2*a)
    x2=(-b-t)/(2*a)
    return x1,x2
print quadratic_equation(2,3,0)
print quadratic_equation(1,-6,5)


#递归函数，我调我自己！
'''
没啥只要注意
使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，
所以，递归调用的次数过多，会导致栈溢出。可以试试计算 fact(10000)。
'''

'''
任务
汉诺塔 (http://baike.baidu.com/view/191666.htm) 的移动也可以看做是递归函数。

我们对柱子编号为a, b, c，将所有圆盘从a移到c可以描述为：

如果a只有一个圆盘，可以直接移动到c；

如果a有N个圆盘，可以看成a有1个圆盘（底盘） + (N-1)个圆盘，首先需要把 (N-1) 个圆盘移动到 b，然后，将 a的最后一个圆盘移动到c，再将b的(N-1)个圆盘移动到c。

请编写一个函数，给定输入 n, a, b, c，打印出移动的步骤：

move(n, a, b, c)

例如，输入 move(2, 'A', 'B', 'C')，打印出：

A --> B
A --> C
B --> C
'''

def move(n,a,b,c):  #a=from b=helper c=to
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)  #将a的(n-1)个都移动到b
    print a, '-->', c  #a的最后一个移动到c
    move(n-1, b, a, c)  #将b的(n-1)个都移动到c

move(4,'A','B','C')  #初始状态 a有4个盘子
运行成功
A --> B
A --> C
B --> C
A --> B
C --> A
C --> B
A --> B
A --> C
B --> C
B --> A
C --> A
B --> C
A --> B
A --> C
B --> C


#Python之定义默认参数
'''
函数的默认参数的作用是简化调用，你只需要把必须的参数传进去。但是在需要的时候，又可以传入额外的参数来覆盖默认参数值。
'''
'''
请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
'''
def greet(s='world'):
    print 'Hello,'+s+'.'
greet()
greet('Bart')


#Python之定义可变参数
'''
如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数：

def fn(*args):
    print args
可变参数的名字前面有个 * 号，我们可以传入0个、1个或多个参数给可变参数：
可变参数也不是很神秘，Python解释器会把传入的一组参数组装成一个tuple传递给可变参数，因此，在函数内部，直接把变量 args 看成一个 tuple 就好了。
'''
'''
请编写接受可变参数的 average() 函数。
'''
def average(*args):
    sum=0.0
    if(len(args)==0):
        return sum
    for x in args:
        sum=sum+x
    return sum/len(args)
print average()
print average(1,2)
print average(1,2,2,3,4)