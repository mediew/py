import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import os


class MyHTMLParser(HTMLParser):

    count = 0

    def __init__(self, title):
        HTMLParser.__init__(self)
        MyHTMLParser.count += 1
        self.jud = ''
        self.title = title + '.md'
        self.count = 1
        self.ex = ''

    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self.jud = 'h1'
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('# ')
        if tag == 'h2':
            self.jud = 'h2'
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('## ')
        if tag == 'h3':
            self.jud = 'h3'
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('### ')
        if tag == 'pre':
            self.jud = 'pre'
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('> ')
        if tag == 'p':
            self.jud = 'p'
        if tag == 'img':
            url = attrs[0][1]
            if url[0:6] != 'https:':
                url = 'https:' + url
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}
            img = get_html(url, headers)
            if not os.path.exists('img'):
                os.mkdir('img')
            expand_name = url.split('.')[-1]
            file_name = str(MyHTMLParser.count) + '_' + str(self.count) + '.' + expand_name
            path = 'img/' + file_name
            with open(path, 'wb') as f:
                f.write(img)
            self.count += 1
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('![](%s)' %  path)
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('\n')
        if tag == 'li':
            self.jud = 'li'
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('* ')
        if tag == 'span' and ('class', 'marked') in attrs:
            self.ex = self.jud
            self.jud = 'span'

    def handle_data(self, data):
        if self.jud != 'span':
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write(data)
        else:
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('`' + data + '`')

    def handle_endtag(self, tag):
        if tag != 'span':
            with open(self.title, 'a', encoding='utf-8') as f:
                f.write('\n')
            self.jud = ''
        else:
            self.jud = self.ex


def main():
    url = 'https://www.runoob.com/markdown/md-tutorial.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}
    # print(get_content(url, headers))
    url_list = get_url_list(url, headers)
    for k, v in url_list.items():
        html = get_content(v, headers)
        p = MyHTMLParser(k)
        p.feed(html)
        print('第%d篇完成！' % MyHTMLParser.count)


def get_content(url, headers):
    """
    得到文章主体
    :param s: str
    :return: str
    """
    html = get_html(url, headers).decode('utf-8')
    bs = BeautifulSoup(html, 'lxml')
    main_contents = bs.find_all('div', class_='container main')[0]
    content = main_contents.find_all('div', class_='article-body')[0].prettify()
    return content


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    html = res.content
    return html


def get_url_list(url, headers):
    """
    获取URL列表
    :param s: str
    :return: dict
    """
    html = get_html(url, headers).decode('utf-8')
    bs = BeautifulSoup(html, 'lxml')
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