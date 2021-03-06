# -*- coding:utf-8 -*-
# @Desc : 
# @Author : chendong
# @Date : 2018-09-13 18:39


### 正则表达式
import re


### 正则表达式语法
# 操作符   	说明  	                            实例
# .	        表示任何单个字符
# [  ]	    字符集，对单个字符给出取值范围     	[ab]表示a、b，[a-z]表示a到z单个字符
# [^  ]	    非字符集，对单个字符给出排除范围	    [^abc]表示非a或b或c的单个字符
# *	        前一个字符0次或无限次扩展	            abc* 表示ab、abc、abcc、abccc等
# +	        前一个字符1次或无限次扩展	            abc+ 表示abc、abcc、abccc等
# ?	        前一个字符0次或1次扩展	            abc? 表示ab、abc
# |	        左右表达式任意一个	                abc|def 表示abc、def
# {m}	    扩展前一个字符m次	                    ab{2}c表示abbc
# {m,n}	    扩展前一个字符m至n次（含n）	        ab{1,2}c表示abc、abbc
# ^	        匹配字符串开头	                    ^abc表示abc且在一个字符串的开头
# $	        匹配字符串结尾	                    abc$表示abc且在一个字符串的结尾
# ( )	    分组标记，内部只能使用| 操作符	    (abc)表示abc，(abc|def)表示abc、def
# \d	    数字，等价于[0‐9]
# \w	    单词字符，等价于[A‐Za‐z0‐9_]

### re模块的基本使用(功能函数)
# 函数            说明
# re.search()     在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
# re.match()      从一个字符串的开始位置起匹配正则表达式，返回match对象
# re.findall()    搜索字符串，以列表类型返回全部能匹配的子串
# re.split()      将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
# re.finditer()   搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
# re.sub()        在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串

### Re库的Match对象(属性和方法)
# 属性	    说明	                                 方法	    说明
# .string	待匹配的文本	                        .group(0)	获得匹配后的字符串
# .re	    匹配时使用的patter对象（正则表达式）	.start()	匹配字符串在原始字符串的开始位置
# .pos	    正则表达式搜索文本的开始位置	        .end()	    匹配字符串在原始字符串的结束位置
# .endpos	正则表达式搜索文本的结束位置	        .span()	    返回(.start(), .end())



