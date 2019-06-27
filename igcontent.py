# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 14:27:45 2019

@author: Dai
"""
import time
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/oppsweiiiii/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
json_part = soup.find_all("script", type="text/javascript")[3].string
json_part = json_part[json_part.find('=')+2:-1]
data = json.loads(json_part)
a = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
'''
#文章內容
context = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
#按讚數
likes = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_preview_like']['count']
#留言數
comments = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_parent_comment']['edges']
'''
#設定空清單吃資料
conlikes = []
concontexts = []
concomments = []

#a[i]['node']['shortcode']  文章連結
for i in range(len(a)):
    timeArray = time.localtime(a[i]['node']['taken_at_timestamp'])
    print(a[i]['node']['shortcode'],'按讚數:',a[i]['node']['edge_media_preview_like']['count'],'發文時間:',time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
    conlikes.append(a[i]['node']['edge_media_preview_like']['count'])
    concontexts.append(a[i]['node']['shortcode'])
    concomments.append(a[i]['node']['edge_media_to_caption']['edges'][0]['node']['text'])

aftercode = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
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
        timeArray = time.localtime(ra[i]['node']['taken_at_timestamp'])
        print(ra[i]['node']['shortcode'],'按讚數:',ra[i]['node']['edge_media_preview_like']['count'],'發文時間:',time.strftime("%Y-%m-%d %H:%M:%S", timeArray))
        conlikes.append(ra[i]['node']['edge_media_preview_like']['count'])
        concontexts.append(ra[i]['node']['shortcode'])
        #如果文章內容空白，就要跳過，不然會出錯
        if ra[i]['node']['edge_media_to_caption']['edges'] != []:
            concomments.append(ra[i]['node']['edge_media_to_caption']['edges'][0]['node']['text'])
    aftercode = rdata['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    #print (aftercode)

print('最受歡迎的文章：',concontexts[conlikes.index(max(conlikes))],'這篇貼文有'+str(max(conlikes))+'個讚')
allconcomments=''.join(concomments)
