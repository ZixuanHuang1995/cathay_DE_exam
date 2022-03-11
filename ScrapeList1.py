
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
import pymongo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["591db"]
mycol = mydb["rent"]
myList = mydb["urlList"]

#設定driver
options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome('/Users/kensmacbook/Desktop/cathay_DE_exam/chromedriver', chrome_options = options)
driver.get("https://rent.591.com.tw/?region=1")
driver.implicitly_wait(30)

count = int(driver.find_elements_by_xpath('//*[@id="rent-list-app"]/div/div[3]/div/section[4]/div/a[7]')[0].text)
originCount = count

while(count):
    try:
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located((By.CLASS_NAME, 'pageNext')))
        print("---afterWait---")
        LinkData = {'page': originCount-count+1 , 'url': []} #存放one page的所有url
        for i in range(30):
            link = driver.find_elements_by_xpath('//*[@id="rent-list-app"]/div/div[3]/div/section[3]/div/section[' + str(i+1) + ']/a')
            url = link[0].get_attribute('href')
            print(url)
            LinkData["url"].append(url)
        myList.insert_one(LinkData) #load to db
        print("page: " + str(originCount-count+1) + " done")
        try: #點擊下一頁
            button = driver.find_element_by_class_name('pageNext')
            button.click()
            count -= 1
        except: #if點擊下一頁失敗then等待5秒讓網頁完全載入
            print("sleep")
            sleep(5)
            button = driver.find_element_by_class_name('pageNext')
            button.click()
            count -= 1
    except:
        print("page: " + str(originCount-count+1) + " error")
        driver.close()
