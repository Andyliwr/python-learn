#!/usr/bin/env python
#-*-coding:utf-8*-
# 程序实现的功能：打印三角形
import simplejson as json
distobj = {'name' : 'jim', 'sex' : 'male', 'age': 18}
jsonstr = simplejson.dumps(distobj)
print(jsonstr)