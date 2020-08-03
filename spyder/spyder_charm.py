from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error

findcode = re.compile(r'<code class="php">(.*?)</code>', re.S)
# findcode2 = re.compile('</span>"(.*)"', re.S)

def main():
    baseurl = 'https://www.wanhebin.com/software/107.html'
    getData(baseurl)
    
def getData(url):
    data = []
    html = askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    for item in soup.find_all('code', class_="php"):    # span class="hljs-number"
        code = re.findall(findcode, str(item))[0]
        print(code)
    
    # print(soup.find_all('code', class_="php"))


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
            
            
if __name__ == '__main__':
    main()
