#coding=utf-8

#list 内置 有序 集合 可加可删 可包含多种数据类型 索引从 0 开始 

'''
假设班里有3名同学：Adam，Lisa和Bart，他们的成绩分别是 95.5，85 和 59，请按照 名字, 分数, 名字, 分数... 的顺序按照分数从高到低用一个list表示，然后打印出来。
'''

L = ['Adam',95.5,'Lisa',85,'Bart',59]
print L

'''
三名同学的成绩可以用一个list表示：

L = [95.5, 85, 59]

请按照索引分别打印出第一名、第二名、第三名，同时测试 print L[3]。

请按照倒序索引分别打印出倒数第一、倒数第二、倒数第三。
'''

L = [95.5, 85, 59]
print L[0]
print L[1]
print L[2]
#print L[3]	#越界 会出错

print L[-1]
print L[-2]
print L[-3]

#list添加元素 append（）加到列尾 或 insert（索引号，元素）

'''
假设新来一名学生Paul，Paul 同学的成绩比Bart好，但是比Lisa差，他应该排到第三名的位置，请用代码实现。
'''

L = ['Adam', 'Lisa', 'Bart']
L.insert(2,'Paul')
print L

#list添删除元素 pop（）从列尾删除 或 pop（索引号）

'''
L = ['Adam', 'Lisa', 'Paul', 'Bart']

Paul的索引是2，Bart的索引是3，如果我们要把Paul和Bart都删掉，请解释下面的代码为什么不能正确运行：

L.pop(2)
L.pop(3) 此时L中只有3个元素 越界了

怎样调整代码可以把Paul和Bart都正确删除掉？
'''

L = ['Adam', 'Lisa', 'Paul', 'Bart']
L.pop(2)
L.pop(2)
print L

#list替换元素 直接替换
'''
班里的同学按照分数排名是这样的：

L = ['Adam', 'Lisa', 'Bart']

但是，在一次考试后，Bart同学意外取得第一，而Adam同学考了倒数第一。

请通过对list的索引赋值，生成新的排名。
'''

L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
L[-1] = 'Adam'
print L