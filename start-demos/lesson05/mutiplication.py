#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：打印九九乘法表
print("-" * 70)
i = 1
while i < 10:
  n = 1
  while n < 10:
    print("{:1d}x{:1d}={:2d} ".format(i, n, i * n), end=" ")
    n += 1
  print()
  i += 1
print("-" * 70)
