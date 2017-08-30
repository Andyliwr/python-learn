def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
  while True:
    ok = input(prompt)
    # in 关键字。它测定序列中是否包含某个确定的值。
    if ok in ('y', 'yes', 'ye'):
      return True
    if ok in ('n', 'no', 'nop', 'nope '):
      return False
    retries = retries -1
    if retries < 0:
      raise OSError('uncooperative use')
    print(complaint)

# 只给出必要的参数:
# ask_ok('Do you really want to quit?')
# 给出一个可选的参数:
# ask_ok('Ok to overwrite the file?', 2)
# 或者给出所有的参数:
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# 默认值在函数 定义 作用域被解析
i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# 默认值只被赋值一次。这使得当默认值是可变对象时会有所不同，比如列表、字典或者大多数类的实例。例如，下面的函数在后续调用过程中会累积（前面）传给它的参数
print('\n')
def f2(a, L=[]):
  L.append(a)
  return L

print(f2(1))
print(f2(2))
print(f2(3))

# 如果你不想让默认值在后续调用中累积，你可以像下面一样定义函数:
print('\n')
def f3(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L

print(f3(1))
print(f3(2))
print(f3(3))

# 函数可以通过 关键字参数 的形式来调用，形如 keyword = value
print("\n")
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
  print("-- This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts througn it.")
  print("-- Lovely plumage, the", type)
  print("-- It's", state, "!")

parrot(100) # 传一个参数
print("\n")
parrot(voltage=0.5) # 传一个参数
print("\n")
parrot(voltage=1000000, action='VOOOOOM')
print("\n")
parrot('a thousand', state='pushing up the daisies')

# 任何参数都不可以多次赋值
print("\n")
def function(a):
  pass

# function(0, a=0)

# 引入一个形如 **name 的参数时，它接收一个字典，该字典包含了所有未出现在形式参数列表中的关键字参数
# 使用一个形如 *name （下一小节详细介绍） 的形式参数，它接收一个元组（下一节中会详细介绍），包含了所有没有出现在形式参数列表中的参数值
# *name 必须在 **name 之前出现
print("\n")
def cheeseshop(kind, *arguments, **keywords):
  print("-- Do you have any", kind, "?")
  print("-- I'm sorry, we're all out of", kind)
  for arg in arguments:
    print(arg)
  print("-" * 40)
  keys = sorted(keywords.keys())
  for kw in keys:
    print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper = "Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# 一个最不常用的选择是可以让函数调用可变个数的参数。这些参数被包装进一个元组，在这些可变个数的参数之前，可以有零到多个普通的参数
# 通常，这些 可变 参数是参数列表中的最后一个，因为它们将把所有的剩余输入参数传递给函数
# 任何出现在 *args 后的参数是关键字参数，这意味着，他们只能被用作关键字，而不是位置参数
def write_multiple_items(file, separator, *args):
  file.write(separator.join(args))

print("\n")
def concat(*args, sep="，"):
  print(sep.join(args))

concat('那就这这样吧', '当然爱都曲终人散')
print("\n")
concat('那就这这样吧', '当然爱都曲终人散', '不要再想了', sep="\n")

