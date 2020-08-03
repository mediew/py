import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

con = sqlite3.connect('movie250.db')
cur = con.cursor()
sql = 'select inq from movie250'
data = cur.execute(sql)
text = ''
for item in data:
    text += item[0]
# print(text)
cur.close()
con.close()

cut = jieba.cut(text)
str = ' '.join(cut)
print(cut)
img = Image.open('fyj.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='simsun.ttc'
)
wc.generate_from_text(str)
plt.figure(1)
plt.imshow(wc)
plt.axis('off')
plt.show()
plt.savefig('wc.png')


