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
L=['Adam','Lisa','Bart','Paul']
M=range(1,5)
for index,name in zip(M,L):
    print index,'-',name
	
#迭代dict的value
'''
dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list，这样，我们迭代的就是 dict的每一个 value：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for v in d.values():
    print v
如果仔细阅读Python的文档，还可以发现，dict除了values()方法外，还有一个 itervalues() 方法，用 itervalues() 方法替代 values() 方法，迭代效果完全一样：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for v in d.itervalues():
    print v
	
那这两个方法有何不同之处呢？

1. values() 方法实际上把一个 dict 转换成了包含 value 的list。

2. 但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
'''
'''
给定一个dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

请计算所有同学的平均分。
'''
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for i in d.itervalues():
   sum= sum + i
print sum/4
