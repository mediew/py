import json
import requests
from lxml import etree
import pandas as pd


url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
}
res = requests.get(url, headers=headers)
html = etree.HTML(res.text)
result = html.xpath('//script[@type="application/json"]/text()')
# print(type(result))    # 此时result为list类型
result = result[0]
# print(type(result))    # 此时为字符串类型
result = json.loads(result)
# print(type(result))      # json.loads()将其转换为dict类型
result = result['component'][0]['caseList']  # 全国各地的人数
'''
观察字典结构发现以下对应关系：
area:省直辖市特别行政区
city:地级市
died:死亡人数
crued：治愈人数
confirmedRelative:累计确诊的增量
cruedRelative:治愈的增量
curConfirm:现有确诊
curConfirmRelative：现有确诊的增量
diedRelative:死亡的增量
'''
# for i in result:
#     print(i, '\n')
#     print('*' * 20, '\n')
#     for k in i.keys():
#         print(k)
provance_lst = []
dic = {}
for provance in result:
    provance_lst = [provance['confirmed'], provance['died'], provance['crued'],
                    provance['curConfirm'], provance['confirmedRelative'], provance['curedRelative'],
                    provance['diedRelative'], provance['curConfirmRelative']]
    index = 0
    for i in provance_lst:
        if not i:
            provance_lst[index] = '0'
        provance_lst[index] = int(provance_lst[index])
        index += 1
    dic[provance['area']] = provance_lst
    provance_lst = []

index = ['累计确诊', '累计死亡', '累计治愈', '现有确诊', '累计确诊的增量', '治愈的增量', '死亡的增量', '现有确诊的增量']
df = pd.DataFrame(index=index, data=dic)
print(df.head(5))
'''
confirmed
died
crued
relativeTime
confirmedRelative
diedRelative
curedRelative
asymptomaticRelative
asymptomatic
curConfirm
curConfirmRelative
icuDisable
area
subList
'''