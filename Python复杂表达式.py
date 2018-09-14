#coding=utf-8
'''
使用for循环的迭代不仅可以迭代普通的list，还可以迭代dict。

假设有如下的dict：

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
完全可以通过一个复杂的列表生成式把它变成一个 HTML 表格：

tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table>'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
注：字符串可以通过 % 进行格式化，用指定的参数替代 %s。字符串的join()方法可以把一个 list 拼接成一个字符串。

把打印出来的结果保存为一个html文件，就可以在浏览器中看到效果了：

<table border="1">
<tr><th>Name</th><th>Score</th><tr>
<tr><td>Lisa</td><td>85</td></tr>
<tr><td>Adam</td><td>95</td></tr>
<tr><td>Bart</td><td>59</td></tr>
</table>
'''
'''
在生成的表格中，对于没有及格的同学，请把分数标记为红色。

提示：红色可以用 <td style="color:red"> 实现。
'''
d={'Adam':95,'Lisa':85,'Bart':59}
def generate_tr(name,score):
    if(score<60):
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name,score)
    else:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name,score)

tds = [generate_tr(name,score) for name,score in d.iteritems()]
print '<table border=1>'
print '<tr><th>Name</th><th>Score</th></tr>'
print '\n'.join(tds)
print '</table>'

#条件过滤
'''
列表生成式的 for 循环后面还可以加上 if 判断,有了 if 条件，只有 if 判断为 True 的时候，才把循环的当前元素添加到列表中。
'''
'''
请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
提示：
1. isinstance(x, str) 可以判断变量 x 是否是字符串；
2. 字符串的 upper() 方法可以返回大写的字母。
'''
def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello','world',101])

#多层表达式
'''
for循环可以嵌套，因此，在列表生成式中，也可以用多层 for 循环来生成列表。

对于字符串 'ABC' 和 '123'，可以使用两层循环，生成全排列：

>>> [m + n for m in 'ABC' for n in '123']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
'''
'''
利用 3 层for循环的列表生成式，找出对称的 3 位数。例如，121 就是对称数，因为从右到左倒过来还是 121。
'''
print [m+n+m for m in '123456789' for n in '0123456789'] #输出的是字符串 不是数字
print [100*m + 10*n +m for m in range(1,10) for n in range(10)]

'''
Python 入门 结束于 2018/9/13
'''
