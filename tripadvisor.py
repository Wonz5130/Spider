# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 10:39:22 2018

@author: 王舟
"""




from bs4 import BeautifulSoup
import requests
import time
url = 'https://www.tripadvisor.cn/Attractions-g298184-Activities-c47-Tokyo_Tokyo_Prefecture_Kanto.html'
url_saves = 'https://www.tripadvisor.cn/Saves/1059341'
urls = ['https://www.tripadvisor.cn/Attractions-g298184-Activities-c47-oa{}-Tokyo_Tokyo_Prefecture_Kanto.html#FILTERED_LIST'.format(str(i)) for i in range(30,90,30)] #每30取下一个


headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cookie':'TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RS.1; TAUnique=%1%enc%3AcW%2BBFH3Ux0S5%2BGsErubcxEU1QZrQm7eS5Bf6IoqN7xY%3D; TASSK=enc%3AAK3syYheKZjICdsQT87VqgchhAH3fkOI05vTrak0LIWiDvksJATMzTuNh%2F76JCf3yRp18kLagisqFyRs3KduU41ArUH8pHJ%2BjCmFqmxI2k8GtfPKFZnH3le25DXJbFkFeg%3D%3D; _ga=GA1.2.1573661204.1520242811; _ym_uid=1520242818952361424; ServerPool=B; VRMCID=%1%V1*id.12019*llp.%2F*e.1521340553683; _gid=GA1.2.1062021013.1520735767; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CSPHRSess%2C%2C-1%7CHanaSession%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C3%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CSPHRPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TART=%1%enc%3AiJBOqCI3nvzR2rQtH3rIBZM4ASogystbLEDnGm4b0WoJZkgnjN5jFZwH8u5pb29ogWZ876bkBKg%3D; _ym_isad=1; _smt_uid=5aa4963b.3f88db27; CommercePopunder=SuppressAll*1520736093055; ki_r=; SecureLogin2=3.4%3AAF3LkROg25XhCAB5noZOC3MUOGxddZKAEzR1k2l%2Bc5x56zJiiVUAGxDNQRuKiirH%2BPgLhC8KgPmSZDkCx96PwnJ2eFuTg1fboQVgGd9Iamack2LDWR8g3Wt0QbUgUviKCL%2FlNu%2FdHYuFxRPWFx9lkPeuWZIUad7bGgspCkpczpVq2wyWLiZJj8QWoUr0C7%2BZfxWolChJgkmVx6ibYAVPhlA%3D; TAAuth3=3%3Aa1fa85ab3e0d5a38451029697fa27017%3AALz9Dkyl4nGVKGuoqn8oprVhumph%2FuwYIsS%2B1SqgEftQiS7bHDLOHBhelS93S5tp9EzHFJgESZxXMuaHdoB65Rw0AMvWHCEVz089BECtKWUxsH0qiOLfIogu24rJ9fgAp5po8OeEIWpKU4CVsgwIoY1OMvrNuv4VSBG0Wng3tcUqDzI7tccevhbRo%2BZnSUFQBg%3D%3D; TAReturnTo=%1%%2FAttraction_Review-g1066459-d1872416-Reviews-Tokyo_Skytree-Sumida_Tokyo_Tokyo_Prefecture_Kanto.html; _gat_UA-79743238-4=1; roybatty=TNI1625!AAfrEHDsJwObgWLxHHsUWYP2R9HeY8v9GEmnzS1gkCmW2QBepHQRgJRtaUUOmHyf3YiUUKwgKrYky114Qmo5J%2Bo7czjAVoCdbkhXNwttznTP87w3RiTZ6xkZPsftFA%2FkjXOOoy%2F3jNmppvKJ70iH74ftycpvzhc%2Fx7jtO4OXaTxs%2C1; ki_t=1520738215990%3B1520738215990%3B1520749332819%3B1%3B13; TASession=%1%V2ID.7C48C5CA85199EBD0B93C36CA99C7754*SQ.95*MC.12019*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Flink%3Furl%3DsyKPD-lpt9BqaT_0MoMLHqQLr_oKEUc3-9t-Mc208oSXDe0DbO3Vg6ib9HflgB03%26ck%3D5912%5C.2%5C.82%5C.266%5C.314%5C.309%5C.226%5C.124%26shh%3Dwww%5C.baidu%5C.com%26sht%3D99006304_7_oem_dg%26wd%3D%26eqid%3D80e241470004cc82000000055aa49606*LP.%2F*PR.39766%7C*LS.DemandLoadAjax*GR.70*TCPAR.43*TBR.22*EXEX.95*ABTR.92*PHTB.94*FS.93*CPU.17*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.F0C361058DD9BC4DA8B388381D08BA2C*LF.zhCN*FA.1*DF.0*MS.-1*RMS.-1*FLO.298184*TRA.true*LD.1872416; TAUD=LA-1520735753997-1*RDD-1-2018_03_10*LG-13571628-2.1.F.*LD-13571629-.....',
        }


# 定义一个获取热门目的地的函数
def get_attractions(url,data=None):
    wb_data = requests.get(url)  # 发出请求
    time.sleep(4)  # 4秒一次发出请求
    wb_data.encoding='utf-8' # 网页编码格式
    # print(wb_data)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # print(soup)
    # titles = soup.select('#BODYCON > div:nth-child(3) > div > div > h3')  # 在东京页面，热门目的地右击检查，点:copy selector
    # titles = soup.select('#BODYCON > div:nth-of-type(2) > div > div > h3')  # nth-child(1)改成nth-of-type(2)
    titles = soup.select('div.listing_title > a')  # 选择一类标题
    # print(titles)
    imgs = soup.select('img[width="180"]')  # 选择一类图片，限定长宽
    # print(imgs)
    cates = soup.select('div.p13n_reasoning_v2')  # 选择一类标签，多对一
    # print(cates)

    # 把它们放入一个字典中
    if data == None:
        for title,img,cate in zip(titles,imgs,cates):
            data = {
                    'title':title.get_text(),
                    'img':img.get('src'),
                    'cate':list(cate.stripped_strings), # 用stripped_strings去除多余空白内容
                    }
            print(data)

# get_attractions(url)
       

'''
# 定义一个获取收藏列表的函数,未成功
def get_favs(url,data = None):
    wb_data = requests.get(url_saves,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('a.location_summary')
    imgs = soup.select('img.media-left')
    metas = soup.select('location_parent')

    if data == None:
        for title,img,meta in zip(titles,imgs,metas):
            data = {
                    'title':title.get_text(),
                    'img':img.get('src'),
                    'meta':list(meta.stripped_strings)
                       }
            print(data)

# get_favs(url_saves)
'''



'''
# 从手机端获取请求，用chrome改成手机端访问,这里有问题
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1', #mobile device user agent from chrome
    }
mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
imgs = soup.select('div.centering_wrapper > img')
for i in imgs:
    print(i.get('src'))
'''




# print(urls)  #获取3页内容
for single_url in urls:
    get_attractions(single_url)









