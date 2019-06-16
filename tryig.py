# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:40:11 2019

@author: user
"""
import re
import json
import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
#以下為單個文章連結下載照片
'''
url = input("請輸入網址：")
res = requests.get(url)

soup = BeautifulSoup(res.text,'lxml')

json_part = soup.find_all("script", type="text/javascript")[3].string
json_part = json_part[json_part.find('=')+2:-1]
data = json.loads(json_part)
# as json

a = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']

#內含多張照片
try:
    for i in range(len(a['edge_sidecar_to_children']['edges'])):
        #print (a['edge_sidecar_to_children']['edges'][i]['node']['display_url'])
        image_url = a['edge_sidecar_to_children']['edges'][i]['node']['display_url']
        img_data = requests.get(image_url).content
        with open(str(i+1) + url.split('/')[4] +'.jpg', 'wb') as handler:
            handler.write(img_data)
        print("Done.")
#如果只有一張
except:
    image_url = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
    img_data = requests.get(image_url).content
    with open(url.split('/')[4]+'.jpg', 'wb') as handler:
        handler.write(img_data)
    print("Done.")
'''

'''
#取得目前頁面之各個文章連結
url = 'https://www.instagram.com/beauty.ig_/'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
json_part = soup.find_all("script", type="text/javascript")[3].string
json_part = json_part[json_part.find('=')+2:-1]
data = json.loads(json_part)
a = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
for i in range(len(a)):
    print(a[i]['node']['shortcode'])
'''
#qhash = 'f2405b236d85e8296cf30347c9f08c2a'
#aftercode = 'QVFDREV5WlY1dm94YzFkQUpIQzgzRGlkbnN2c0tEYTVHdmY1bDJXMnR3cU5BcUpuX19tQ0ZmQVNrSENyZ2daZEUtZkFwQmNaSUhqZDNpSVB4V0NxREJWbw%3D%3D"%7D'
url = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%227868856227%22%2C%22first%22%3A12%2C%22after%22%3A%22QVFDREV5WlY1dm94YzFkQUpIQzgzRGlkbnN2c0tEYTVHdmY1bDJXMnR3cU5BcUpuX19tQ0ZmQVNrSENyZ2daZEUtZkFwQmNaSUhqZDNpSVB4V0NxREJWbw%3D%3D%22%7D'
res = requests.get(url)
soup = BeautifulSoup(res.text,'lxml')
data = json.loads(soup.text)
print (data['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['shortcode'])
