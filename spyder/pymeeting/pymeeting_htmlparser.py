from bs4 import BeautifulSoup
import re
from urllib import request
import xlwt
from html.parser import HTMLParser
from html.entities import name2codepoint


def main():
    url = 'https://www.python.org/events/python-events/'
    html = gethtml(url)
    data = parsehtml(html)
    print(data)
    # '''
    savepath = 'pymeeting.xls'
    save2xls(data, savepath)
    # '''


def save2xls(data, savepath):
    book = xlwt.Workbook(encoding = 'utf-8')
    sheet = book.add_sheet('pymeeting')
    sheet.write(0, 0, 'pymeeting')
    sheet_head = ['title', 'year', 'datetime', 'location']
    for i in range(len(sheet_head)):
        sheet.write(1, i, sheet_head[i])
    for x in range(len(data)):
        for y in range(4):
            index = sheet_head[y]
            sheet.write(x + 2, y, data[x][index])
    book.save(savepath)


def gethtml(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'}
    req = request.Request(url, headers = headers)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    return html


def parsehtml(html):
    # bs = BeautifulSoup(html, 'html.parser')
    # lst = bs.select("[class = 'event-title']")
    # return str(lst[0])
    # '''
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.lst
    # '''


class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.lst = []
        self.dic = {}
        self.jud = ''
    

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and ('class','event-title') in attrs:
            self.jud = 'title'
        
        if tag == 'time' and ('datetime') in attrs[0]:
            self.jud = 'datetime'
            
        if tag == 'span' and ('class', "say-no-more") in attrs:
            
            self.jud = 'year'
            
        if tag == 'span' and ('class', "event-location") in attrs:
            self.jud = 'location'
        

    def handle_data(self, data):
        if self.jud == 'title':
            self.dic['title'] = data
            self.jud = ''
            
        if self.jud == 'datetime':
            self.dic['datetime'] = data
            self.jud = ''
            
        if self.jud == 'year':
            if re.match(r'\s\d{4}', data):    # 后面还有span标签，所以要用正则匹配一下
                self.dic['year'] = data
            else:
                self.jud = ''
                
        if self.jud == 'location':
            self.dic['location'] = data
            self.lst.append(self.dic)
            self.jud = ''
            self.dic = {}
            



if __name__ == '__main__':
    main()


    
