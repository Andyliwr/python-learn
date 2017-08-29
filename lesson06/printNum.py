#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：给定一串字符串，选中其中的数字打印出来
str = input("请输入一串字符串(使用双引号或者单引号括起来)：")
strArr = list(str)
result = []
for x in strArr:
  if(x.isdigit()):
    result.append(x)
print('过滤非数字得到的结果是: {}'.format(''.join(result)))