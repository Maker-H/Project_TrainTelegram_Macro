# https://kminito.tistory.com/79?category=373099

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

korail_id = '' #korail number
korail_pwd = ''
korail_start_station = '동대구' 
korail_end_station = '서울'
korail_hour = 9 #hour ex)9, 11, 15 등
korail_month = 1 #month ex)1, 2, 4, 12 등
korail_day = 25 #day ex) 1, 4, 14, 29 등

#if hour, day, month is less than 10, add 0 in front of str
if korail_day < 10:
    korail_day = '0'+ str(korail_day)
else:
    korail_day = str(korail_day)

if korail_month < 10:
    korail_month = '0' + str(korail_month)
else:
    korail_month = str(korail_month)

if korail_hour < 10:
    korail_hour = '0' + str(korail_hour)
else:
    korail_hour = str(korail_hour)


# start webdriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome("/Users/hs_/Downloads/chromedriver_mac_arm64/chromedriver") # enter the path of the file
url = 'https://www.letskorail.com/korail/com/login.do'
driver.get(url) # enter the url of the page that I want to move to
driver.implicitly_wait(15) # wait until the page is loaded

# enter id and pwd
driver.find_element(By.ID, 'txtMember').send_keys(korail_id)
driver.find_element(By.ID, 'txtPwd').send_keys(korail_pwd)

# submit
driver.find_element(By.XPATH, '//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
driver.implicitly_wait(10)

# go to purchase page
url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'
driver.get(url)
driver.implicitly_wait(15)
time.sleep(1)

# close popup page - deprecated
# time.sleep(5)
# main = driver.window_handles
# driver.switch_to.window(main[1])
# driver.close()
# driver.switch_to.window(main[0])

#enter starting station
dep_stn = driver.find_element(By.ID, 'start')
dep_stn.clear() 
dep_stn.send_keys(korail_start_station)
driver.implicitly_wait(5)

#enter ending station
arr_stn = driver.find_element(By.ID, 'get')
arr_stn.clear()
arr_stn.send_keys(korail_end_station)
driver.implicitly_wait(5)


# enter stating date by using calender - still thinking
# driver.find_element(By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img').click()
# driver.implicitly_wait(5)
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[4]/td[4]').click()


# enter starting month
Select(driver.find_element(By.ID,"s_month")).select_by_value(korail_month)

# enter starting day
Select(driver.find_element(By.ID,"s_day")).select_by_value(korail_day)

# enter starting hour
Select(driver.find_element(By.ID,"s_hour")).select_by_value(korail_hour)
# Select(driver.find_element(By.ID,"time")).select_by_visible_text(str(korail_hour))


# submit
driver.find_element(By.XPATH,'//*[@id="center"]/form/div/p/a/img').click()
driver.implicitly_wait(5)
time.sleep(2)


# print train list
trains = driver.find_elements(By.CSS_SELECTOR, '#tableResult > tbody > tr')

for train in range(1, len(trains)*2 + 1, 2):
    
    for train_one_sec in range(3, 9):
        train_info = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child({train_one_sec})').text.replace('\n', ' ').replace('-', '')
        print(train_info, end=" ")
    # 가격    
    train_price = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td.guide365 > div > strong').text.replace('\n', ' ')
    
    train_time = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(14)').text.replace('\n', ' ')

    print(train_info, train_price, train_time)


# book only top 2 trains in list
is_reserved = True
while is_reserved: 
    for select_train in range(1, 5, 2):

        try:
            standard_seat = driver.find_element(By.CSS_SELECTOR, f'#tableResult > tbody > tr:nth-child({select_train}) > td:nth-child(6) > a:nth-child(1) > img').click()
            print("예약되었습니다")
            @todo 텔레그램에 예약되었다는 메세지 출력....
            is_reserved = False
            break
        except:
            pass
    if is_reserved:
        # if all train is reserved refresh again
        submit = driver.find_element(By.XPATH, '//*[@id="center"]/div[3]/p/a/img')
        driver.execute_script('arguments[0].click();', submit)
        driver.implicitly_wait(10)
    else:
        break
