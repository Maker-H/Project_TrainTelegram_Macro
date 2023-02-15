# https://kminito.tistory.com/79?category=373099

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time
import pwd_token

korail_id = pwd_token.get_korailid()
korail_pwd = pwd_token.get_korailpwd()
korail_start_station = '구미'
korail_end_station = '서울'
korail_hour = 10
korail_month = 1
korail_day = 25

#앞에 달과 날이 10 미만이면 0 추가
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



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Chrome("/Users/hs_/Downloads/chromedriver_mac_arm64/chromedriver") # Webdriver 파일의 경로를 입력
url = 'https://www.letskorail.com/korail/com/login.do'
driver.get(url) # 이동을 원하는 페이지 주소 입력
driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림

# 아이디 비밀번호 입력
driver.find_element(By.ID, 'txtMember').send_keys(korail_id) # 회원번호
driver.find_element(By.ID, 'txtPwd').send_keys(korail_pwd) # 비밀번호


driver.find_element(By.XPATH, '//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
driver.implicitly_wait(10)

# 예매 페이지로 이동
url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketpr21100W_pr21110.do'
driver.get(url) # 이동을 원하는 페이지 주소 입력
driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림
time.sleep(1)

# 팝업 닫기 
time.sleep(3)
main = driver.window_handles
driver.switch_to.window(main[1])
driver.close()
driver.switch_to.window(main[0])

#출발지 입력
dep_stn = driver.find_element(By.ID, 'start')
dep_stn.clear() 
dep_stn.send_keys(korail_start_station)
driver.implicitly_wait(5)

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'get')
arr_stn.clear()
arr_stn.send_keys(korail_end_station)
driver.implicitly_wait(5)


# 출발 날짜 입력
# https://velog.io/@rkfksh/Selenium-click%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-element%EB%A5%BC-javascript-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-click%ED%95%98%EA%B8%B0
# driver.find_element(By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img').click()
# driver.implicitly_wait(5)
# time.sleep(1)
# driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[4]/td[4]').click()


# 출발 월 입력
Select(driver.find_element(By.ID,"s_month")).select_by_value(korail_month)

# 출발 일 입력 
Select(driver.find_element(By.ID,"s_day")).select_by_value(korail_day)

# 출발 시간 입력
Select(driver.find_element(By.ID,"s_hour")).select_by_value(korail_hour)
# Select(driver.find_element(By.ID,"time")).select_by_visible_text(str(korail_hour))


# 조회하기 클릭
driver.find_element(By.XPATH,'//*[@id="center"]/form/div/p/a/img').click()
driver.implicitly_wait(5)
time.sleep(2)


# 기차들 출력
trains = driver.find_elements(By.CSS_SELECTOR, '#tableResult > tbody > tr')

for train in range(1, len(trains)*2 + 1, 2):
    
    for train_one_sec in range(3, 9):
        train_info = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child({train_one_sec})').text.replace('\n', ' ').replace('-', '')
        print(train_info, end=" ")
    # 가격    
    train_price = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td.guide365 > div > strong').text.replace('\n', ' ')
    
    train_time = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(14)').text.replace('\n', ' ')

    print(train_info, train_price, train_time)

# 상위 2개 기차만 예매 
is_reserved = True
while is_reserved: 
    for select_train in range(1, 5, 2):

        try:
            standard_seat = driver.find_element(By.CSS_SELECTOR, f'#tableResult > tbody > tr:nth-child({select_train}) > td:nth-child(6) > a:nth-child(1) > img').click()
            print("예약되었습니다")
            is_reserved = False
            break
        except:
            pass
    if is_reserved:
        # 매진일 경우 다시 조회
        # time.sleep(1)
        submit = driver.find_element(By.XPATH, '//*[@id="center"]/div[3]/p/a/img')
        driver.execute_script('arguments[0].click();', submit)
        driver.implicitly_wait(10)
    else:
        break
