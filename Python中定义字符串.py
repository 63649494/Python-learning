#coding=utf-8
'''
字符串可以用''或者""括起来表示。
本身包含'，可以用" "括起来表示。反之同理
如果字符串既包含'又包含"怎么办？
这个时候，就需要对字符串的某些特殊字符进行“转义”，Python字符串用\进行转义。
要表示字符串 Bob said "I'm OK".
由于 ' 和 " 会引起歧义，因此，我们在它前面插入一个\表示这是一个普通字符，不代表字符串的起始，因此，这个字符串又可以表示为
'Bob said \"I\'m OK\".'
'''

'''
请将下面两行内容用Python的字符串表示并打印出来：

　　Python was started in 1989 by "Guido".

　　Python is free and easy to learn.
'''
s='\tPython was started in 1989 by \"Guido\".\n\tPython is free and easy to learn.'
print s