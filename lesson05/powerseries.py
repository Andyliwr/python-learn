#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：计算幂级数
x = float(input("请输入x的值："))
n = term = num = 1
result = 1.0
while n < 100:
  term *= x / n
  result += term
  n += 1
  if term < 0.0001:
    break
print("共执行 {} 次, 结果为 {}".format(n, result))