# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:31:38 2018

@author: 王舟
"""




from bs4 import BeautifulSoup
import requests
import time
import random
import urllib.request # python3中应用urllib.request
import re
url = 'https://movie.douban.com/celebrity/1027883/photos/?type=C&start=0&sortby=like&size=a&subtype=a'
urls= ['https://movie.douban.com/celebrity/1027883/photos/?type=C&start={}&sortby=like&size=a&subtype=a'.format(str(i)) for i in range(0,1020,30)]

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }


# 获取页面信息
def getHtml(url):
    page = urllib.request.urlopen(url)  # 打开页面
    time.sleep(1)
    html = page.read()  # 获取目标页面的源代码
    return html
# print(html)

'''
def getnum():
    for i in range(1020):
        yield i
'''

# 通过正则获取图片
def getImg(html):
    reg = r'src="(.+?\.jpg)" '  # 正则表达式筛选目标图片格式，有些是'data-original="(.+?\.jpg)"'
    imgre = re.compile(reg)
    html=html.decode('utf-8') # python3要加上这句话
    imglist = re.findall(imgre,html)
    #x = 1
    for imgurl in imglist:
        #urllib.request.urlretrieve(imgurl,'D:/Code/Python爬虫/jcw/%s.jpg' %x) # 放入目录
        urllib.request.urlretrieve(imgurl,'D:/Code/Python爬虫/jcw/%s.jpg' %random.randint(1,1020)) # 放入目录
        #x+=1
    return imglist
# print(getImg)
    
# 把图片保存到本地
def saveImg(url):
    for i,url in enumerate(urls):
        with open('./'+str(i)+'.jpg','wb') as f:  # 用二进制打开才不会有马赛克
            f.write(requests.get(url).content)

for single_url in urls:
    html = getHtml(single_url)
    print(getImg(html))
    saveImg(single_url)