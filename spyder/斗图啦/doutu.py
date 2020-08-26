import os
import time
import parsel
import requests
from multiprocessing import Pool


def main():
    base_url = 'https://www.doutula.com/photo/list/?page='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'}
    print('开始爬取！\n·····························································')
    start = time.perf_counter()
    # p = Pool(4)   # 建立进程池
    c = count()
    for page in range(1, 11):
        print(next(c))
        url = base_url + str(page)
        html = get_html(url, headers)
        img_list = parse_html(html)
        # p.apply_async(down_img, args=(img_list, headers))
        down_img(img_list, headers)
        print(next(c))
    # p.close()
    # p.join()
    stop = time.perf_counter()
    t = stop - start
    print('总用时%d！' % t)
    print('爬取失败{}张:'.format(Count.c), '\n', Count.fail_list)


def get_html(url, headers):
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    return html


def parse_html(html):
    sel = parsel.Selector(html)
    result_list = sel.xpath('//a[@class="col-xs-6 col-sm-3"]')  # 获取所有a标签
    img_lst = []
    for a in result_list:
        img_url = a.xpath('./img/@data-original').extract_first()  # 获取图片url
        img_title = a.xpath('./img/@alt').extract_first()  # 获取图片标题
        img_type = img_url.split('.')[-1]
        img_name = img_title + '.' + img_type
        img_dict = dict(img_url=img_url, img_name=img_name)
        img_lst.append(img_dict)
    return img_lst  # 也可利用yield返回包含img_url和url_name的元组，但要注意写在for循环内


def down_img(img_lst, headers):
    for img_dict in img_lst:
        img_data = requests.get(img_dict['img_url'], headers=headers).content
        if not os.path.exists('img'):
            os.mkdir('img')
        try:
            with open('E:\\pynote\\spyder\\斗图啦\\img\\' + img_dict['img_name'], 'wb') as f:
                f.write(img_data)
                print('成功爬取图片：%s' % img_dict['img_name'])
        except Exception as e:
            print(e, '图片%s爬取失败！' % img_dict['img_name'])
            print('图片链接：%s' % img_dict['img_url'])
            c = Count(img_dict)


def count():
    n = 1
    while True:
        yield '开始爬取第%d页' % n
        yield '第%d页爬取完毕！' % n
        n += 1


class Count():
    c = 0
    fail_list = []

    def __init__(self, name):
        Count.c += 1
        Count.fail_list.append(name)


if __name__ == '__main__':
    """
    多进程下用时61秒，单进程下用时324秒!
    """
    main()
