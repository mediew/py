from flask import Flask, render_template, request
import datetime

app = Flask(__name__)


# # 路由解析，通过用户访问的路径返回相应的内容
# @app.route('/')
# def index():
#     return render_template("index.html")   # 返回网页模板


# 向页面传递一些变量
@app.route('/')
def index():
    time = datetime.date.today()
    name = ['小李', '小王', "小牛"]
    task = {'任务': '打扫卫生', "时间": '3小时'}
    return render_template("index.html", var = time, list = name, task = task)    # jinjia把渲染后的html文件发出去，所以浏览器看到的源代码var已经被替换成2020-01-01


# 表单提交
@app.route('/test/register')
def register():
    return render_template('test/register.html')


# 表单接受的路由，需要指定methods为post
@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        resul = request.form
        return render_template('test/result.html', result = resul)


# 通过路径获取字符串参数
@app.route('/user/<name>')
def welcome0(name):
    return '你好，%s!' % name


# 通过路径获取整数型参数，此外还有浮点型参数
@app.route('/user/<int:id>')
def welcome1(id):
    return '你好，第%d号会员!' % id
# 路由路径不可重复，用户通过唯一的路径访问特定的网页


if __name__ == '__main__':
    app.run(debug = True)     # debug模式开启后，保存文件后可以试试显示修改过的内容
