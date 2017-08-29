#!/usr/bin/env python
#-*coding:utf-8*-
# 打印斐波拉起数列
def fib(n):
  """Print a Fibonacci series up to n."""
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()

def fib2(n):
  """Return a list containing the Fibonacci series up to n."""
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a+b
  # return 语句从函数中返回一个值，不带表达式的 return 返回 None
  return result

fib(2000)
print(fib(0))
f100 = fib2(100)
print(f100)
