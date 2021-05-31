import requests, json, time, datetime


def everyWeek(Cookie): # 每周青年大学习
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
            if res['code'] == '100' or res['code'] == '102':
                print(res['message'])
                return True
            else:
                print(res['message'])
                return False
        else:
            print(f'每周阅读：发生未知错误：\n{r.text}')
            return False
    except Exception as e:
        print(e)
        return False


def everyDay(Cookie): # 每日签到领积分
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
            resp = r.json()
            if resp['code'] == '100' or resp['code'] == '-1':
                print(resp['message'])
                return True
            else:
                print(resp['message'])
                return False
        else:
            print(f'每日签到：发生未知错误：\n{r.text}')
            return False
    except Exception as e:
        print(e)
        return False


def main(event, context):
    # with open('./config.json', 'r', encoding='utf-8') as f:
    #     Cookie = json.load(f)['Cookie']
    with open('./cookie.txt', 'r', encoding='utf-8') as f:
        Cookie = f.readline()[:-1]
    if time.localtime()[6] in [0,1,2]: # 周一、周二、周三各学习一遍
        i = 3
        while i:
            result = everyWeek(Cookie)
            if result:
                break
            else:
                print(f'每周阅读失败，准备重试……')
                i -= 1
        i = 3
        while i:
            result = everyDay(Cookie)
            if result:
                break
            else:
                print(f'每日签到失败，准备重试……')
                i -= 1
    else:
        i = 3
        while i:
            result = everyDay(Cookie)
            if result:
                break
            else:
                print(f'每日签到失败，准备重试……')
                i -= 1


if __name__ == '__main__':
    main("","")
