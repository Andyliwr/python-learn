# -*- coding:utf-8 -*-
# from __future__ import unicode_literals
import json

import requests

from logger import get_logger

# info_log = get_logger('logs/info.log')

def fir(_token):
    headers = {
        'charset': 'utf-8',
        'content-type': 'application/json',
        'token': _token,
        'referer': 'https://servicewechat.com/wx003dcdaf65732dc1/33/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B5084a MicroMessenger/6.6.7 NetType/4G Language/zh_CN',
        'Host': 'eva.mintbao.com',
    }

    response = requests.get('https://xxx', headers=headers)
    print('checkShareUse: {}'.format(response.text))


def sec(que, _token):
    headers = {
        'charset': 'utf-8',
        'content-type': 'application/json',
        'token': _token,
        'referer': 'https://servicewechat.com/wx003dcdaf65732dc1/33/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B5084a MicroMessenger/6.6.7 NetType/4G Language/zh_CN',
        'Host': 'eva.mintbao.com',
    }

    params = (
        ('type', '1'),
        ('question', que),
    )
    response = requests.get('https://xxx', headers=headers, params=params)
    print(response.text)
    print(que)
    print('-'*50)
    return response.json()


def thr(que, _token):
    headers = {
        'charset': 'utf-8',
        'content-type': 'application/json',
        'token': _token,
        'referer': 'https://servicewechat.com/wx003dcdaf65732dc1/33/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16B5084a MicroMessenger/6.6.7 NetType/4G Language/zh_CN',
        'Host': 'eva.mintbao.com',
    }

    data = json.dumps(({"question": que,"type":4}), ensure_ascii=False, indent=2).encode("utf-8")
    response = requests.post('https://xxx', headers=headers, data=data)
    print('saveLog: {}'.format(response.text))


def main(que, _token):
    try:
        print('开始发送checkShareUse')
        fir(_token)
        print('开始发送botResponse')
        answer = sec(que, _token)
        print('开始发送saveLog')
        thr(que, _token)
        return answer
    except:
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    pass
