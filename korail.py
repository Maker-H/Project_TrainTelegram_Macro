# https://kminito.tistory.com/79?category=373099

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time 
import datetime
import pwd_token # getting id

# ---------------global variables--------------
korail_id = pwd_token.get_korailid()
korail_pwd = pwd_token.get_korailpwd()

korail_start_station = '동대구'
korail_end_station = '구미'

korail_hour = '19'
korail_year = '2023'
korail_month = '02'
korail_day = '20'

korail_train_types = []

num_of_reservation = 2
# ---------------global variables--------------


TODAY = datetime.datetime.now()

    #23/02/23     #23/2/23    # 2/23    
    # # If year is not assigned, set default year by current year
def get_date(date_with_year):
    global korail_day
    global korail_month
    global korail_year


    # Have to convert to int because of date_format
    input_date = date_with_year.strip()
    if input_date != '':
        input_date = list(map(int, date_with_year.split('/')))
    
    # With year
    if len(input_date) == 3:
        
        # Set year
        if len(input_date[0]) == 2:
            korail_year = '20' + str(input_date[0])
        else:
            korail_year = str(input_date[0])

        korail_month = hour_day_month_format(input_date[1])
        korail_day = hour_day_month_format(input_date[2])
    
    #With month and date
    elif len(input_date) == 2:
        korail_year = str(TODAY.year)
        korail_month = hour_day_month_format(input_date[1])
        korail_day = hour_day_month_format(input_date[2])

    # Without month and date, set today date as default
    elif input_date == '':
        korail_year = str(TODAY.year)
        korail_month = hour_day_month_format(TODAY.month)
        korail_day = hour_day_month_format(TODAY.day)


def get_hour(input_hour):
    global korail_hour
    if input_hour == '':
        korail_hour = hour_day_month_format(int(TODAY.hour))
    elif input_hour != '':
        korail_hour = hour_day_month_format(int(input_hour))


# If month and date is smaller than 10, add 0 and convert to str
# For hour, day, month
def hour_day_month_format(int_date):
    if int_date < 10:
        return '0' + str(int_date)
    else:
        return str(int_date)


def get_station(user_input):
    global korail_start_station
    global korail_end_station

    stations = user_input.split()
    korail_start_station = stations[0]
    korail_end_station = stations[1]



def get_num_of_reservation(user_input):
    global num_of_reservation
    return int(user_input)


def get_train_type(user_input):
    korail_train_types = user_input.split()

def click_train_type():
    global driver 
    if not korail_train_types:
        return
    
    for type in korail_train_types:
        if type == 'ktx':
            Select(driver.find_element(By.XPATH, '//*[@id="selGoTrainRa00"]')).click()
        elif type == '새마을':
            Select(driver.find_element(By.XPATH, '//*[@id="selGoTrainRa08"]')).click()

#=============================================================================

def show_train_list():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome("/Users/hs_/Downloads/chromedriver_mac_arm64/chromedriver") # Webdriver 파일의 경로를 입력
    url = 'https://www.letskorail.com/korail/com/login.do'
    driver.get(url) # 이동을 원하는 페이지 주소 입력
    driver.implicitly_wait(10) # 페이지 다 뜰 때 까지 기다림

    # enter id, pwd
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

    #enter departure station
    dep_stn = driver.find_element(By.ID, 'start')
    dep_stn.clear() 
    dep_stn.send_keys(korail_start_station)
    driver.implicitly_wait(5)

    # enter arrival station
    arr_stn = driver.find_element(By.ID, 'get')
    arr_stn.clear()
    arr_stn.send_keys(korail_end_station)
    driver.implicitly_wait(5)
    
    # select train type
    click_train_type()

    # 출발 날짜 입력
    # https://velog.io/@rkfksh/Selenium-click%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-element%EB%A5%BC-javascript-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-click%ED%95%98%EA%B8%B0
    # driver.find_element(By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img').click()
    # driver.implicitly_wait(5)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[4]/td[4]').click()


    # enter departure date
    Select(driver.find_element(By.ID,"s_year")).select_by_value(korail_year)
    Select(driver.find_element(By.ID,"s_month")).select_by_value(korail_month)
    Select(driver.find_element(By.ID,"s_day")).select_by_value(korail_day)

    # enter departure date
    Select(driver.find_element(By.ID,"s_hour")).select_by_value(korail_hour)
    # Select(driver.find_element(By.ID,"time")).select_by_visible_text(str(korail_hour))


    # start look up
    driver.find_element(By.XPATH,'//*[@id="center"]/form/div/p/a/img').click()
    driver.implicitly_wait(5)
    time.sleep(2)


    # print trains
    trains = driver.find_elements(By.CSS_SELECTOR, '#tableResult > tbody > tr')

    for train in range(1, len(trains)*2 + 1, 2):
    
        train_departure = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(3)').text.replace('\n', ' ').replace('-', '').replace('(1량)', '')
        train_arrival = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(4)').text.replace('\n', ' ').replace('-', '').replace('(1량)', '')

        # price    
        train_price = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td.guide365 > div > strong').text.replace('\n', '')
        

        tmp = train_price.split()
        if len(tmp) != 1:
            train_price = tmp[-1]

        train_time = driver.find_element(By.CSS_SELECTOR,f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(14)').text.replace('\n', ' ')

        train_type = driver.find_element(By.CSS_SELECTOR, f'#tableResult > tbody > tr:nth-child({train}) > td:nth-child(2)').get_attribute('title')
        
        if train_type == '':
            train_type = '새마을호'

        print(f'{train_departure} {train_arrival} {train_price} {train_type}  소요:{train_time}')



def start_reservation():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # driver = webdriver.Chrome("/Users/hs_/Downloads/chromedriver_mac_arm64/chromedriver") # Webdriver 파일의 경로를 입력
    url = 'https://www.letskorail.com/korail/com/login.do'
    driver.get(url) # 이동을 원하는 페이지 주소 입력
    driver.implicitly_wait(15) # 페이지 다 뜰 때 까지 기다림

    # Enter korail id and pwd
    driver.find_element(By.ID, 'txtMember').send_keys(korail_id) # 회원번호
    driver.find_element(By.ID, 'txtPwd').send_keys(korail_pwd) # 비밀번호


    driver.find_element(By.XPATH, '//*[@id="loginDisplay1"]/ul/li[3]/a/img').click()
    driver.implicitly_wait(10)

    # Goto reservation site
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

    # Enter departure station
    dep_stn = driver.find_element(By.ID, 'start')
    dep_stn.clear() 
    dep_stn.send_keys(korail_start_station)
    driver.implicitly_wait(5)

    # Enter arrival station
    arr_stn = driver.find_element(By.ID, 'get')
    arr_stn.clear()
    arr_stn.send_keys(korail_end_station)
    driver.implicitly_wait(5)

    # Select train type
    click_train_type()

    # 출발 날짜 입력
    # https://velog.io/@rkfksh/Selenium-click%EB%90%98%EC%A7%80-%EC%95%8A%EB%8A%94-element%EB%A5%BC-javascript-%EB%AA%85%EB%A0%B9%EC%96%B4%EB%A1%9C-click%ED%95%98%EA%B8%B0
    # driver.find_element(By.XPATH, '//*[@id="res_cont_tab01"]/form/div/fieldset/ul[2]/li[1]/a/img').click()
    # driver.implicitly_wait(5)
    # time.sleep(1)
    # driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[1]/div/div/table/tbody/tr[4]/td[4]').click()

    # enter departure date
    Select(driver.find_element(By.ID,"s_year")).select_by_value(korail_year)
    Select(driver.find_element(By.ID,"s_month")).select_by_value(korail_month)
    Select(driver.find_element(By.ID,"s_day")).select_by_value(korail_day)

    # enter departure date
    Select(driver.find_element(By.ID,"s_hour")).select_by_value(korail_hour)
    # Select(driver.find_element(By.ID,"time")).select_by_visible_text(str(korail_hour))


    # start searching
    driver.find_element(By.XPATH,'//*[@id="center"]/form/div/p/a/img').click()
    driver.implicitly_wait(5)
    time.sleep(2)


    # Start Resevation
    is_reserved = True
    while is_reserved: 
        for select_train in range(1, 5, num_of_reservation):

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
