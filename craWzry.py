# -*-coding:utf-8-*-
import os
import requests

url = 'http://pvp.qq.com/web201605/js/herolist.json'

# 发送请求 获取响应
html = requests.get(url)
# print(html.text)
html_json = html.json() #转化为json格式
# html_json = json.loads(html.text)
# print(html_json)
#提取英雄的名字和数字
hero_name = list(map(lambda x:x['cname'],html_json))
hero_number = list(map(lambda x:x['ename'],html_json))
print(hero_name,hero_number)

# os.mkdir("E:\\mycode\\PySpace\\demo\\crawler\\picture\\" + "张飞")

def main():
    ii = 0
    for v in hero_number:
        os.mkdir("E:\\mycode\\PySpace\\demo\\crawler\\picture\\"+hero_name[ii]) # 这里是创建文件夹用的
        os.chdir("E:\\mycode\\PySpace\\demo\\crawler\\picture\\"+hero_name[ii]) # 这里是进入文件夹用的
        ii= ii+ 1
        for u in range(12): # range 从0 到12
            onehero_links = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(v)+'/'+str(v)+'-bigskin-'+str(u)+'.jpg'
            im = requests.get(onehero_links)
            if im.status_code == 200:
                # 对文件的打开方式要以 二进制 的形式，“wb”
                # open(str(u),'wb').write(im.content)
                pic_name = str(u)+'.jpg'
                with open(pic_name,'wb')as file:
                    file.write(im.content)
            # else:
            #     print('false:'+str(u)+' and '+str(im.status_code))

main()