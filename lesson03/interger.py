#!/usr/bin/env python
days = int(input("Enter days: "))
# method1
# months = days // 30
# days = days % 30
# print("Months = {} Days = {}".format(months, days))

# method2
print("Months = {} Days = {}".format(*divmod(days, 30)))
