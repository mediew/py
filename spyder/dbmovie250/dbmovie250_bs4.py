from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import sqlite3


# 爬虫学习笔记
# 查找筛选的方法：
'''
list = bs.select('title')   #查找标签'title'
list = bs.select('.mnav')   #查找类名'mnav'
list = bs.select('#u1')     #查找id=u1
list = bs.select("a[class = 'bri']")     #查找属性(attrs)class='bri'
list = bs.select('head > title')         #查找子标签
list = bs.select('.mnav ~ .bri')         #查找和mnav同级的兄弟标签为'bri'
'''
# 正则表达式
'''
re.sub('a', 'A', 'abcdea')   #找到a用A替换

'''

findLink = re.compile(r'<a href="(.*?)">')      # 创建正则表达式匹配对象，匹配电影链接
findImgSrc = re.compile(r'<img alt.*src="(.*?)" width="100"/>', re.S)             # 匹配图片链接
findTitle = re.compile(r'<span class="title">(.*?)</span>')       #影片标题
findRate = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')         #评分
findInq = re.compile(r'<span class="inq">(.*?)</span>')         #概况
# findBd = re.compile(r'<p class="">(.*))</p>', re.S)          #相关信息



def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    # 2.解析网页
    data = getData(baseurl)
    # print(data)
    # 3.保存数据
    savepath = 'movie250.db'
    # savepath = 'movie250.xls'
    saveData2DB(data, savepath)


def getData(baseurl):
    data = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            # print(item)          # 测试
            item = str(item)
            link = re.findall(findLink, item)[0]
            # print(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            imgSrc = imgSrc.replace('.jpg', '.webp')
            title = re.findall(findTitle, item)
            if len(title) > 1:
                cntitle = title[0]
                othertitle = re.sub(r'\xa0/\xa0', '', title[1])

            else:
                cntitle = title[0]
                othertitle = '无其他名'
            rate = re.findall(findRate, item)[0]
            inq = re.findall(findInq, item)
            if inq == []:
                inq = '暂无'
            else:
                inq = re.findall(findInq, item)[0]
            # bd = re.findall(findBd, item)[0]
            # bd = re.sub('<br(\s+)?>(\s+)?', ' ', bd).strip()
            data.append({
                'infolink': link,
                'piclink': imgSrc,
                'cntitle': cntitle,
                'othertitle': othertitle,
                'rate': rate,
                'inq': inq
            })
    return data

def askURL(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    request = urllib.request.Request(url, headers = headers)
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        return html
    except urllib.error as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        


# 3.1保存数据到excel
def saveData2xls(data, savepath):
    book = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = book.add_sheet('dbmovie250', cell_overwrite_ok = True)
    firstRow = ['排名', '中文名', '其他名', '评分', '概述', '电影详情页', '电影海报']
    for c in range(7):
        sheet.write(0, c, firstRow[c])
    for fc in range(250):
        sheet.write(fc + 1, 0, fc + 1)
    for n in range(len(data)):
        sheet.write(n + 1, 1, data[n]['cntitle'])
        sheet.write(n + 1, 2, data[n]['othertitle'])
        sheet.write(n + 1, 3, data[n]['rate'])
        sheet.write(n + 1, 4, data[n]['inq'])
        sheet.write(n + 1, 5, data[n]['infolink'])
        sheet.write(n + 1, 6, data[n]['piclink'])
    book.save(savepath)
    

# 3.2保存数据到数据库
def saveData2DB(data, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for movie in data:
        row = []

        row.append('"'+movie['cntitle']+'"')
        row.append('"'+movie['othertitle']+'"')
        row.append('"'+movie['infolink']+'"')
        row.append('"'+movie['piclink']+'"')
        row.append('"'+movie['rate']+'"')
        row.append('"'+movie['inq']+'"')
        print(','.join(row))

        sql = '''
            insert into movie250(cntitle, othertitle, infolink, piclink, rate, inq)
            values(%s)
        ''' % ','.join(row)

        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()



# 创建数据库
def init_db(dbpath):
    sql = '''
    create table movie250
    (
    id integer primary key autoincrement,
    cntitle text,
    othertitle text,
    infolink text,
    piclink text,
    rate numeric,
    inq text
    )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
