#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：打印斐波那契数列
a, b = 0, 1
while b < 100:
    print(b, end=' ')
    a, b = b, a + b