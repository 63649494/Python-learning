#coding=utf-8
'''
对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。

对应上面的问题，取前3个元素，用一行代码就可以完成切片：

>>> L[0:3]
['Adam', 'Lisa', 'Bart']
L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

如果第一个索引是0，还可以省略：

>>> L[:3]
['Adam', 'Lisa', 'Bart']
也可以从索引1开始，取出2个元素出来：

>>> L[1:3]
['Lisa', 'Bart']
只用一个 : ，表示从头到尾：

>>> L[:]
['Adam', 'Lisa', 'Bart', 'Paul']
因此，L[:]实际上复制出了一个新list。

切片操作还可以指定第三个参数：

>>> L[::2]
['Adam', 'Bart']
第三个参数表示每N个取一个，上面的 L[::2] 会每两个元素取出一个来，也就是隔一个取一个。

把list换成tuple，切片操作完全相同，只是切片的结果也变成了tuple。
'''
'''
range()函数可以创建一个数列：

>>> range(1, 101)
[1, 2, 3, ..., 100]
请利用切片，取出：

1. 前10个数；
2. 3的倍数；
3. 不大于50的5的倍数。
'''
L = range(1,101)

print L[:10]
print L[2::3]
print L[4:50:5]

#倒序切片：记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
'''
利用倒序切片对 1 - 100 的数列取出：

* 最后10个数；

* 最后10个5的倍数。
'''
L=range(1,101)
print L[-10:]
print L[-46::5]

#对字符串切片
'''
字符串 'xxx'和 Unicode字符串 u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
'''
'''
字符串有个方法 upper() 可以把字符变成大写字母：

>>> 'abc'.upper()
'ABC'
但它会把所有字母都变成大写。请设计一个函数，它接受一个字符串，然后返回一个仅首字母变成大写的字符串。

提示：利用切片操作简化字符串操作
'''
def firstCharUpper(s):
	return s[0].upper()+s[1:]
print firstCharUpper('hello')

