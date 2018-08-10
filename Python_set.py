#coding=utf-8

#set相当于没有value的dict  创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素 s=set([])

s = set(['Adam','Lisa','Bart','Paul'])

print 'Adam' in s
print 'Bart' in s

'''
请用 for 循环遍历如下的set，打印出 name: score 来。
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
'''
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0],':',x[1]

	
#添加元素 s.remove s.add
'''
针对下面的set，给定一个list，对list中的每一个元素，如果在set中，就将其删除，如果不在set中，就添加进去。
'''
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
       s.remove(name)
    else:
       s.add(name)
print s

