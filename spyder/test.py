from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error

findLink = re.compile(r'<a href="(.*?)">')      # 创建正则表达式匹配对象，匹配电影链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)             # 匹配图片链接
findTitle = re.compile(r'<span class="title">(.*?)</span>')       #影片标题
findRate = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')         #评分
findInq = re.compile(r'<span class="inq">(.*?)</span>')         #概况
# findBd = re.compile(r'<p class="">(.*?)</p>', re.S)          #相关信息



def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    print(getData(baseurl))

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


def getData(baseurl):
    data = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askURL(url)
        # 逐一解析数据
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_ = 'item'):
            # print(item)          # 测试
            item = str(item)
            link = re.findall(findLink, item)[0]
            # print(link)
            imgSrc = re.findall(findImgSrc, item)[0]
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
                '影片详情页':link,
                '图片下载页':imgSrc,
                '中文名':cntitle,
                '其他名':othertitle,
                '评分':rate,
                '概述':inq
            })
    return data
    
if __name__ == '__main__':
    main()
