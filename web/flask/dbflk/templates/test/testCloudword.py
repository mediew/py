import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import sqlite3

con = sqlite3.connect(dbmovie)
cur = con.cursor()
sql = 'select inq from'
