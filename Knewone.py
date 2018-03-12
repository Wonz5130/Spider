# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 09:14:40 2018

@author: 王舟
"""



# 异步加载，往下刷，第二页内容在当前页面显示出来
from bs4 import BeautifulSoup
import requests
import time

url = 'https://knewone.com/things?page=2'

def get_page(url,data = None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    
    # print(soup)
    
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')
    
    if data == None:
        for img,title,link in zip(imgs,titles,links):
            data = {
                    'imgs':img.get('src'),
                    'title':title.get('title'),
                    'link':link.get('href')
                    }
            print(data)

def get_more_pages(start,end):
    for one in range (start,end):
        get_page(url+str(one))
        time.sleep(2)  # 反爬虫,设置爬取时间间隔


get_more_pages(1,3)