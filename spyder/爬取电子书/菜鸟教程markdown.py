import requests
from bs4 import BeautifulSoup
import os


def get_content(url, headers):
    """
    得到侧边目录栏
    :param s: str
    :return: str
    """
    html = get_html(url, headers).decode('utf-8')
    bs = BeautifulSoup(html, 'lxml')
    main_contents = bs.find_all('div', class_='container main')[0]
    # print(main_contents)
    index_bar = main_contents.div.div
    index_bar = index_bar.prettify()
    content = main_contents.find_all('div', class_="article")[0]
    content = content.find_all('div', class_='article-body')[0].prettify()
    main_content = index_bar + content
    return main_content


def main():
    url = 'https://www.runoob.com/markdown/md-tutorial.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}
    # html = get_html(url, headers)
    # if not os.path.exists('md.html'):
    #     with open('md.html', 'wb') as f:
    #         f.write(html)
    with open('md.html', 'rb') as f:
        md = f.read()
    url_list = get_url_list(md)
    # print(url_list)
    head = '''<!Doctype html>
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta property="qc:admins" content="465267610762567726375" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Markdown 教程 | 菜鸟教程</title>

  <link rel='dns-prefetch' href='//s.w.org' />
<link rel="canonical" href="http://www.runoob.com/markdown/md-tutorial.html" />
<meta name="keywords" content="Markdown 教程,markdown">
<meta name="description" content="Markdown 教程   Markdown 是一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档。 Markdown 语言在 2004 由约翰·格鲁伯（英语：John Gruber）创建。 Markdown 编写的文档可以导出 HTML 、Word、图像、PDF、Epub 等多种格式的文档。  Markdown 编写的文档后缀为 .md, .markdown。   Markdown 应用 Markdown 能被使用来撰写电..">
		
	<link rel="shortcut icon" href="https://static.runoob.com/images/favicon.ico" mce_href="//static.runoob.com/images/favicon.ico" type="image/x-icon" >
	<link rel="stylesheet" href="../Styles/style.css" type="text/css" media="all" />	
	<link rel="stylesheet" href="../Styles/font-awesome.min.css" media="all" />	
</head>
<body>'''
    pad = '''</body>
</html>'''
    frame_head = '''<div class="col middle-column">
  <div class="article">
	<div class="article-heading-ad" style="display: none;">
	</div>'''

    frame_pad = '''</div>	
</div>'''
    # print(get_content(url, headers))
    for title, url in url_list.items():
        content = get_content(url, headers)
        with open(title + '.xhtml', 'w', encoding='utf-8') as f:
            f.write(head)
            f.write(frame_head)
            f.write(content)
            f.write(frame_pad)
            f.write(pad)
        print('%s.html完成！' % title)


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    html = res.content
    return html


def get_url_list(s):
    """
    获取URL列表
    :param s: str
    :return: list
    """
    bs = BeautifulSoup(s, 'lxml')
    index_column = bs.find_all('div', class_='design', id='leftcolumn')[0]
    index_column = index_column.find_all('a')
    index_list = {}
    for index in index_column:
        url = 'https://www.runoob.com' + index['href']
        title = index['title']
        index_list[title] = url
    return index_list



if __name__ == '__main__':
    main()