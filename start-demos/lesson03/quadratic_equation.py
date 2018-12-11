#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现功能：求解a*x^2+b*x+c=0的解
import math
a = input("Enter value of a: ")
b = input("Enter value of b: ")
c = input("Enter value of c: ")
d = b * b - 4 * a * c
if(d < 0):
  print('方程无解！')
else:
  root1 = (-b + math.sqrt(d)) / 2 * a
  root2 = (-b - math.sqrt(d)) / 2 * a
  print("方程的两个解为 {} {}".format(root1, root2))

