import requests
from bs4 import BeautifulSoup as bs
import time
import sqlite3

'''
由于网站反扒设置，此脚本仅能爬取部分章节
Summary:
    soup.get_text("|", strip=True)  获取tag包裹的内容并去除前后的空格
    a['href']  返回a标签下href属性的值
    快捷键：输入main敲回车即可快速设置主函数
    re.findall()加上re.S参数可以匹配到换行符，即把换行符包含进去
    for key, value in urlst.items():可以迭代字典的key和value
    判断语句l == []等价于not l
'''

def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = res.text
    return html


def get_urlst():
    url = 'http://www.xbiquge.la/10/10489/'
    html = get_html(url)
    # print(html)
    soup = bs(html, 'html.parser')
    dd_lst = soup.find_all('dd')
    # print(ddlst)
    a_lst = [dd.find_all('a')[0] for dd in dd_lst]
    # print(alst)
    name_lst = [a.get_text() for a in a_lst]
    ref_lst = [a['href'] for a in a_lst]
    base_url = 'http://www.xbiquge.la'
    ref_lst = [base_url + i for i in ref_lst]
    # print(name_lst, ref_lst)
    urlst = dict(zip(name_lst, ref_lst))
    # print(urlst)
    return urlst


def get_content(url):
    html = get_html(url)
    soup = bs(html, 'html.parser')
    content = soup.find_all(id='content')
    if not content:
        content = '暂无'
    else:
        content = content[0].get_text()
    # print(content)
    return content


def save2db(data, dbpath):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    row = ['"' + data[0] + '"', '"' + data[1] + '"']
    # 由于下文对row进行join方法后不带“”号，而sqlite语句需要加双引号，故需再此处加上双引号

    sql = '''
        insert into acrj(title, content)
        values(%s)
    ''' % ','.join(row)

    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
    create table acrj
    (
    id integer primary key autoincrement,
    title text,
    content text
    )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


def main():
    urlst = get_urlst()
    path = 'bqg.db'
    init_db(path)
    for key, value in urlst.items():
        content = get_content(value)
        data = (key, content)
        save2db(data, path)
        time.sleep(1)
        print('%s：完成！' % key)


if __name__ == '__main__':
    main()
