#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：计算圆的面积
import math
rValue = float(input("请输入圆的半径："))
area = 2 * math.pi * rValue * rValue
print("圆的面积是：{:10f}".format(area))