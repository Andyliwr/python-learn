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
=======
# 数据结构
## 知识点
1. 列表的方法与列表元素的删除
2. 将列表用作栈和队列
3. 列表推导式
4. 元组、集合、字典的创建与操作
5. enumerate() 和 zip() 函数

## 列表
### apend
类似数组的push方法，在末尾加入一项
```
>>> a = [23, 45, 1, -3434, 43624356, 234]
>>> a.append(45)
>>> a
[23, 45, 1, -3434, 43624356, 234, 45]
```
### insert
在指定位置插入一项，比如在a的第0个位置插入1
```
>>> a.insert(0, 1) # 在列表索引 0 位置添加元素 1
>>> a
[1, 23, 45, 1, -3434, 43624356, 234, 45]
```
### count
检查某一项在列表中出现了多少次，比如检查45这一项在列表中出现了几次
```
>>> a.count(45)
2
```
### remove
移除指定项，如果指定项在列表中多个位置都有出现，则每次只移除第一次出现的项
```
>>> a.remove(234)
>>> a
[111, 1, 23, 45, 1, -3434, 43624356, 45]
```
使用del也能删除指定位置的元素,`del a[-1]`表示删除列表a的最后一项
### reserve
列表反转，和数组的reserve类似
### extend
讲两个列表合并，形成一个新的列表，`a.extent(b)`表示讲b添加在a的后面，组成一个新的列表a
### sort
列表排序，和数组sort方法类似，但是貌似不能自定义排序方法
```
>>> a.sort()
>>> a
[-3434, 1, 1, 23, 45, 45, 45, 56, 90, 111, 43624356]
```
## 将列表用作堆栈和队列
栈是我们通常所说的一种 LIFO （Last In First Out 后进先出）数据结构。它的意思是最后进入的数据第一个出来。一个最简单的例子往一端封闭的管道放入一些弹珠然后取出来，如果你想把弹珠取出来，你必须从你最后放入弹珠的位置挨个拿出来。用代码实现此原理：
```
>>> a = [1, 2, 3, 4, 5, 6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> a.pop()
6
>>> a.pop()
5
>>> a.pop()
4
>>> a.pop()
3
>>> a
[1, 2]
>>> a.append(34)
>>> a
[1, 2, 34]
```
上面的代码中我们使用了一个新方法 pop()。传入一个参数 i 即 pop(i) 会将第 i 个元素弹出。

在我们的日常生活中会经常遇到队列，比如售票窗口、图书馆、超市的结账出口。队列 是一种在末尾追加数据以及在开始弹出数据的数据结构。与栈不同，它是 FIFO （First In First Out 先进先出）的数据结构。
```
>>> a = [1, 2, 3, 4, 5]
>>> a.append(1)
>>> a
[1, 2, 3, 4, 5, 1]
>>> a.pop(0)
1
>>> a.pop(0)
2
>>> a
[3, 4, 5, 1]
```
我们使用 a.pop(0) 弹出列表中第一个元素。

## 列表推导式
列表推导式为从序列中创建列表提供了一个简单的方法。如果没有列表推导式，一般都是这样创建列表的：通过将一些操作应用于序列的每个成员并通过返回的元素创建列表，或者通过满足特定条件的元素创建子序列。

假设我们创建一个 squares 列表，可以像下面这样创建。
```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
注意这个 for 循环中的被创建（或被重写）的名为 x 的变量在循环完毕后依然存在。使用如下方法，我们可以计算 squares 的值而不会产生任何的副作用：。
```python
squares = list(map(lambda x: x**2, range(10)))
```
等价与下面下面的表达式
```python
squares = [x**2 for x in range(10)]
```
列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
等同于
```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```
列表推导式也可以嵌套：
```python
>>> z = [x + 1 for x in [x ** 2 for x in a]]
>>> z
[2, 5, 10]
```
## 元组
```python
元组是由数个逗号分割的值组成。
>>> a = 'Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus'
>>> a
('Fedora', 'ShiYanLou', 'Kubuntu', 'Pardus')
>>> a[1]
'ShiYanLou'
>>> for x in a:
...     print(x, end=' ')
...
Fedora ShiYanLou Kubuntu Pardus
```
你可以对任何一个元组执行拆封操作并赋值给多个变量，就像下面这样：
```python
>>> divmod(15,2)
(7, 1)
>>> x, y = divmod(15,2)
>>> x
7
>>> y
1
```
元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值。如果你尝试这些操作，将会出错:
```python
>>> a = (1, 2, 3, 4)
>>> del a[0]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
```
要创建只含有一个元素的元组，在值后面跟一个逗号。
```python
>>> a = (123)
>>> a
123
>>> type(a)
<class 'int'>
>>> a = (123, )
>>> b = 321,
>>> a
(123,)
>>> b
(321,)
>>> type(a)
<class 'tuple'>
>>> type(b)
<class 'tuple'>
```
通过内建函数 type() 你可以知道任意变量的数据类型。还记得我们使用 len() 函数来查询任意序列类型数据的长度吗？
```python
>>> type(len)
<class 'builtin_function_or_method'>
```
## 集合
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。集合对象还支持 union（联合），intersection（交），difference（差）和 symmetric difference（对称差集）等数学运算。

大括号或 set() 函数可以用来创建集合。注意：想要创建空集合，你必须使用 set() 而不是 {}。后者用于创建空字典，我们在下一节中介绍的一种数据结构。
```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # 你可以看到重复的元素被去除
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket
True
>>> 'crabgrass' in basket
False

>>> # 演示对两个单词中的字母进行集合操作
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # a 去重后的字母
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # a 有而 b 没有的字母
{'r', 'd', 'b'}
>>> a | b                              # 存在于 a 或 b 的字母
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # a 和 b 都有的字母
{'a', 'c'}
>>> a ^ b                              # 存在于 a 或 b 但不同时存在的字母
{'r', 'd', 'b', 'm', 'z', 'l'}
```
从集合中添加或弹出元素：
```python
>>> a = {'a','e','h','g'}
>>> a.pop()
'h'
>>> a.add('c')
>>> a
{'c', 'e', 'g', 'a'}
```
## 字典
字典是是无序的键值对（key:value）集合，同一个字典内的键必须是互不相同的。一对大括号 {} 创建一个空字典。初始化字典时，在大括号内放置一组逗号分隔的键：值对，这也是字典输出的方式。我们使用键来检索存储在字典中的数据。
```python
>>> data = {'kushal':'Fedora', 'kart_':'Debian', 'Jace':'Mac'}
>>> data
{'kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian'}
>>> data['kart_']
'Debian'
```
创建新的键值对很简单：
```python
>>> data['parthan'] = 'Ubuntu'
>>> data
{'kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}
```
使用 del 关键字删除任意指定的键值对, `del data['Ubuntu']`
使用 in 关键字查询指定的键是否存在于字典中。`'Ubuntu' in data`
必须知道的是，字典中的键必须是不可变类型，比如你不能使用列表作为键。
dict() 可以从包含键值对的元组中创建字典。
```python
>>> dict((('Indian','Delhi'),('Bangladesh','Dhaka')))
{'Indian': 'Delhi', 'Bangladesh': 'Dhaka'}
```
如果你想要遍历一个字典，使用字典的 items() 方法。
```python
>>> data
{'Kushal': 'Fedora', 'Jace': 'Mac', 'kart_': 'Debian', 'parthan': 'Ubuntu'}
>>> for x, y in data.items():
...     print("{} uses {}".format(x, y))
...
Kushal uses Fedora
Jace uses Mac
kart_ uses Debian
parthan uses Ubuntu
```

许多时候我们需要往字典中的元素添加数据，我们首先要判断这个元素是否存在，不存在则创建一个默认值。如果在循环里执行这个操作，每次迭代都需要判断一次，降低程序性能。

我们可以使用 dict.setdefault(key, default) 更有效率的完成这个事情。
```python
>>> data = {}
>>> data.setdefault('names', []).append('Ruby')
>>> data
{'names': ['Ruby']}
>>> data.setdefault('names', []).append('Python')
>>> data
{'names': ['Ruby', 'Python']}
>>> data.setdefault('names', []).append('C')
>>> data
{'names': ['Ruby', 'Python', 'C']}
```
试图索引一个不存在的键将会抛出一个 keyError 错误。我们可以使用 dict.get(key, default) 来索引键，如果键不存在，那么返回指定的 default 值。
```python
>>> data['foo']
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 'foo'
>>> data.get('foo', 0)
0
```

如果你想要在遍历列表（或任何序列类型）的同时获得元素索引值，你可以使用 enumerate()。

```python
>>> for i, j in enumerate(['a', 'b', 'c']):
...     print(i, j)
...
0 a
1 b
2 c
```
你也许需要同时遍历两个序列类型，你可以使用 zip() 函数。
```python
>>> a = ['Pradeepto', 'Kushal']
>>> b = ['OpenSUSE', 'Fedora']
>>> for x, y in zip(a, b):
...     print("{} uses {}".format(x, y))
...
Pradeepto uses OpenSUSE
Kushal uses Fedora
```
