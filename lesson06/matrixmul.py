#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：计算nxn的矩阵相乘
n = int(input("输入n的值: "))
print("输入矩阵A: ")
a = []
for i in range(n):
  a.append([int(x) for x in input().split()])
  print("输入矩阵B: ")12
b = []
for i in range(n):
  b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[j][i] for j in range(n)])
print("矩阵相乘的结果: ")
print("-" * 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5), end=' ')
    print()
print("-" * 7 * n)