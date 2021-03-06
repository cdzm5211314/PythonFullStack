# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 文件的操作流程:
    # 打开文件/或新建立一个文件
    # 读/写数据
    # 关闭文件

### 在Python中使用open()函数打开或者新建一个文件 :
    # open("文件名","访问模式")  # 返回已个文件对象
    # whit open("文件名","访问模式") as fh:   # 文件操作完成会自动关闭文件
    #       pass

### 文件的访问模式(mode属性值)
# t	    文本模式 (默认)。
# x	    写模式，新建一个文件，如果该文件已存在则会报错。
# b	    二进制模式。
# +	    打开一个文件进行更新(可读可写)。
# U	    通用换行模式（不推荐）。
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	    打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# 打开文件:相对路径
file = open("text.txt","w")
file.write("hello\tword")
# 关闭文件
file.close()

# 读取文件的内容
f = open("text.txt","r")
# text = f.read()
# text = f.read(5)  ## read(5) 表示读取了5个字节
# text = f.readlines()  # readlines() 读取文件的所有行内容,返回一个列表
text = f.readline()  # readline() 读取文件的一行内容
print(text)
f.close()

# 文件对象的方法:
    # read()  读取所有

