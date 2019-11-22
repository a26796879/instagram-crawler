
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
options = Options()
#將chrome設定於背景執行

options.add_argument('--headless')
options.add_argument('--disable-gpu') # 允許在無GPU的環境下運行，可選
driver = webdriver.Chrome('G:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe', chrome_options = options)

url = "https://www.google.com/search?sxsrf=ACYBGNRPb9cvmU2J4PXN6PtaCCPDrJ99ZA:1574443574109&q=%E5%9F%BA%E9%80%B2&tbm=nws&source=univ&tbo=u&sxsrf=ACYBGNRPb9cvmU2J4PXN6PtaCCPDrJ99ZA:1574443574109&sa=X&ved=2ahUKEwjdndCvq_7lAhW1xIsBHapyDuEQt8YBKAF6BAgBEAY&biw=1913&bih=921"

driver.get(url)

import pygsheets
gc = pygsheets.authorize(service_file='F:\python codes\google_sheets_API\python-230518-9f6b02dba966.json')
sht = gc.open('For Taiwan')
wks = sht.sheet1

wks.clear()

starttime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    for p in range(1,50):
        for i in range(1,11):
            title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[1]/h3/a')
            href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[1]/h3/a').get_attribute('href')
            wks.append_table(values=[title.text,href])
            print(title.text,href)
            try:
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[2]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[2]/a').get_attribute('href')
                print(title.text,href)                
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[4]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[4]/a').get_attribute('href')
                print(title.text,href)                
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[6]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[6]/a').get_attribute('href')
                print(title.text,href)                
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[8]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[8]/a').get_attribute('href')
                print(title.text,href)
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[10]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[10]/a').get_attribute('href')
                print(title.text,href)
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[10]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[10]/a').get_attribute('href')
                print(title.text,href)
                wks.append_table(values=[title.text,href])
                
                title = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[12]/a')
                href = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+ str(i) +']/div/div[12]/a').get_attribute('href')
                print(title.text,href)
                wks.append_table(values=[title.text,href])
            except:
                print('')
        driver.find_element_by_xpath('//*[@id="pnnext"]/span[1]').click()
        sleep(2)
except:
    print('抓取完成')

wks.update_value('G1','更新時間：'+ starttime)

driver.quit()

'''
'//*[@id="rso"]/div/div[1]/div/div[1]/h3/a'
'//*[@id="rso"]/div/div[1]/div/div[2]/a'
'//*[@id="rso"]/div/div[1]/div/div[4]/a'
'//*[@id="rso"]/div/div[1]/div/div[6]/a'
'//*[@id="rso"]/div/div[1]/div/div[8]/a'
'//*[@id="rso"]/div/div[2]/div/div[1]/h3/a'
'//*[@id="rso"]/div/div[2]/div/div[2]/a'
'//*[@id="rso"]/div/div[2]/div/div[4]/a'
'//*[@id="rso"]/div/div[2]/div/div[6]/a'
'//*[@id="rso"]/div/div[2]/div/div[8]/a'
'//*[@id="rso"]/div/div[3]/div/div[2]/a'
'//*[@id="rso"]/div/div[3]/div/div[4]/a'
'//*[@id="rso"]/div/div[3]/div/div[6]/a'
'//*[@id="rso"]/div/div[3]/div/div[8]/a'
'//*[@id="rso"]/div/div[4]/div/div[2]/a'
'//*[@id="rso"]/div/div[4]/div/div[4]/a'
'//*[@id="rso"]/div/div[4]/div/div[6]/a'
'//*[@id="rso"]/div/div[4]/div/div[8]/a'
'''