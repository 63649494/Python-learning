#coding=utf-8

'''
注意: Python代码的缩进规则。具有相同缩进的代码被视为代码块，

缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误。
'''

'''
if 有：
如果成绩达到60分或以上，视为passed，否则视为failed。

假设Bart同学的分数是55，请用if语句打印出 passed 或者 failed:
'''
score = 55
if score>=60:
    print 'passed'
else:
    print 'failed'
	
'''
如果按照分数划定结果：

    90分或以上：excellent

    80分或以上：good

    60分或以上：passed

    60分以下：failed

请编写程序根据分数打印结果。
'''
score = 85

if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'
	

'''
班里考试后，老师要统计平均成绩，已知4位同学的成绩用list表示如下：

L = [75, 92, 59, 68]

请利用for循环计算出平均成绩。
'''
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum=sum+score
print sum / 4


'''
利用while循环计算100以内奇数的和。
'''
sum = 0
x = 1
while (x<100)&&(x%2==1):
    sum=sum+x
	x=x+1
print sum

