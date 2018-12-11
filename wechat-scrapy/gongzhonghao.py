#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 爬去核保查查公众号数据
# @date 2018/11/28
# @author lidikang@myhexin.com

import random
import time
from datetime import datetime

import itchat
import pymongo
from apscheduler.schedulers.background import BackgroundScheduler
from threading import Timer


class GzhScrapy:
    def __init__(self):
        self.cur_disease_id = ''
        self.cur_count = 0
        self.cur_company = 1
        self.max_len = 0
        self.cur_user_name = ''
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.send_disease_name, 'interval', id='main_schedule', seconds=60, args=[self])
        self.scheduler.add_job(self.send_company_num, 'interval', id='sub_schedule', seconds=5, args=[self])
        self.scheduler.start()
        self.scheduler.pause_job('main_schedule')
        self.scheduler.pause_job('sub_schedule')
        self.reply = {}
        self.start_collect_reply = 0
        self.db = self.connect_db()
        self.wechat_init(self)
        # self.init_database(self)

    # 初始化数据库
    @staticmethod
    def init_database(self):
        print('Initial database started!')
        # 初始化疾病表
        disease_file = open('./disease.txt', 'r', encoding='UTF-8')
        try:
            for line in disease_file:
                tmp_line = line.strip().strip('\n')
                self.db.disease.insert_one({'name': tmp_line, 'reply': {}, 'finished': 0 })
                print('Initial disease: ', tmp_line)
        finally:
            print('Initial database finished!')
            disease_file.close()

    @staticmethod
    def send_company_num(self):
        print('Start to send company number ---> ', self.cur_company)
        itchat.send(str(self.cur_company), toUserName=self.cur_user_name)
        self.cur_company = self.cur_company + 1

    @staticmethod
    def send_disease_name(self):
        if self.cur_count > self.max_len:
            self.scheduler.pause_job('main_schedule')
            print('Congratulation! you have finished all task!')
            return
        print('\n\nCurrent time: ', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        cur_disease = self.db.disease.find_one({ 'finished': 0 }, skip=self.cur_count)
        self.cur_disease_id = cur_disease['_id']
        self.cur_count = self.cur_count + 1
        self.cur_company = 1
        self.reply = {}
        itchat.send(cur_disease['name'], toUserName=self.cur_user_name)
        print('Start to send disease name ---> ', cur_disease['name'], ', cur_count: ', self.cur_count)
        # 爬取每家公司关于当前疾病的回复
        self.scheduler.resume_job('sub_schedule')

    @staticmethod
    def get_data(self):
        mps = itchat.get_mps()
        mps = itchat.search_mps(name='公众号名称')
        if len(mps) > 0:
            userName = mps[0]['UserName']
            self.cur_user_name = userName
            max_len = self.db.disease.count_documents({ 'finished': 0 })
            print('There are still ', max_len, ' diseases needing to be scrapied')
            # 周期性爬取疾病
            # self.scheduler.resume_job('main_schedule')
            self.send_disease_name(self)
        else:
            print('Can\'t find MPS 公众号名称')



    @staticmethod
    def connect_db():
        instance = pymongo.MongoClient('127.0.0.1', 27017)
        db = instance.hebaochacha
        return db

    @staticmethod
    def wechat_init(self):
        @itchat.msg_register(itchat.content.TEXT, isMpChat=True)
        def reply_msg(msg):
            print("Recive a message from MPS: ", msg['Content'].strip().strip('\n'))
            if msg['FromUserName'] == self.cur_user_name:
                if msg['Content'].find('请问您是问哪家公司的核保建议') >= 0:
                    self.start_collect_reply = 1
                else:
                    # 疾病答案不合法，停止询问公司详情
                    if self.cur_company == 1:
                        self.db.disease.update_one({ '_id': self.cur_disease_id }, { '$set': { 'finished': 1 } })
                        self.scheduler.pause_job('sub_schedule')
                        print('No answer, has paused the sub_schedule!')
                        return

                    if self.cur_company == 10:
                        self.db.disease.update_one({ '_id': self.cur_disease_id }, { '$set': { 'reply': self.reply, 'finished': 1 } })
                        self.scheduler.pause_job('sub_schedule')
                        print(self.cur_disease_id, 'Save data successfully!')
                        return

                    if self.start_collect_reply == 1:
                        print(self.reply)
                        print('reply\'s length: ', str(len(self.reply)), ', cur_count: ' + str(self.cur_count) + ', cur_company: ' + str(self.cur_company))
                        self.reply[str(self.cur_company)] = msg['Content'].strip()

        def after_login():
            print('Login success!')
            # self.init_database(self)
            self.get_data(self)
            pass

        def after_logout():
            # 关闭定时任务
            self.scheduler.shutdown()
            print('Has shutdown the scheduler!')
            pass

        itchat.auto_login(hotReload=True, loginCallback=after_login, exitCallback=after_logout)
        itchat.run()


instance = GzhScrapy()
