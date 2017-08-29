#!/usr/bin/env python
# -*- coding:utf-8 -*-

from pymongo import MongoClient
import json

conn = MongoClient('localhost', 27017)
db = conn.test_db  #连接mydb数据库，没有则自动创建
my_set = db.testTable
my_set.insert({"name":"lidikang","age":18})

with open("zips.json",'r') as load_f:
  load_dict = json.load(load_f)
  print(len(load_dict['data']))
  my_set.insert(load_dict['data'])