import requests
from bs4 import BeautifulSoup as bs
from multiprocessing import Pool

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
    lst10 = ['0%d' % d for d in range(0, 10)]
    lst20 = list(map(str, range(10, 100)))
    index_lst = lst10 + lst20
    lst1 = ['http://reader.epubee.com/books/mobile/46/46c142f8bd116f7a062db4ce39ad4a91/text000{}.html'.format(i) for i in index_lst]
    lst2 = ['http://reader.epubee.com/books/mobile/46/46c142f8bd116f7a062db4ce39ad4a91/text00{}.html'.format(i) for i in range(100, 109)]
    lst = lst1 + lst2
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
    base_url = 'http://reader.epubee.com/books/mobile/46/46c142f8bd116f7a062db4ce39ad4a91/'
    for tag in content.contents:
        if tag != '\n' and tag.name != 'nav':
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
    p = Pool(4)
    for url in url_lst:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Cookie': '_ga=GA1.2.1443472058.1596077277; _gid=GA1.2.132754376.1597805529; Hm_lvt_6ef419ba5cea4fb5ed354aab51911eb2=1597805657; Hm_lpvt_6ef419ba5cea4fb5ed354aab51911eb2=1597807183Cookie: _ga=GA1.2.1443472058.1596077277; _gid=GA1.2.132754376.1597805529; Hm_lvt_6ef419ba5cea4fb5ed354aab51911eb2=1597805657; Hm_lpvt_6ef419ba5cea4fb5ed354aab51911eb2=1597807183'
        }
        content = get_content(url, headers)
        title = get_title(url, headers)
        with open(title + '.xhtml', 'w', encoding='utf-8-sig') as f:
            upper = """<head><meta content="true" name="cover" />
<title>Cover</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<link href="../Styles/Style0001.css" rel="stylesheet" type="text/css" />
<link href="../Styles/Style0002.css" rel="stylesheet" type="text/css" />
<script src='/books/mobile/jquery.min.js' language = 'javascript' type='text/javascript'></script>
<script src='/books/mobile/webreader3.js' language = 'javascript' type='text/javascript'></script>

<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=0.5,maximum-scale=1.5, user-scalable=yes" />
<link rel="stylesheet" type="text/css" href="../Styles/Style0003.css" />
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
    p.close()
    p.join()


if __name__ == '__main__':
    main()
