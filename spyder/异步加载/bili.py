import json
import requests
import re
from lxml import etree


def main():
    # url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,2.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    # html = get_html(url)
    # with open('51job.html', 'wt', encoding='gbk') as f:
    #     f.write(html)
    with open('51job.html', encoding='gbk', errors='ignore') as f:
        hs = f.read()
        html = etree.HTML(hs)
        result = html.xpath('//script[@type="text/javascript"]/text()')[0].replace('window.__SEARCH_RESULT__ = ', '')
        # print(result)
        dic = json.loads(result)
        dic_1 = dic['engine_search_result']    # 表示通过搜索得到的结果
        for k in dic_1:
            print(k)
            print("*" * 20)


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    res = requests.get(url, headers=headers)
    # res.encoding = 'gbk'      # 自动检测当前字符集
    html = res.content.decode(encoding='gbk')
    return html


if __name__ == '__main__':
    main()