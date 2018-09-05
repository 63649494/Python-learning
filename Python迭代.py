#coding=utf-8
'''
在Python中，如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）。

在Python中，迭代是通过 for ... in 来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的

因为 Python 的 for循环不仅可以用在list或tuple上，还可以作用在其他任何可迭代对象上。

因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。

迭代与按下标访问数组最大的不同是，后者是一种具体的迭代实现方式，而前者只关心迭代结果，根本不关心迭代内部是如何实现的。
'''
'''
请用for循环迭代数列 1-100 并打印出7的倍数。
'''
for i in range(1,101):
    if i%7==0:
        print i
		
#索引迭代
'''
Python中，迭代永远是取出元素本身，而非元素的索引
为了拿到索引 ，方法是使用 enumerate() 函数：

enumerate() 函数把：
['Adam', 'Lisa', 'Bart', 'Paul']
变成了类似：
[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
因此，迭代的每一个元素实际上是一个tuple：
for t in enumerate(L):
    index = t[0]
    name = t[1]
    print index, '-', name

如果我们知道每个tuple元素都包含两个元素，for循环又可以进一步简写为：

for index, name in enumerate(L):
    print index, '-', name
	可见，索引迭代也不是真的按索引访问
'''

'''
zip()函数可以把两个 list 变成一个 list：

>>> zip([10, 20, 30], ['A', 'B', 'C'])
[(10, 'A'), (20, 'B'), (30, 'C')]
在迭代 ['Adam', 'Lisa', 'Bart', 'Paul'] 时，如果我们想打印出名次 - 名字（名次从1开始)，请考虑如何在迭代中打印出来。

提示：考虑使用zip()函数和range()函数
'''
