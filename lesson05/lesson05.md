# 循环
# while 循环
while循环语句的语法如下：
```
while condition:
 statement1
 statement2
```
只有在codition为真的时候statement1和statement2才会被执行

默认情况下，print除了打印你提供的字符串之外，还会打印一个换行符,我们可以通过print()的另一个参数来替换这个换行符。但是这个只有在3.0版本以上的python才支持
```
print(a, end=' ')
```
使用关键字`break`可以终止循环

字符串如果乘以一个整数n，讲返回一个由n个此字符串拼接成的字符串
```
print('-' * 10) ===> ----------
```