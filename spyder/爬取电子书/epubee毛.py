import requests
from bs4 import BeautifulSoup as bs

"""
Target:
    爬取 http://reader.epubee.com/ 上电子书资源，并用 Sigil 软件制作成epub文件
Tips:
    map(f, iterable)
    utf-8网页出现乱码用utf-8-sig编码
    BeautifulSoup对象提取class属性结果是list，其他属性是str
    open()函数'a'参数表示追加模式, 'w'表示覆盖模式
"""


def get_url_list():
    lst10 = ['0%d' % d for d in range(1, 10)]
    lst20 = list(map(str, range(10, 16)))
    index_lst = lst10 + lst20
    lst = ['http://reader.epubee.com/books/mobile/6e/6eba0802dfa2628383b630a4943e2c2e/text000{}.html'.format(i) for i in index_lst]
    return lst


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = res.content.decode('utf-8-sig')
    return html


def get_pic(url, headers):
    res = requests.get(url, headers=headers)
    pic = res.content
    return pic


def get_content(url, headers):
    """
    爬取正文
    :param headers: dict
    :param url: str
    :return:
    """
    html = get_html(url, headers)
    bs_html = bs(html, 'lxml')
    content = bs_html.find_all('div', class_='readercontent-inner')[0]
    con_lst = []
    base_url = 'http://reader.epubee.com/books/mobile/6e/6eba0802dfa2628383b630a4943e2c2e/'
    for tag in content.contents:
        if tag != '\n':
            if tag['class'][0] == 'picture_figure':
                with open(tag.img['src'], 'wb') as f:
                    pic_url = base_url + tag.img['src']
                    pic = get_pic(pic_url, headers)
                    f.write(pic)
                tag.img['src'] = '../Images/' + tag.img['src']
        con_lst.append(tag)
        # print(tag)
    return con_lst


def get_title(url, headers):
    """
    爬取标题
    :param headers: dict
    :param url: str
    :return:
    """
    html = get_html(url, headers)
    bs_html = bs(html, 'lxml')
    title = bs_html.find_all('title')[0].get_text("|", strip=True)
    return title


def main():
    url_lst = get_url_list()
    for url in url_lst:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Cookie': '_ga=GA1.2.1443472058.1596077277; _gid=GA1.2.132754376.1597805529; Hm_lvt_6ef419ba5cea4fb5ed354aab51911eb2=1597805657; Hm_lpvt_6ef419ba5cea4fb5ed354aab51911eb2=1597807183Cookie: _ga=GA1.2.1443472058.1596077277; _gid=GA1.2.132754376.1597805529; Hm_lvt_6ef419ba5cea4fb5ed354aab51911eb2=1597805657; Hm_lpvt_6ef419ba5cea4fb5ed354aab51911eb2=1597807183'
        }
        content = get_content(url, headers)
        title = get_title(url, headers)
        with open(title + '.xhtml', 'w', encoding='utf-8-sig') as f:
            upper = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN" lang="zh-CN">
<head><meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8"/>
<title>毛泽东选集</title>
<link rel="stylesheet" href="../Styles/Style0002.css" type="text/css"/>
<link rel="stylesheet" type="text/css" href="../Styles/Style0001.css"/>
</head>
<body>
"""
            f.write(upper)
        with open(title + '.xhtml', 'a', encoding='utf-8-sig') as f:
            for tag in content:
                f.write(str(tag))
        with open(title + '.xhtml', 'a', encoding='utf-8-sig') as f:
            down = """
</body>
</html>
"""
            f.write(down)
        print('%s:完成！' % title)


if __name__ == '__main__':
    main()
