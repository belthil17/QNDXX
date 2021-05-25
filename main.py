import requests, json, time


def main():
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
    body = {
	"txtid": time.localtime()[7] // 7 + 51
    }
    r = requests.post(url, data=json.dumps(body), headers=headers)
    if r.ok:
	res = r.json()
	if res['code'] == '100' or res['code'] == '102':
            print(res['message'])
        else:
            print(res)
    else:
	print(r.text)


if __name__ == '__main__':
    with open('./cookie.txt', 'r', encoding='utf-8') as f:
	Cookie = f.read()[:-1]
    main()
