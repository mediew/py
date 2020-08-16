import requests
from hashlib import md5
import random
import json


# 调用api无需headers等
appid = '20200816000544116'
secretKey = 'y7eXTKTk59mJhUu3IVwn'
api_url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
fromLang = 'auto'   #原文语种
toLang = 'zh'   #译文语种
salt = random.randint(32768, 65536)
q= 'apple'    # 翻译原文，q=query
sign = appid + q + str(salt) + secretKey
sign = md5(sign.encode()).hexdigest()     # 签名
'''用get方法实现
# myurl = api_url + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign      # 按照标准，URL只允许一部分ASCII字符，其他字符（如汉字）是不符合标准的，此时就要进行编码。
myurl = api_url + '?appid=' + appid + '&q=' + q + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign
res = requests.get(myurl)
print(json.loads(res.content))
'''
# 用post方法实现
headers = {'content-type': 'application/x-www-form-urlencoded'}
word = input('please input a Chinese word')
data = {
    'q': word,
    'from': 'zh',
    'to': 'en',
    'appid': appid,
    'salt': salt,
    'sign': md5((appid + word + str(salt) + secretKey).encode()).hexdigest()
}
res = requests.post(api_url, headers = headers, data=data)
print(res.content)
result = json.loads((res.content.decode('utf-8')))['trans_result'][0]
print('中文：', result['src'], '\n', '英文：', result['dst'])