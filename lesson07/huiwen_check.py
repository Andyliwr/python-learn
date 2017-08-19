#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：回文检查
def huiwen_check(s):
  return s == s[::-1]
str = input("请输入一串字符串(使用双引号或者单引号括起来)：")
print('回文检查的结果是: {}'.format(huiwen_check(str)))
