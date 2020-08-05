import requests
from bs4 import BeautifulSoup as bs
import ffmpy3
import os
from multiprocessing.dummy import Pool as tp


def main():
    search_url = r'http://www.okzy.co/index.php?m=vod-search'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
    }
    search_data = {
        'wd': '越狱第一季',
        'submit': 'search'
    }
    url = getURL(search_url, search_data, headers)
    content_dic = get_content(url, headers)
    # print(content_dic)
    video_dir = '越狱-第一季（完结）'
    if video_dir not in os.listdir('./'):
        os.mkdir(video_dir)
    downVideo(content_dic)
    print('全部完成！')


def getURL(search_url, search_data, headers):
    s_res = requests.post(search_url, data=search_data, headers=headers)
    s_html = s_res.text
    # print(search_res.text)
    search_html = bs(s_html, 'lxml')
    # print(search_html)
    result = search_html.find_all('span', class_='xing_vb4')
    print(result)
    # print(result[0].a['href'])
    base_url = 'http://www.okzy.co'
    url = base_url + result[0].a['href']
    return url


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    html = res.text
    return html


def get_content(url, headers):
    html = get_html(url, headers=headers)
    soup = bs(html, 'lxml')
    content = soup.find_all('div', id='1')
    if not content:
        content = '暂无'
    else:
        content = content[0].find_all('li')
        dic = {}
        for i in content:
            dic[i.get_text()[:4]] = i.input['value']
    print(dic)
    return dic


def downVideo(dic):
    for k,v in dic.items():
        name = os.path.join('./越狱-第一季（完结）', k + '.mp4')
        ffmpy3.FFmpeg(inputs={v:None}, outputs={name:None}).run()
        print(k + '完成！')


if __name__ == '__main__':
    main()