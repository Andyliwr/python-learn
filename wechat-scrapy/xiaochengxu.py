#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 爬去核保查查公众号数据
# @date 2018/11/28
# @author lidikang@myhexin.com

import base64
import json
import logging
import os
import random
import re
import time
from binascii import a2b_hex, b2a_hex
from datetime import datetime

import pymongo
import requests
from apscheduler.schedulers.background import BlockingScheduler
from Crypto.Cipher import AES

from curl_moni import main
from logger import get_logger


class prpcrypt():
    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)
        add = length - (count % length)
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text, iv):
        cryptor = AES.new(self.key, self.mode, IV=iv)
        plain_text = cryptor.decrypt(text)
        return plain_text.strip()

def b(content):
    return base64.b64decode(content)

class XcxScrapy:
    def __init__(self):
        KEY1 = 'UwVrGX4x2r+Pk7bf1aItja=='
        self.token = '4ac1c0259b27f13dfb78c2959da3bf4e'
        self.pc = prpcrypt(b(KEY1))  # 初始化密钥
        self.info_log = get_logger('logs/info.log')
        self.db = self.connect_db()
        # 查找剩余需要爬取的疾病数量
        self.max_len = self.db.disease.count_documents({ 'finished': 0 })
        self.count = 0
        print('Number of the lefting disease: {}'.format(self.max_len))
        self.info_log.warning('Number of the lefting disease: {}'.format(self.max_len))
        if self.max_len > 0:
            print('Task started.')
            print('-' * 50)
            self.info_log.warning('Task started.....')
            # 定时爬取
            self.scheduler = BlockingScheduler()
            self.scheduler.add_job(self.request_data, 'interval', id='main_schedule', seconds=120, args=[self])
            self.scheduler.start()
        # self.init_database(self)
        # self.request_data(self)

    # 初始化数据库
    @staticmethod
    def init_database(self):
        print('Initial database started!')
        # 初始化疾病表
        disease_file = open('./disease.txt', 'r', encoding='UTF-8')
        try:
            for line in disease_file:
                tmp_line = line.strip().strip('\n')
                self.db.disease.insert_one({
                    'name': tmp_line,
                    'reply': '',
                    'finished': 0
                })
                print('Initial disease: ', tmp_line)
        finally:
            print('Initial database finished!')
            disease_file.close()

    @staticmethod
    def connect_db():
        instance = pymongo.MongoClient('127.0.0.1', 27017)
        db = instance.hebaochacha
        return db
    
    @staticmethod
    def request_data(self):
        # 查找即将爬取的疾病信息
        cur_disease = self.db.disease.find_one({ 'finished': 0 }, skip=self.count)
        question = cur_disease['name']
        print('Start to scrapy: {} ...'.format(question))
        self.info_log.critical('Start to scrapy: {} ...'.format(question))
        res = main(question, self.token)
        print('Response: {}'.format(json.dumps(res, ensure_ascii=False, indent=2)))
        self.info_log.critical('Response: {}'.format(json.dumps(res, ensure_ascii=False, indent=2)))
        if not res: return False
        if res.get('isSuccess'):
            result = res.get('result', {})
            iv = result.get('iv', '')
            content = result.get('content', '')
            if iv and content:
                answer = self.pc.decrypt(b(content), b(iv))
                answer = str(answer, encoding="utf-8")
                if answer:
                    # print(json.dumps(json.loads(str(answer, encoding="utf-8")), ensure_ascii=False, indent=2))
                    answer_re = re.compile('''"content":"(.*?)"''')
                    img_re = re.compile('''"resource_url":"(.*?)"''')
                    answer_list = answer_re.findall(''.join(answer.split()))
                    an = '\n'.join(answer_list)
                    img_list = img_re.findall(''.join(answer.split()))
                    im = '\n'.join(img_list)
                    self.db.disease.update_one({ 'name': question }, { '$set': { 'reply': an, 'images': im, 'finished': 1 } })
                    print('Save data to db: {}'.format({ 'name': question, 'reply': an, 'images': im, 'finished': 1 }))
                    self.info_log.critical('Save data to db: {}'.format({ 'name': question, 'reply': an, 'images': im, 'finished': 1  }))
                    self.count = self.count + 1
                    return True
                else:
                    print('Answer is empty.')
                    self.info_log.warning('Answer is empty.')
                    self.db.disease.update_one({ 'name': question }, { '$set': { 'reply': '', 'images': '', 'finished': 1 } })
                    self.count = self.count + 1
                    return False
            else:
                print('NO iv or content --- {}.'.format(question))
                self.info_log.warning('NO iv or content --- {}.'.format(question))
                self.db.disease.update_one({ 'name': question }, { '$set': { 'reply': '', 'images': '', 'finished': 1 } })
                self.count = self.count + 1
                return False
        else:
            if res.get('errorMsg') == 'token已过期':
                print('Token is invild, please login again.')
                self.info_log.warning('Token is invild, please login again.')
                # 结束进程
                os._exit(0)
            else:
                self.count = self.count + 1
                return False


instance = XcxScrapy()
