# PythonStudyLoad
python学习之路

Life is short, you need python!

##如何为python程序添加可执行权限
1.在python的首行加入`#! /usr/bin/env python3.6`，目的是告诉shell使用python解释器执行下面的代码
2.添加可以执行权限，`chmod +x helloworld.py`
3.Termenel中输入`./helloword.py`

## python 代码风格
1. python使用空格来将标识符区分，行开始处的空格叫做缩进，如果你的缩进是错误的，python会报unexpected indent错误。如果你在代码中混用制表符和空格，这种缩进错误会很常见。
2. 书写代码准则
+ 使用2两个空格来缩进
+ 永远不要混用空格和制表符
+ 在函数之前空一行
+ 在类之间空两行
+ 字典、列表、元组以及参数列表中在`,`后添加一个空格，对于字典，在`:`后也添加一个空格
+ 在赋值运算符和比较运算符周围要有空格，但是括号里侧不添加空格，eg:`a = f(1, 2) + g(2, 3)`

## python注释
python的注释以#开头，从#开始到行尾都会被程序忽略为注释。应该在#后面跟一个空格然后再写注释

## python模块
模块是包含了我们能复用的代码文件，通常以.py为扩展名。python本身就含有大量的模块，在使用模块之前应该先使用import导入他们
