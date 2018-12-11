#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：打印三角形
row = int(input("请输入需要打印的行数："))
i = 0
full_space = 4 * row - 3
while i < row:
  init_space = int((full_space - (4 * (i + 1) - 3)) / 4)
  print(' ' * init_space, end="")
  print(' ' * init_space, end="")
  j = 0
  while j <= i:
    if j == i:
      print("*", end="")
    else:
      print("*   ", end="")
    j += 1
  i += 1
  print("")