#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：使用remove实现全部移除
a = [1, 2, 3, 4, 5, 1, 2, 1, 2]
print("初始值为: {}".format(a))
need_delete_value = int(input("请输入需要删除的值："))
while need_delete_value in a:
  a.remove(need_delete_value)
print("删除之后的值: {}".format(a))