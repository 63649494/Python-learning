一、python单行注释符号(#)

python中单行注释采用 #开头

示例：#this is a comment

二、批量、多行注释符号

多行注释是用三引号''' '''包含的，例如：
'''
三对单引号 多行注释
三对单引号 多行注释
三对单引号 多行注释
三对单引号 多行注释
'''
"""
或者双引号
或者双引号
或者双引号
"""


三、python中文注释方法

若运行报错：

SyntaxError: Non-ASCII character '\xe4' in file getoptTest.py on line 14, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

如果文件里有非ASCII字符，需要在第一行或第二行指定编码声明。把ChineseTest.py文件的编码重新改为ANSI，并加上编码声明：

一定要在第一行或者第二行加上这么一句话：

#coding=utf-8

或者

# -*- coding: utf-8 -*-  


py脚本的前两行一般都是：

#!/usr/bin/python  
# -*- coding: utf-8 -*- 