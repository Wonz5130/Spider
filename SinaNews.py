# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 20:52:31 2018

@author: 王舟
"""

'''
import requests
from bs4 import BeautifulSoup # 引入美丽汤
res = requests.get('http://news.sina.com.cn/c/nd/2018-02-22/doc-ifyrvspi0753024.shtml') # 请求用get命令
res.encoding='utf-8' # 网页编码格式

soup = BeautifulSoup(res.text,'html.parser') #将返回东西丢进美丽汤中，并指定html.parser

print(soup.select('.main-title')[0].text) # class用.  id用#
'''

'''
import requests
from bs4 import BeautifulSoup # 引入美丽汤
res = requests.get('http://news.sina.com.cn/') # 请求用get命令
res.encoding='utf-8' # 网页编码格式
soup = BeautifulSoup(res.text,'html.parser') #将返回东西丢进美丽汤中，并指定html.parser
a = soup.select('#syncad_1 h1 a') # 抓取要闻 h1表示选择所有h1标题 a表示选择超链接
for b in a: # 遍历所有要闻
    print(b.text,b['href']) # 循环打印标题和超链接
'''

'''
import requests
from bs4 import BeautifulSoup # 引入美丽汤
res = requests.get('http://news.sina.com.cn/c/nd/2018-02-22/doc-ifyrvspi0753024.shtml') # 请求用get命令
res.encoding='utf-8' # 网页编码格式
soup = BeautifulSoup(res.text,'html.parser') #将返回东西丢进美丽汤中，并指定html.parser
a = soup.select('#article p')
for b in a[:-1]: # 切片表达式，去掉最后一行
    print(b.text) # 打印新闻内容
'''

'''
import requests
from bs4 import BeautifulSoup # 引入美丽汤
result = {} # 字典
res = requests.get('http://news.sina.com.cn/c/nd/2018-02-22/doc-ifyrvspi0753024.shtml') # 请求用get命令
res.encoding='utf-8' # 网页编码格式
soup = BeautifulSoup(res.text,'html.parser') #将返回东西丢进美丽汤中，并指定html.parser

title = soup.select('.main-title')[0].text
result['title'] = title # 把标题放进字典

a = soup.select('#article p')
content = ' '
for b in a[:-1]: # 切片表达式，去掉最后一行
    content = content + b.text # 新闻标题+内容
    content = content.replace('\u3000','  ')  # 把\u3000换成空两格
result['content'] = content # 把内容放进字典



article_bottom = soup.select('#article-bottom')
article_bottom = article_bottom[0].text.replace('\n','') # 把\n换成无
result['editor'] = article_bottom # 把责任编辑放进字典

data = soup.select('.date')[0].text
#data[0].text.replace('\n','').split('\t','')
result['data'] = data #把时间放进字典

source = soup.select('.source')[0].text
result['source'] = source # 把文章来源放进字典
print(result)
'''

'''
import requests
import json # 引入json
res = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyrvspi0753024&group=0&compress=0&ie=gbk&oe=gbk&page=1&page_size=20&jsvar=loader_1519354505221_17791544')
#res.encoding='utf-8' # 网页编码格式
json_str = res.text.strip('var data=')
print(json.loads(json_str))
'''

'''
import re,json # 用正则表达式
import requests
url = 'http://news.sina.com.cn/c/nd/2018-02-22/doc-ifyrvspi0753024.shtml'
n = re.match('(.*)(doc-i)(.*)(\.shtml)',url)  # 分组取出url
n.groups()
common_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-%s&group=0&compress=0&ie=gbk&oe=gbk&page=1&page_size=20&jsvar=loader_1519354505221_17791544' % (n.group(3))
res = requests.get(common_url)
def getCommentsInfo(url):
    n = re.match('(.*)(doc-i)(.*)(\.shtml)',url)
    common_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-%s&group=0&compress=0&ie=gbk&oe=gbk&page=1&page_size=20&jsvar=loader_1519354505221_17791544' % (n.group(3))
    res = requests.get(common_url)
    json_str = res.text.strip('var data=') # 去掉var
    count = json.loads(json_str)['result']['count']['total']
    return count
getCommentsInfo('http://news.sina.com.cn/c/nd/2018-02-22/doc-ifyrvspi0753024.shtml') # 抓取评论数
'''



import requests,json,re
from bs4 import BeautifulSoup # 引入美丽汤

def getCommentsInfo(url): # 定义抓取评论数函数
    try:
        n = re.match('(.*)(doc-i)(.*)(\.shtml)',url)
        common_url = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-%s&group=0&compress=0&ie=gbk&oe=gbk&page=1&page_size=20&jsvar=loader_1519354505221_17791544' % (n.group(3))
        res = requests.get(common_url)
        json_str = res.text.strip('var data=') # 去掉var
        count = json.loads(json_str)['result']['count']['total']
        return count
    except Exception as e:
        print(e)
        return 0

res = requests.get('http://news.sina.com.cn/') # 请求用get命令
res.encoding='utf-8' # 网页编码格式
soup = BeautifulSoup(res.text,'html.parser') #将返回东西丢进美丽汤中，并指定html.parser
a = soup.select('#syncad_1 h1 a') # 抓取要闻 h1表示选择所有h1标题 a表示选择超链接
info_list = []
for b in a: # 遍历所有要闻
    print(b.text,b['href']) # 循环打印标题和超链接
    url = b['href']
    result = {} # 字典
    res = requests.get(url) # 请求用get命令
    res.encoding='utf-8' # 网页编码格式
    soup = BeautifulSoup(res.text,'lxml') #将返回东西丢进美丽汤中，并指定html.parser
    # 把标题放进字典
    # title = soup.select('.main-title')[0].text # 这一行有问题，list[0]没有值
    # result['title'] = title
    # 把内容放进字典
    a = soup.select('#article p')
    content = ' '
    for data in a[:-1]: # 切片表达式，去掉最后一行
        content = content + data.text # 新闻标题+内容
        #content = content.replace('\u3000','  ')  # 把\u3000换成空两格
    result['content'] = content
    # 把责任编辑放进字典
    # article_bottom = soup.select('#article-bottom')
    # article_bottom = article_bottom[0].text.replace('\n','') # 把\n换成无  # 这一行有问题，list[0]没有值
    # result['editor'] = article_bottom
    #把时间放进字典
    # data = soup.select('.date')[0].text # 这一行有问题，list[0]没有值
    # data[0].text.replace('\n','').split('\t','')
    # result['data'] = data
    # 把文章来源放进字典
    #s ource = soup.select('.source')[0].text # 这一行有问题，list[0]没有值
    # result['source'] = source
    # 获取评论数
    count = getCommentsInfo(url)
    result['count'] = count
    # 将新闻字典放入info_list列表中
    info_list.append(result)

#遍历info_list    
for info in info_list:
    print(info)

'''    
import pandas as pd
df = pd.DataFram(info_list)
df.to_excel('news.excel') # 导出为excel
'''