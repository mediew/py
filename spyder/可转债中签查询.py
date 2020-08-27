import re
import requests


"""
tips:
    切片反向截取要指定步长：'69667271'[-1:-5:-1]
    6778694192
    网页格式不符合时也可手动输入。。。
"""


def main():
    url = input('输入综投网地址，如http://www.zt5.com/gp/xingu/498622.html。。。')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}
    html = get_html(url, headers)
    data = parse_html(html)
    print(data)
    parse_data(data)


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    return html


def parse_html(html):
    # print(html)
    result = []
    f4 = re.findall('<p>　　末四位数 (.*?)</p>', html)[0]
    f4 = re.findall('\d{4}', f4)
    result.append(f4)
    f5 = re.findall('<p>　　末五位数 (.*?)</p>', html)[0]
    f5 = re.findall('\d{5}', f5)
    result.append(f5)
    f6 = re.findall('<p>　　末六位数 (.*?)</p>', html)[0]
    f6 = re.findall('\d{6}', f6)
    result.append(f6)
    f7 = re.findall('<p>　　末七位数 (.*?)</p>', html)[0]
    f7 = re.findall('\d{7}', f7)
    result.append(f7)
    f8 = re.findall('<p>　　末八位数 (.*?)</p>', html)[0]
    f8 = re.findall('\d{8}', f8)
    result.append(f8)
    f9 = re.findall('<p>　　末九位数 (.*?)</p>', html)[0]
    f9 = re.findall('\d{9}', f9)
    result.append(f9)
    f10 = re.findall('<p>　　末十位数 (.*?)</p>', html)[0]
    f10 = re.findall('\d{10}', f10)
    result.append(f10)
    return result


def parse_data(data):
    ph = int(input('输入配号：'))
    span = [str(i) for i in range(ph, ph + 1000)]
    count = 0
    for i in span:
        for f4 in data[0]:
            if i[-4:] == f4:
                count += 1
        for f5 in data[1]:
            if i[-5:] == f5:
                count += 1
        for f6 in data[2]:
            if i[-6:] == f6:
                count += 1
        for f7 in data[3]:
            if i[-7:] == f7:
                count += 1
        for f8 in data[4]:
            if i[-8:] == f8:
                count += 1
        for f9 in data[5]:
            if i[-9:] == f9:
                count += 1
        for f10 in data[6]:
            if i[-10:] == f10:
                count += 1
    print('中%d签！' % count)


if __name__ == '__main__':
    main()