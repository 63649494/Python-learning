#coding=utf-8

#dict 关联  key: value,最后一个 key: value 的逗号可以省略。花括号 {} 表示这是一个dict 一个 key-value 算一个 len() 函数可以计算任意集合的大小：

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
	'Paul': 75
}

#d[key] 的形式来查找对应的 value
#判断一下 key 是否存在，用 in 操作符
#dict本身提供的一个 get 方法，在Key不存在的时候，返回None

print 'Adam:',d['Adam']
if 'Lisa' in d:
    print 'Lisa:',d['Lisa']
print 'Bart:',d.get('Bart')

#特点:查找速度快 查找速度都一样 占用内存大，还会浪费很多内容 key不能重复 无顺序

#更新dict的方法d[key]

d['Meng']= 99 #添加元素
d['Meng']= 90 #更改元素的值

for key in d:
    print key,':',d[key] #遍历dict

