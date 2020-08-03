import urllib

from bs4 import BeautifulSoup as bs
import re
import requests
import urllib
import sqlite3

def main():
    front = r'https://search.51job.com/list/170200,000000,0000,00,9,99,python,2,'
    back = r'.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
    urlist = urlst(front, back, 1)
    data = []
    for u in urlist:
        infolinklst = getinfolink(u)
        for ur in infolinklst:
            html = gethtml(ur)
            data.append(pars(html))

    print(data)
    # save2db(data)


def urlst(f, b, n):
    ulst = []
    lst = [i + 1 for i in range(n)]
    for i in lst:
        url = f + str(i) + b
        ulst.append(url)
    return ulst


def getinfolink(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'
    }
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    soup = bs(html, 'html.parser')
    findinfolink = soup.find_all(href=re.compile("s=01&t=0"), onmousedown="")
    infolinklst = [i['href'] for i in findinfolink]
    return infolinklst


def gethtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'
    }
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    return html


def pars(html):
    soup = bs(html, 'html.parser')
    post = soup.h1['title']
    wage = soup.find('strong').contents
    req = soup.find('p', 'msg ltype')['title'].strip().replace('\xa0', '')
    dy = ''.join([i.contents[0] for i in soup.find_all('span', 'sp4')])
    try:
        zwlst = [str(i.contents[0]) for i in soup.find_all('div', 'bmsg job_msg inbox')[0].find_all('p')[0:-2]]
        zwstr = ''
        for i in zwlst:
            zwstr += i
        zwstr = zwstr.replace('<br/>', '').replace('\xa0', '')
    except:
        print('indexError')
        zwstr = ''
    return {'职位': post, '工资': wage, '要求': req, '待遇': dy, '职位信息': zwstr}


if __name__ == '__main__':
    main()