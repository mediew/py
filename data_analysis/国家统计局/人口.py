import requests
import json


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    res = requests.get(url, headers=headers)
    # res.encoding = 'gbk'      # 自动检测当前字符集
    html = res.content.decode('utf-8')
    return html

def main():
    url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0301%22%7D%5D&k1=1597492913761&h=1'
    # print(get_html(url))
    html = get_html(url)
    # print(isinstance(html, str))   # 虽然上一步看似返回了一个字典，但返回的对象是一个str！
    dic = json.loads(html)
    # print(dic)
    for k, v in dic.items():         # 注意dic.items()一定要加()!
        for i in v['returndata']:
            print(i)
            print('*' * 50)


if __name__ == '__main__':
    main()
