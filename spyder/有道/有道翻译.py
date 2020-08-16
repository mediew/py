import requests
from hashlib import md5
import time
import random


def translate(word):
    data = r(word)

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "252",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=-1103206661@10.108.160.208; JSESSIONID=aaaz2uYzc9C-MbIla70px; OUTFOX_SEARCH_USER_ID_NCOO=313162146.4733675; ___rl__test__cookies=1597541988358",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.59",
        "X-Requested-With": "XMLHttpRequest",
    }

    params = {
        "i": word,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": data['salt'],
        "sign": data['sign'],
        "lts": data['ts'],
        "bv": data['bv'],
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME",
    }

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    res = requests.post(url, headers=headers, data=params)
    # print(res)
    return res.json()


# 用Python代码模拟JavaScript代码
def r(e):
    appversion = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    t = md5(appversion.encode()).hexdigest()
    r = str(int(time.time() * 1000))
    i = r + str(random.randint(0, 9))
    sign = md5(('fanyideskweb' + e + i + ']BjuETDhU)zqSxf-=B#7m').encode()).hexdigest()
    return {
        'ts': r,
        'bv': t,
        'salt': i,
        'sign': sign
    }


if __name__ == '__main__':
    word = input('请输入你想翻译的内容：')
    result = translate(word)
    print(result)
    print('原文', result['translateResult'][0][0]['tgt'], '\n', '译文', result['translateResult'][0][0]['src'])
