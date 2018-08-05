#coding=utf-8

#如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了。

print r"\(~_~)/ \(~_~)/"

#多行用r'''...'''

'''
请把下面的字符串用r'''...'''的形式改写，并用print打印出来
'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
'''

print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''