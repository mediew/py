import requests

url = 'https://video.pearvideo.com/mp4/adshort/20200711/cont-1685309-15257784_adpkg-ad_hd.mp4'
headers = {
    'referer': 'https://www.pearvideo.com/video_1685309',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
requests = requests.get(url, headers = headers)
content = requests.content
with open('[pear_video]CEO_mask.mp4', 'wb') as f:
    f.write(content)

