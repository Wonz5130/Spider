# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:38:35 2018

@author: 王舟
"""




from bs4 import BeautifulSoup
import requests
import time
import urllib.request # python3中应用urllib.request
import re
url = 'https://www.douban.com/photos/album/138194636/?start=0'
urls= ['https://www.douban.com/photos/album/138194636/?start={}'.format(str(i)) for i in range(0,54,18)]
# url = 'https://www.douban.com/photos/album/35398857/?start=0'
# urls =['https://www.douban.com/photos/album/35398857/?start={}'.format(str(i)) for i in range(0,36,18)]

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
        }
x = 1
# x = 84

'''
def get_pic(url):
    web_data = requests.get(url,headers = headers)
    time.sleep(4)
    soup = BeautifulSoup(web_data.text,'lxml')
    # print(soup)
    titles = soup.select('div.photo_wrap > a')  # 选择一类标题
    print(titles)
    imgs = soup.select('img[width="145"]')  # 选择一类图片，限定长宽
    # print(imgs)
    
# get_pic(url)
'''

'''
for single_url in urls:
    get_pic(single_url)
'''






# 获取页面信息
def getHtml(url):
    page = urllib.request.urlopen(url)  # 打开页面
    time.sleep(4)
    html = page.read()  # 获取目标页面的源代码
    return html


# print(html)

# 通过正则获取图片
def getImg(html):
    reg = r'src="(.+?\.jpg)" '  # #正则表达式筛选目标图片格式，有些是'data-original="(.+?\.jpg)"'
    imgre = re.compile(reg)
    html=html.decode('utf-8') # python3要加上这句话
    imglist = re.findall(imgre,html)
    for imgurl in imglist:
        global x
        urllib.request.urlretrieve(imgurl,'D:/Code/Python爬虫/xuruoxuan/%s.jpg' %x) # 放入目录
        x+=1
    return imglist
# print(getImg)
    
# 把图片保存到本地
def saveImg(url):
    for i,url in enumerate(urls):
        with open('./'+str(i)+'.jpg','wb') as f:
            f.write(requests.get(url).content)

for single_url in urls:
    html = getHtml(single_url)
    print(getImg(html))
    saveImg(single_url)




"""
import os
import requests
from bs4 import BeautifulSoup

all_url = []

def get_Imgs(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'lxml')

        for url in soup.find('ul', {'class':'photo_wrap'}).find_all('img'):
            all_url.append(url['src'])
        return all_url
    except:
        return "error"


def save_imgs():
    dir_name = 'pic'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        os.chdir(dir_name)
    try:
        for i,url in enumerate(all_url):
            with open('./' + str(i) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
    except:
        return "error"
def main():
    url = 'https://www.douban.com/photos/album/138194636/?start='
    try:
        for i in range(0,36,18):
            get_Imgs(url + str(i))
    except:
        return "error"
    save_imgs()


if __name__ == '__main__':
    main()
"""



