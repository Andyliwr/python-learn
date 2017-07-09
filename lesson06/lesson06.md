# 字符串
用单引号('xxx')或者双引号("xxx")包裹起来的变量
在变量命名的时候使用'\'可以标示接下来的一行内容也是属于字符串的内容，在命令行可以用来输入一个多行的字符串

字符串定义的时候使用'\n'标识换行，在使用print的时候'\n'前后会出现在不同的行

如果你想分几行输出，并且希望行尾的换行符自动包含到字符串中，可以使用三对引号："""xxx"""或者'''xxx'''
```python
>>> print("""\
... Usage: thingy [OPTIONS]
...      -h                        Display this usage message
...      -H hostname               Hostname to connect to
... """)
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
```
## 字符串的常用方法
### title
title可以将字符串的单词首字母变成大写
```python
>>> s = "shi yan lou"
>>> s.title()
'Shi Yan Lou'
```
### upper
upper可以将字符串的单词全部转化成大写

### lower
lower可以将字符串的单词全部转化成小写

### swapcase
swapcase返回字符串大小写交换之后的版本

### isalnum
isalnum检查所有字符串是否为数字字母

### isalpha
isalpha检查字符串是不是只包含字母，类似的isdigit检查字符串所有字符是否均为数字，islower检查字符串所有字符是不是都是小写，istitle检查是不是首字母大写，isupper检查字符串所有字符是不是都是大写

### split
split用来分割字符串，它有一个参数用来指定字符串以什么字符分割，默认为" "，它将返回一个包含所有分割后的字符串的列表

```python
>>> s = "We all love Python"
>>> s.split()
['We', 'all', 'love', 'Python']
>>> x = "shiyanlou:is:waiting"
>>> x.split(':')
['shiyanlou', 'is', 'waiting']
```

### join
join可以用来指定字符连接多个字符串，它需要一个包含字符串元素的列表作为输入然后连接列表中的字符串元素

```python
>>> "-".join("GNU/Linux is great".split())
'GNU/Linux-is-great'
```
## 字符串剥离