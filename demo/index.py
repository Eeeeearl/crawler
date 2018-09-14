# -*-coding:utf-8-*-
import time
import requests
import re
import pymysql

# 连接数据库
db=pymysql.connect('127.0.0.1','root','123456','db',3306)
# 创建游标
cursor=db.cursor()
# cursor.execute("select * from images")
# print(cursor.fetchall())

# 获取图片
def getImageList(page=1):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    html = requests.get('http://www.doutula.com/photo/list/?page={}'.format(page),headers=header).text
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg,re.S)
    imageList = re.findall(reg,html) # 这里的数据类型是个列表 url+名字
    for image in imageList:
        imageurl = image[0]
        imagetitle = image[1]
        cursor.execute("insert into images(name,imageUrl) VALUES ('{}','{}')".format(imagetitle,imageurl))
        # print("loding %s" %imagetitle)
        db.commit()

# for i in range(110,1000): # 1000不会取到
#     print("第{}页".format(i))
#     time.sleep(3)
#     getImageList(i)