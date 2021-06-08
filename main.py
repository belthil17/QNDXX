#!/usr/bin/env python3
import requests ,json ,time 
def everyWeek (OOO0O0OO0OOO0O000 ):
    ""
    OO0OOOO0000OO0000 ='每周青年大学习\n'
    O00000O00OOOOOOO0 ='http://home.yngqt.org.cn/qndxx/xuexi.ashx'
    OOOO000OOOOOOOO0O ={"Host":"home.yngqt.org.cn","Accept":"application/json, text/javascript, */*; q=0.01","X-Requested-With":"XMLHttpRequest","Accept-Language":"zh-cn","Accept-Encoding":"gzip, deflate","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Origin":"http://home.yngqt.org.cn","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN","Referer":"http://home.yngqt.org.cn/qndxx/","Cookie":OOO0O0OO0OOO0O000 }
    O0OOOOOO00O0O0OOO ={"txtid":time .localtime ()[7 ]//7 +51 }
    try :
        OOOOOOOOO0OO00000 =requests .post (O00000O00OOOOOOO0 ,data =json .dumps (O0OOOOOO00O0O0OOO ),headers =OOOO000OOOOOOOO0O ,proxies ={"http":None ,"https":None })
        OOOOOOOOO0OO00000 .encoding =OOOOOOOOO0OO00000 .apparent_encoding 
        if OOOOOOOOO0OO00000 .ok :
            OO0000OO0000OOOOO =OOOOOOOOO0OO00000 .json ()
            if OO0000OO0000OOOOO ['message'].find ('成功')!=-1 or OO0000OO0000OOOOO ['message'].find ('已学习')!=-1 :
                print (f"{OO0OOOO0000OO0000}{OO0000OO0000OOOOO['message']}")
                return True 
            else :
                print (f"{OO0OOOO0000OO0000}{OO0000OO0000OOOOO['message']}")
                return False 
        else :
            print (f'{OO0OOOO0000OO0000}POST 完成后发生未知错误，错误信息如下：\n{OOOOOOOOO0OO00000.text}')
            return False 
    except Exception as O0O0O0O000OOOOO00 :
        print (f"{OO0OOOO0000OO0000}无法完成 POST 访问，错误信息如下：\n{O0O0O0O000OOOOO00}")
        return False 
def everyDay (O0OOO0O000OO0OO00 ):
    ""
    O0O0OOOO000OO0OOO ='每日签到领积分\n'
    OO0O0OO0OOO000OOO ="http://home.yngqt.org.cn/qndxx/user/qiandao.ashx"
    OO0O0O0O0O0O000O0 ={"Host":"home.yngqt.org.cn","X-Requested-With":"XMLHttpRequest","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-cn","Accept":"application/json, text/javascript, */*; q=0.01","Origin":"http://home.yngqt.org.cn","Content-Length":"0","Connection":"keep-alive","User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.4(0x1800042c) NetType/4G Language/zh_CN","Referer":"http://home.yngqt.org.cn/qndxx/user/guize.aspx","Cookie":O0OOO0O000OO0OO00 }
    try :
        OOO0O0O000OO0OOOO =requests .post (OO0O0OO0OOO000OOO ,headers =OO0O0O0O0O0O000O0 ,proxies ={"http":None ,"https":None })
        OOO0O0O000OO0OOOO .encoding =OOO0O0O000OO0OOOO .apparent_encoding 
        if OOO0O0O000OO0OOOO .ok :
            O000OOO00OOO0OO0O =OOO0O0O000OO0OOOO .json ()
            if O000OOO00OOO0OO0O ['message'].find ('成功')!=-1 or O000OOO00OOO0OO0O ['message'].find ('已签到')!=-1 :
                print (f"{O0O0OOOO000OO0OOO}{O000OOO00OOO0OO0O['message']}")
                return True 
            else :
                print (f"{O0O0OOOO000OO0OOO}{O000OOO00OOO0OO0O['message']}")
                return False 
        else :
            print (f'{O0O0OOOO000OO0OOO}POST 完成后发生未知错误，错误信息如下：\n{OOO0O0O000OO0OOOO.text}')
            return False 
    except Exception as OOOO0O000OO0O00OO :
        print (f"{O0O0OOOO000OO0OOO}无法完成 POST 访问，错误信息如下：\n{OOOO0O000OO0O00OO}")
        return False 
def main (OO00O0O00OOO00000 ,O0OO0000O0O00OOO0 ):
    ""
    with open ('./cookie.json','r',encoding ='utf-8')as OOO0O0OO000O000O0 :
        O0OO00000000000O0 =json .load (OOO0O0OO000O000O0 )
    for OO0000O00O0OO00OO in O0OO00000000000O0 :
        if time .localtime ()[6 ]in [0 ,1 ,2 ]:
            OO0O0OOOOOO000OO0 =3 
            while OO0O0OOOOOO000OO0 :
                O000OO0O000OOOOOO =everyWeek (OO0000O00O0OO00OO )
                if O000OO0O000OOOOOO :
                    OO0O0OOOOOO000OO0 =0 
                else :
                    print ('每周阅读失败，准备重试……')
                    OO0O0OOOOOO000OO0 -=1 
        OO0O0OOOOOO000OO0 =3 
        while OO0O0OOOOOO000OO0 :
            O000OO0O000OOOOOO =everyDay (OO0000O00O0OO00OO )
            if O000OO0O000OOOOOO :
                OO0O0OOOOOO000OO0 =0 
            else :
                print ('每日签到失败，准备重试……')
                OO0O0OOOOOO000OO0 -=1 
if __name__ =='__main__':
    main ("","")
