#coding=utf-8

#tuple是另一种有序的列表，中文翻译为“ 元组 ”，一旦创建完毕，就不能修改了。
#创建tuple和创建list唯一不同之处是用( )替代了[ ]。

'''
创建一个tuple，顺序包含0 - 9这10个数。
'''
t = (0,1,2,3,4,5,6,7,8,9)
print t		#输出时包含（）

# 0 个元素的 tuple，也就是空tuple，直接用 ()表示：
t = ()
print t

'''
创建包含1个元素的 tuple，若用t = (1) 则不会输出(1)，而是输出1。
因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果1，导致我们得到的不是tuple，而是整数 1。
正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”
所以 t = (1,)，输出为(1,)，明确告诉时一个tuple
'''

'''
请指出右边编辑器中代码为什么没有创建出包含一个学生的 tuple：

t = ('Adam')

print t

请修改代码，确保 t 是一个tuple。
'''
t = ('Adam',)
print t



#“可变”的tuple:tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

'''
定义了tuple：

t = ('a', 'b', ['A', 'B'])

由于 t 包含一个list元素，导致tuple的内容是可变的。能否修改上述代码，让tuple内容不可变？
'''
t = ('a', 'b', 'A', 'B')
print t
#或
t = ('a', 'b', ('A', 'B'))
print t

#len(t)可求t的元素个数