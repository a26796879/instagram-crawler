# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:40:11 2019
<<<<<<< HEAD
=======

>>>>>>> b14bb778e85e2c527b9c340b5f95c31520c48c05
@author: user
"""
import os
import json
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
class igdownload():
    # 以下為單個文章連結下載照片
    def __init__(self):
        if not os.path.isdir(ID):
            os.makedirs(ID)
    def fromcontext(self, url):
        # url = input("請輸入網址：")
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'lxml')
        json_part = soup.find_all("script", type="text/javascript")[3].string
        json_part = json_part[json_part.find('=')+2:-1]
        data = json.loads(json_part)

        a = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
        # 如果有多張照片
        try:
            for i in range(len(a['edge_sidecar_to_children']['edges'])):
                # print (a['edge_sidecar_to_children']['edges'][i]['node']['display_url'])
                image_url = a['edge_sidecar_to_children']['edges'][i]['node']['display_url']
                img_data = requests.get(image_url).content
                with open('./'+ID+'/'+str(i+1) + url.split('/')[4] + '.jpg', 'wb') as handler:
                    handler.write(img_data)
                print("Done.")
        # 如果只有一張
        except:
            image_url = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
            img_data = requests.get(image_url).content
            with open('./'+ID+'/'+url.split('/')[4]+'.jpg', 'wb') as handler:
                handler.write(img_data)
            print("Done.")
# 取得第一頁之各個文章連結
ID = input('請輸入要抓取的帳號：')
url = 'https://www.instagram.com/' + ID + '/'
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
json_part = soup.find_all("script", type="text/javascript")[3].string

try:
    json_part = json_part[json_part.find('=')+2:-1]
    data = json.loads(json_part)
    a = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

    # 總文章數
    count = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
    userid = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']
    print('輸入的帳號為：',ID ,'共有',count,'篇貼文')

    for i in range(len(a)):
        print(a[i]['node']['shortcode'])
        igdownload().fromcontext('https://www.instagram.com/p/' +
                                 a[i]['node']['shortcode'] + '/')
    aftercode = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    # print (aftercode)

    # 總文章數
    count = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['count']
    userid = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']

    # 取得第二頁後各個文章連結
    for b in range(int(count/12)):
        rurl = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%22' + \
            userid + '%22%2C%22first%22%3A12%2C%22after%22%3A%22' + \
            aftercode.replace('=', '') + '%3D%3D"%7D'
        rres = requests.get(rurl, headers=headers)
        rsoup = BeautifulSoup(rres.text, 'html.parser')
        rdata = json.loads(rsoup.text)
        ra = rdata['data']['user']['edge_owner_to_timeline_media']['edges']
        for i in range(len(ra)):
            print(ra[i]['node']['shortcode'])
            igdownload().fromcontext('https://www.instagram.com/p/' +
                                     ra[i]['node']['shortcode'] + '/')
        aftercode = rdata['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        # print (aftercode)

    print('已全數下載完畢')
except:
    print('帳號輸入有誤(或此帳號設定不公開)')


