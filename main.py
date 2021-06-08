#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Chiupam (https://t.me/chiupam)
# @Data     : 2021-06-08 19:58
# @Version  : v1.3
# @Updata   : 1. 支持多账号学习
# @Future   : Null

import requests, json, time


def everyWeek(Cookie):
    """
    每周青年大学习
    :param Cookie: 传入 Cookie
    :return: 返回是否成功完成 POST 请求的布尔值
    """
    task = '每周青年大学习\n'
    url = 'http://home.yngqt.org.cn/qndxx/xuexi.ashx'
    headers = {
        "Host": "home.yngqt.org.cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "http://home.yngqt.org.cn",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Referer": "http://home.yngqt.org.cn/qndxx/",
        "Cookie": Cookie
    }
    data = {
        "txtid": time.localtime()[7] // 7 + 51
    }
    try:
        r = requests.post(url, data=json.dumps(data), headers=headers, proxies={"http": None, "https": None})
        r.encoding = r.apparent_encoding
        if r.ok:
            res = r.json()
            if res['message'].find('成功') != -1 or res['message'].find('已学习') != -1:
                print(f"{task}{res['message']}")
                return True
            else:
                print(f"{task}{res['message']}")
                return False
        else:
            print(f'{task}POST 完成后发生未知错误，错误信息如下：\n{r.text}')
            return False
    except Exception as e:
        print(f"{task}无法完成 POST 访问，错误信息如下：\n{e}")
        return False


def everyDay(Cookie):
    """
    每日签到领积分
    :param Cookie: 传入 Cookie
    :return: 返回是否成功完成 POST 请求的布尔值
    """
    task = '每日签到领积分\n'
    url = "http://home.yngqt.org.cn/qndxx/user/qiandao.ashx"
    headers = {
        "Host": "home.yngqt.org.cn",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-cn",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Origin": "http://home.yngqt.org.cn",
        "Content-Length": "0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN",
        "Referer": "http://home.yngqt.org.cn/qndxx/user/guize.aspx",
        "Cookie": Cookie
    }
    try:
        r = requests.post(url, headers=headers, proxies={"http": None, "https": None})
        r.encoding = r.apparent_encoding
        if r.ok:
            res = r.json()
            if res['message'].find('成功') != -1 or res['message'].find('已签到') != -1:
                print(f"{task}{res['message']}")
                return True
            else:
                print(f"{task}{res['message']}")
                return False
        else:
            print(f'{task}POST 完成后发生未知错误，错误信息如下：\n{r.text}')
            return False
    except Exception as e:
        print(f"{task}无法完成 POST 访问，错误信息如下：\n{e}")
        return False


def main(event, context):
    """
    腾讯云函数程序入口
    :param event: 可省略
    :param context: 可省略
    :return: 可省略
    """
    with open('./cookie.json', 'r', encoding='utf-8') as f:
        cookies = json.load(f)
    for cookie in cookies:
        if time.localtime()[6] in [0,1,2]: # 周一、周二、周三各学习一遍
            i = 3
            while i:
                result = everyWeek(cookie)
                if result:
                    i = 0
                else:
                    print('每周阅读失败，准备重试……')
                    i -= 1
        i = 3
        while i:
            result = everyDay(cookie)
            if result:
                i = 0
            else:
                print('每日签到失败，准备重试……')
                i -= 1


if __name__ == '__main__':
    main("","")
