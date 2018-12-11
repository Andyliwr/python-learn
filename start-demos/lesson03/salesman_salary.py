#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能： 计算数码相机销售人员的工资，一个月基本工资是1500，每销售一台相机他可以得到200元并2%的提成
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02
number_of_camera = int(input("请输入销售员已经卖出的的相机数量："))
price = float(input("请输入相机单价："))
bonus = bonus_rate * number_of_camera
commision = commision_rate * number_of_camera * price
print("总奖励金额：{}，提成：{}，最终到手的钱是：{}".format(bonus, commision, (1500 + bonus + commision)))