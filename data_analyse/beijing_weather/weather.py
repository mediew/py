from bs4 import BeautifulSoup as bs
import re
import requests
import xlwt

'''
get_text() 方法,这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,并将结果作为Unicode字符串返回

'''


def main():
    year = [str(i) for i in range(2015, 2020)]
    month = ['0' + str(i) for i in range(1, 10)] + [str(i) for i in range(10, 13)]
    data = []
    for y in year:
        for m in month:
            url = geturl(y, m)
            data += getData(url)
    savepath = 'weather.xls'
    saveData2xls(data, savepath)


def saveData2xls(data, savepath):
    book = xlwt.Workbook(encoding = 'utf-8', style_compression = 0)
    sheet = book.add_sheet('beijing_weather', cell_overwrite_ok = True)
    firstRow = ['日期', '最高气温', '最低气温', '天气', '风向']
    for c in range(5):
        sheet.write(0, c, firstRow[c])
    for n in range(len(data)):
        for i in range(5):
            sheet.write(n + 1, i, data[n][firstRow[i]])
    book.save(savepath)


def geturl(y, m):
    baseurl = r'http://lishi.tianqi.com/beijing/'
    back = '.html'
    result = baseurl + y + m + back
    return result


def getData(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'
        }
    res = requests.get(url, headers = headers)
    html = res.text
    soup = bs(html, 'html.parser')
    # print(soup)
    ul = soup.find('ul', 'thrui')
    date = []
    for i in ul.find_all('div', "th200"):
        date.append(i.get_text().strip())
    htemp = []
    for i in ul.find_all('div', 'th140')[::4]:
        htemp.append(i.get_text())
    ltemp = []
    for i in ul.find_all('div', 'th140')[1:][::4]:
        ltemp.append(i.get_text())
    tq = []
    for i in ul.find_all('div', 'th140')[2:][::4]:
        tq.append(i.get_text())
    fx = []
    for i in ul.find_all('div', 'th140')[3:][::4]:
        fx.append(i.get_text())

    data = []
    dic = {}
    for i in range(len(date)):
        data.append({
            '日期' : date[i],
            '最高气温' : htemp[i],
            '最低气温' : ltemp[i],
            '天气' : tq[i],
            '风向' : fx[i],
            })
    '''
    for i in list(range(0, 30)):
        dic['日期'] = date[i]
        dic['最高气温'] = htemp[i]
        dic['最低气温'] = ltemp[i]
        dic['天气'] = tq[i]
        dic['风向'] = fx[i]
        data.append(dic)
        dic = {}        # 注意：必须把dic归零！若无这一步，则之前的i为引用，当进行到最后一步时才计算，此时i指向29，则之前的i的值全部为29！这一步归零后，将及时计算i的值。
    '''
    return data


if __name__ == '__main__':
    main()


