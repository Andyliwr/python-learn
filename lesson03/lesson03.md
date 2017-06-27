#python 运算符和表达式
## 算数运算符
最常见的无非就是 + - * /

运算符连接的两个数字，只要一个浮点数，结果就会返回浮点数。

进行除法运算若是除不尽，结果将会是小数，`//`类似js中的`%`表示整除，将返回商的整数部分。而求余运算符变成了`%`

一个计算n天多少个月余多少天的小程序：
```
days = int(input("Enter days: "))
# method1
# months = days // 30
# days = days % 30
# print("Months = {} Days = {}".format(months, days))

# method2
print("Months = {} Days = {}".format(*divmod(days, 30)))
```
方法2中`divmod(num1, num2)`返回一个二元组，第一个值是num1和num2相整除得到的值，第二个是num1和num2求余得到的值，然后使用`*`来拆封这个二元组，得到这两个值。

## 关系运算符
就是常见的那些，没啥说的
## 逻辑运算符
对于逻辑与或非，python使用and、or、not这几个关键字

逻辑运算符and和or也叫短路运算符，他们的参数从左向右解析，一旦结果确定就停止了。比如A和C为真而B为假，那么A and B and C就不会去解析C，解析完A和B就直接返回false了。

关于逻辑运算符的优先级，not具有最高优先级，其实是and，or优先级最低，所以A and not B or C等于(A and (not B)) or C，另外逻辑运算符的优先级低于关系运算符

## 自增自减运算符
x op= expression 等价于 x = x op expression

## 类型装换
1. float将字符串转换成浮点数
2. int将字符串转换成整数值
3. str将浮点数或者整数转换成字符串

## 如何解决python注释不支持中文的错误
```
SyntaxError: Non-ASCII character '\xe7' in file demo.py on line 15, but no encoding declared; see http://Python.org/dev/peps/pep-0263/ for details
```
在首行添加这样一行注释：
```
#-*-coding:utf-8-*
```
## python的除法
在python2.5的版本中存在两种除法，即所谓的true除法和floor除法。当使用x/y形式进行除法运算的时候，如果x和y都是整数，那么运算会对结果进行截取，取运算的整数部分，比如2/3的结果就是0。当x和y的运算结果有一个是浮点数那么会进行所谓的true除法，比如2/3.0的结果就是0.66666666666，另外一种除法是采用x//y的形式，那么这里采用的就是floor除法，即得到不大于结果的最大整数，也就是商取整，比如2//3的结果是0, 4//3的结果是1
