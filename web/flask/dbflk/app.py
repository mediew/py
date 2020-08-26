from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    # return render_template('index.html')
    return index()


@app.route('/list')
def list():
    datalist = []
    con = sqlite3.connect('movie250.db')
    cur = con.cursor()
    sql = 'select * from movie250'
    data = cur.execute(sql)
    datalist = data
    # cur.close()
    # con.close()
    return render_template('list.html', movies = datalist)


@app.route('/score')
def score():
    score = []   # 评分有多少种
    num = []
    con = sqlite3.connect('movie250.db')
    cur = con.cursor()
    sql = 'select rate, count(rate) from movie250 group by rate'
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    # cur.close()
    # con.close()
    return render_template('score.html', score = score, num = num)


@app.route('/wordcloud')
def wordcloud():
    return render_template('wordcloud.html')


@app.route('/team')
def hello_world():
    return render_template('team.html')


if __name__ == '__main__':
    app.run()
