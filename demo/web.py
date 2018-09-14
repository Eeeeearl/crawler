import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)

# 装饰器 给函数新增功能的
@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')

@app.route('/search')
def search():
    keyworld = request.args.get('kw')
    count = request.args.get('count')
    print(keyworld)
    cursor.execute("select * from images WHERE name LIKE '%{}%'".format(keyworld))
    data = cursor.fetchmany(int(count))
    return render_template('index.html', iamges = data)
    # print(data)

if __name__ == '__main__': # 防止外部调用
    db = pymysql.connect(host='127.0.0.1', port = 3306, db = 'db', user = 'root', passwd = '123456', charset = 'utf8',
                         cursorclass = pymysql.cursors.DictCursor)
    cursor = db.cursor()
    app.run(debug=True)