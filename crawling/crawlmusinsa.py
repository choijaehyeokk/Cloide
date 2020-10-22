from selenium import webdriver
import re, csv
from bs4 import BeautifulSoup
import openpyxl
import time
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import datetime
from random import uniform, randint
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
import scipy.interpolate as si
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException
import requests
import re

driver = webdriver.Firefox(executable_path = r'C:/Users/qkrtm/Desktop/KAU/4-1/Jongsul/gitJongsul/RNN/datacrawl/geckodriver.exe')

driver.maximize_window()
driver.implicitly_wait(20)

driver.get('https://store.musinsa.com/app/contents/brandshop')




#select = Select(driver.find_element_by_id("brandselect"))


#driver.find_element_by_id('brandselect').click()
#'쿠어',
#검색창에 리스트 순으로 검색 입력


brand_list = [
'블론드나인',
'테이크이지',
'트릴리온',
'어커버',
'캉골',
'뉴발란스',
'프리즘웍스',
'미나브',
'오앤에이',
'일오공칠',
'엠블러',
'크리틱',
'어반스터프',
'크럼프',
'니티드',
'엠엠지엘',
'칸코',
'랩101',
'가먼트레이블',
'비슬로우',
'그레이버',
'비욘드클로젯',
'아식스',
'하프크라이즈',
'소버먼트',
'타미진스',
'로맨틱무브',
'어낫띵',
'노매뉴얼',
'어텐션로우',
'이벳필드',
'아웃스탠딩',
'알파 인더스트리',
'이너프이즈이너프',
'퍼스텝'
]

#'쿠어','브렌슨','반스','더블유브이프로젝트','꼼파뇨','비바스튜디오','칼하트','디스커버리 익스페디션','엘무드
element= 0
print(driver.current_url)
file_name = "brandinfo.txt"
file_open = open(file_name, "w", encoding="utf-8")


for brand in brand_list:
    driver.implicitly_wait(20)
    element = driver.find_element_by_name('q')
    element.click()
    driver.implicitly_wait(10)
    element.send_keys(brand)
    driver.implicitly_wait(20)
    element.submit()
    driver.implicitly_wait(55)
    sleep(20)
    if element != 0:
        
        driver.execute_script("window.scrollTo(0, window.scrollY + 400);")
        sleep(20)

    #driver.find_element_by_class_name('img-block').click()
    #sleep(18)
    #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #sleep(8)
    #driver.execute_script("window.scrollTo(document.body.scrollHeight, window.scrollY-2500);")
    #sleep(8)

    #result = driver.find_element_by_class_name('row')
    source = requests.get(driver.current_url).text
    soup = BeautifulSoup(source,'html.parser')

    info = soup.find("div", {"class":"item"})
    info2 = soup.select(" .item")
    cnt =0
    list = []
    re = info.text
    list.append(re)
    ans = list[0]
    #cate = ans.split(" ")
    '''for an in ans:
        for real in an:
            if not real.isdigit():
                real2 = real
                print(real2)
     '''
    answer = ''
    kindlist = [1]
    for an in ans:
        if not an.isdigit():
            real2= an
            answer = answer+real2
            #print(real2)

    cate = answer.split(" ")
    for c in cate:
        if c == '상의':
            kindlist.append(1)
        elif c == '바지':
            kindlist.append(2)
        elif c == '아우터':
            kindlist.append(3)
        elif c == '원피스':
            kindlist.append(4)
        elif c == '스커트':
            kindlist.append(5)
        elif c =='가방':
            kindlist.append(6)
        elif c == '신발':
            kindlist.append(7)
        elif c == '모자':
            kindlist.append(8)
        elif c == '양말/레그웨어':
            kindlist.append(9)
        else:
            continue

    print(kindlist)
    
    
