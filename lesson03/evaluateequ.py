#!/usr/bin/env python
#-*-coding: utf-8-*
# 程序实现功能：计算1/x + 1/(x+1) + 1/(x+2) + ... + 1/(x+n),设x=1, n=10
sum = 0
for i in range(1, 10):
  sum = sum + (1.0/i)
  print("{:2d} {:6.4f}".format(i, sum))
  i += 1
