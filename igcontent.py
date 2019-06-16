# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:27:45 2019

@author: Dai
"""

import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/niceguy331/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
json_part = soup.find_all("script", type="text/javascript")[3].string
json_part = json_part[json_part.find('=')+2:-1]
data = json.loads(json_part)
a = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
'''
#避免過長的程式碼
basic = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']

#文章內容
context = basic['edge_media_to_caption']['edges'][0]['node']['text']

#按讚數
likes = basic['edge_media_preview_like']['count']

#留言數
comments = basic['edge_media_to_parent_comment']['edges']
'''
#設定空清單吃資料
conlikes = []
concontexts = []
concomments = []
#a[i]['node']['shortcode']  文章連結
for i in range(len(a)):
    print(a[i]['node']['shortcode'],'按讚數:',a[i]['node']['edge_media_preview_like']['count'])
    conlikes.append(a[i]['node']['edge_media_preview_like']['count'])
    concontexts.append(a[i]['node']['shortcode'])
    concomments.append(a[i]['node']['edge_media_to_caption']['edges'][0]['node']['text'])
#print(max(conlikes))

aftercode = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

#print (aftercode)
#總文章數
count = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
userid = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']

for b in range(int(count/12)):
    rurl = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%22'+ userid +'%22%2C%22first%22%3A12%2C%22after%22%3A%22'+ aftercode.replace('=','') +'%3D%3D"%7D'
    rres = requests.get(rurl)
    rsoup = BeautifulSoup(rres.text,'html.parser')
    rdata = json.loads(rsoup.text)
    ra = rdata['data']['user']['edge_owner_to_timeline_media']['edges']
    for i in range(len(ra)):
        print(ra[i]['node']['shortcode'],'按讚數:',ra[i]['node']['edge_media_preview_like']['count'])
        conlikes.append(ra[i]['node']['edge_media_preview_like']['count'])
        concontexts.append(ra[i]['node']['shortcode'])
        #如果文章內容空白，就要跳過，不然會出錯
        if ra[i]['node']['edge_media_to_caption']['edges'] != []:
            concomments.append(ra[i]['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    aftercode = rdata['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    #print (aftercode)

print('最受歡迎的文章：',concontexts[conlikes.index(max(conlikes))],'這篇貼文有'+str(max(conlikes))+'個讚')
allconcomments=''.join(concomments)



'''
from wordcloud import WordCloud
import matplotlib.pyplot as plt
def igwordcloud(all_lyric):
    all_lyric = allconcomments
    # 設定停用字(排除常用詞、無法代表特殊意義的字詞)
    stopwords = {}.fromkeys(["沒有","一個","什麼","那個","作詞","阿信","作曲","五月天","怪獸"])
    # 產生文字雲
    wc = WordCloud(font_path="G:/Windows/Fonts/NotoSansCJKtc-Bold.otf", #設置字體
                   background_color="white", #背景顏色
                   max_words = 2000,        #文字雲顯示最大詞數
                   stopwords=stopwords,
                   width=300 ,height=180,
                   colormap='viridis')      #停用字詞
    wc.generate(all_lyric)
    # 視覺化呈現
    plt.imshow(wc)
    plt.axis("off")
    plt.figure(figsize=(3000,1800), dpi = 4000)
    plt.show()
    
igwordcloud(concomments)
''''