import os
import sys
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as bs

USER_INFO = {
    "id": "userid"
    ,"pw": "userpw"
    
}

ptjs = "S://devtool//phantomjs-2.1.1-windows//bin//phantomjs"    #* phatomjs 경로
# warnings.filterwarnings('ignore')

def run():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)
    # chrome_option.add_argument("headless")   #*창안보이게 실행
    # chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('S://CODE//Django//crawler//chromedriver.exe', chrome_options=chrome_option)
    # driver = webdriver.PhantomJS(ptjs)
    
    return driver

def run_browser(driver):
    url = "https://www.yes24.com/Templates/FTLogin.aspx"
    # url = "https://ezsso.bizmeka.com/loginForm.do"

    driver.implicitly_wait(3) 

    driver.get(url)
    driver.find_element(By.ID,"SMemberID").send_keys(USER_INFO['id'])
    driver.find_element(By.ID,"SMemberPassword").send_keys(USER_INFO['pw'])
    driver.find_element(By.ID,"btnLogin").click()

    #팝업창 대응
    popups = driver.find_elements(By.CLASS_NAME, "yPopBot")
    # print(popups, len(popups))
    if len(popups) != 0:
        for pop in popups:
            try:
                pop.find_element(By.ID, "chk_info").click()    #팝업창 닫기 버튼이 있을 시 클릭이벤트
                print("popup element: ", pop)
            except:
                pass
            
    #티켓창으로 이동
    driver.get("http://ticket.yes24.com/")
    
    #공연 팝업창 대응
    popups = driver.find_elements(By.CLASS_NAME, "pop-bottom")
    # print(popups, len(popups))
    if len(popups) != 0:
        for pop in popups:
            try:
                pop.find_element(By.ID, "chkToday").click()    #팝업창 닫기 버튼이 있을 시 클릭이벤트
                print("popup element: ", pop)
            except:
                pass
    else:
        print("팝업창이 존재하지 않습니다.")
    
    
    #공연 순위정보 긁어오기
    top_navi = driver.find_element(By.CLASS_NAME, "perform-top")
    top_navi.find_element(By.PARTIAL_LINK_TEXT, "랭킹").click()
    print("랭킹 탐색")
    driver.switch_to.window(driver.window_handles[-1])    #윈도우 창 전환
      
    rank_best = driver.find_element(By.CLASS_NAME, "rank-best").text
    rank_list = driver.find_element(By.CLASS_NAME, "rank-list").text
    
    # html = driver.page_source    #동적으로 내용 불러오는지 .....html  안읽어와짐..
    # soup = bs(html, 'html.parser')
    
    print("rank_best: ",rank_best)
    print("rank_list: ",rank_list)
    
    
    return rank_best, rank_list
    # time.sleep(500)
    
    driver.quit()
    while True:     #브라우저 자동종료 방지 코드
        pass



driver = run()
run_browser(driver)


