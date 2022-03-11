
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import pymongo
import threading
import concurrent.futures
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["591db"]
mycol = mydb["Rent"]
 
urls = []
cursor = list(mydb.urlList.find({}))
for page in cursor:
    for item in page['url']:
        urls.append(item)

#urls = urls[18611:]
AllCase = len(urls)
OriginAllCase = AllCase
print(AllCase)

def scrape(link):
    #開啟網頁
    print("start scraping: " + link)
    options = Options()
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome('/Users/kensmacbook/Desktop/cathay_DE_exam/chromedriver', chrome_options = options)
    driver.get(link)
    driver.implicitly_wait(30)
    #建立需求資料json
    try:
        Renter_and_RenterIdentity = driver.find_elements_by_xpath('//*[@id="rightConFixed"]/section/div[1]/div[2]/p[1]')[0].text
    except:
        Renter_and_RenterIdentity = 'none: none'
    Renter = Renter_and_RenterIdentity[Renter_and_RenterIdentity.index(" "):]
    RenterIdentity = Renter_and_RenterIdentity[:Renter_and_RenterIdentity.index(":")]
    try:
        ContactNumber = driver.find_elements_by_xpath('//*[@id="rightConFixed"]/section/div[2]/div/div[1]/span[2]')[0].text
    except:
        ContactNumber = 'none'
    try:
        Type = driver.find_elements_by_xpath('//*[@id="houseInfo"]/div[3]/span[7]')[0].text
    except:
        Type = 'none'
    try:
        State = driver.find_elements_by_xpath('//*[@id="houseInfo"]/div[3]/span[1]')[0].text
    except:
        State = 'none'
    try:
        GenderRequirements = driver.find_elements_by_xpath('//*[@id="service"]/div[3]/div/span')[0].text
    except:
        GenderRequirements = 'none'
    RentData = { "出租者": Renter, "出租者身份": RenterIdentity, "聯絡電話": ContactNumber, "型態": Type, "現況": State, "性別要求": GenderRequirements, "url": link}
    print(RentData)
    #Load to db
    mycol.insert_one(RentData)
    driver.close()
    print("---closed---")
    AllCase = AllCase-1

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(scrape, urls)
