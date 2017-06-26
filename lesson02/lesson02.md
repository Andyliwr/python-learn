# 第二课
## python所有的关键字
False def if raise None del import return and else if while as except lambda with assert finally monlocal yield break for not class from or continue global pass
## python声明变量
在python中不需要为变量指定数据类型，`a = 1`就已经声明了一个变量了
## python从键盘读取数据
在python中使用`input()`可以做到从键盘读取数据
## 计算投资的小程序
```
#!/usr/bin/env python
amount = float(input("Enter amount: "))  # 输入数额
inrate = float(input("Enter Interest rate: "))  # 输入利率
period = int(input("Enter period: "))  # 输入期限
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year, value))
    amount = value
    year = year + 1
```
while year <= period: 的意思是，当 year 的值小于等于 period 的值时，下面的语句将会一直循环执行下去，直到 year 大于 period 时停止循环。

Year {} Rs. {:.2f}".format(year, value) 称为字符串格式化，大括号和其中的字符会被替换成传入 str.format() 的参数，也即 year 和 value。其中 {:.2f} 的意思是替换为 2 位精度的浮点数。
## python定义多个变量
`a, b = 45, 55` => `a =45, b = 45`
