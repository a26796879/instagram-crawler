import requests, json, math
from datetime import timedelta, date

url = 'https://ibsearch.jejuair.net/jejuair/com/jeju/ibe/availHybris.do'

DetDate = date.today() + timedelta(days=7)

headers = {
'accept-language': 'zh-TW',
'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
'origin': 'https://www.jejuair.net',
'referer': 'https://www.jejuair.net/jejuair/tw/com/jeju/ibe/goAvail.do',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
#RET回程 DEP到達
def params(n):
    params = {
    'AdultPaxCnt': '1',
    'ChildPaxCnt': '0',
    'InfantPaxCnt': '0',
    'RouteType': 'I',
    'Language': 'TW',
    'ReturnSeatAvail': 'true',
    'PointsPayment': 'false',
    'FFPGrade': '',
    'TripType': 'RT',
    'DepDate': DetDate,
    'SegType': n,
    'DepStn': 'PUS',
    'ArrStn': 'TPE',
    'SystemType': 'IBE',
    "MULTIFLAG":"N","COUNTRYNAME":"TAIWAN","MAXAMT":'6000',"REGIONCODE":"NEA","CURRENCY":"TWD"}
    return params

res = requests.post(url , headers = headers , params = params('DEP'))
js = json.loads(res.text)
for i in range(7):
    price = js['Result']['Data']['AvailabilityDates'][i]['CheapestFare'] / 34.95
    date = js['Result']['Data']['AvailabilityDates'][i]['Date']
    print(math.ceil(price),date)


