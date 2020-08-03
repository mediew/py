from bs4 import BeautifulSoup
from urllib import request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re
import xlwt

def main():
    url = 'https://movie.douban.com/top250?start='
    # html = getHtml(url)
    data = parseHtml(url)
    # print(data)
    # '''
    savepath = 'db250_hp.xls'
    save2xls(data, savepath)
    # '''

def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    req = request.Request(url, headers = headers)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def parseHtml(url):
    lst = []
    for i in range(10):
        html = getHtml(url + str(25 * i))
        parser = MyHTMLParser()
        parser.feed(html)
        lst.extend(parser.lst)
    return lst

def save2xls(data, savepath):
    book = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = book.add_sheet('dbmovietop250', cell_overwrite_ok = True)
    sheet.write(0, 0, 'dbmovietop250')
    sheet_head = ['ID', '中文名', '外文名', '详情', '评分', '评分人数', '评价', '海报链接', '电影详情链接']
    for i in range(len(sheet_head)):
        sheet.write(1, i, sheet_head[i])
    for i in range(len(data)):
        sheet.write(i + 2, 0, data[i]['ID'])
        sheet.write(i + 2, 1, data[i]['中文名'])
        sheet.write(i + 2, 2, data[i]['外文名'])
        sheet.write(i + 2, 3, data[i]['详情'])
        sheet.write(i + 2, 4, data[i]['评分'])
        sheet.write(i + 2, 5, data[i]['评分人数'])
        sheet.write(i + 2, 6, data[i]['评价'])
        sheet.write(i + 2, 7, data[i]['海报链接'])
        sheet.write(i + 2, 8, data[i]['电影详情链接'])
    book.save(savepath)
    

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.dic = {}
        self.jud = ''
    

    def handle_starttag(self, tag, attrs):
        if tag == 'em' and ('class', '') in attrs:
            self.jud = 'ID'
        if tag == 'img' and ('width', '100') in attrs:
            self.dic['海报链接'] = attrs[2][1]
        
        if tag == 'a' and ('href') in attrs[0] and ('class', '') in attrs:
            self.dic['电影详情链接'] = attrs[0][1]
            
        if tag == 'span' and ('class', 'title') in attrs:
            self.jud = 'title'
            
        if tag == 'p' and ('class', '') in attrs:
            self.jud = 'info'

        if tag == 'span' and ('class', 'rating_num') in attrs:
            self.jud = 'rating'

        if tag == 'span' and attrs == []:
            self.jud = 'rating_num'

        if tag == 'span' and ('class', "inq") in attrs:
            self.jud = 'inq'
        

    def handle_data(self, data):
        if self.jud == 'ID':
            self.dic['ID'] = data
            self.jud = ''
            
        if self.jud == 'title':
            if re.match(r'^\s/\s.*', data):
                data = re.sub(r'\s/\s', '', data)
                self.dic['外文名'] = data
            else:
                
                self.dic['中文名'] = data
            self.jud = ''
            
        if self.jud == 'info':
            info = data.replace(' ', '')
            info = info.replace('\n', '')
            info = info.replace('\xa0\xa0\xa0', '')
            self.dic['详情'] = info
            self.jud = ''
                
        if self.jud == 'rating':
            self.dic['评分'] = data
            self.jud = ''

        if self.jud == 'rating_num':
            num = re.findall('(\d*)人评价', data)
            if num == []:
                self.dic['评分人数'] = '暂无'
            else:
                self.dic['评分人数'] = num[0]
            self.jud = ''

        if self.jud == 'inq':
            self.dic['评价'] = data
            if '外文名' not in self.dic:
                self.dic['外文名'] = '无'
            self.lst.append(self.dic)
            self.dic = {}
            self.jud = ''

if __name__ == '__main__':
    main()
        
