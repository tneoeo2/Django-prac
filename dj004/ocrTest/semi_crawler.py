import os
import sys
import time
import getpass
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup as bs


chromedriver_autoinstaller.install()



ptjs = "S://devtool//phantomjs-2.1.1-windows//bin//phantomjs"    #* phatomjs 경로
# warnings.filterwarnings('ignore')

def run():
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)
    # chrome_option.add_argument("headless")   #*창안보이게 실행
    # chrome_option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=chrome_option)
    # driver = webdriver.PhantomJS(ptjs)

    return driver


def get_seat(driver):    #자리줍줍
    t_month = "9"   #월
    t_date = "4"    #일
    num = "1"    #회차 1, 2

    driver.get("http://ticket.yes24.com/Perf/42489?Gcode=009_400")    #원하는 공연번호
    #월 맞는지 확인
    month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text

    #팝업창 있다면
    try:
        popup = driver.find_element(By.CLASS_NAME,"pop-alert-check")
        popup.find_element(By.TAG_NAME, 'a').click()
    except:
        pass

    while True:
        if int(month) == int(t_month):
            calendar = driver.find_element(By.CLASS_NAME, "ui-datepicker-calendar")
            calendar.find_element(By.PARTIAL_LINK_TEXT, t_date).click()
            numlist = driver.find_element(By.ID, "PerfPlayTime")
            numlist.find_element(By.PARTIAL_LINK_TEXT, num+"회").click()
            driver.find_element(By.PARTIAL_LINK_TEXT, "예매하기").click()   #예매하기
            break
        else:
            driver.find_element(By.CLASS_NAME, "ui-icon-circle-triangle-e").click()
            time.sleep(2)
            month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text


def get_rank(driver):

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
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])    #윈도우 창 전환
    time.sleep(2)

    #랭킹 데이터 제목, 이미지, 기간, 장소 나눠서 저장 (dict 형태로 공연별 정보 저장)
    """
    #? dict 형식
    goods_info = {
      0: {
        "title": ""      #제목       rlb-tit
        ,"image": ""     #이미지     rank-best-img  > img
        ,"place": ""     #장소      rlb-sub-tit
        ,"date": ""      #기간      rlb-sub-tit  (<br>로 구분)
        ,"ranking": ""   #순위정보   rank-best-number
      }.
      1 : {
        ...
      }
    }
    """
    goods_info = {}


    #rank best dict 만들기
    rank_best = driver.find_elements(By.CLASS_NAME, "rank-best > div")
    # rank_best =
    for i, rank in enumerate(rank_best):
      title = rank.find_element(By.CLASS_NAME, "rlb-tit").text
      image = rank.find_element(By.TAG_NAME, "img").get_attribute('src')
      date = rank.find_element(By.CLASS_NAME, "rlb-sub-tit").text.split('\n')[0]
      place = rank.find_element(By.CLASS_NAME, "rlb-sub-tit").text.split('\n')[1]
      ranking = rank.find_element(By.CLASS_NAME, "rank-best-number").text.split("\n")[0]
      goods_info.update({ i : {"title": title, "image": image, "date": date, "place": place, "ranking": ranking }})

    print("best_goods_info : \n", goods_info)


    rank_list = driver.find_elements(By.CLASS_NAME, "rank-list > div")

    g_keys = list(goods_info.keys())
    i = g_keys[-1]
    for rank in rank_list:
      i += 1
      title = rank.find_element(By.CLASS_NAME, "rank-list-tit a").text
      image = rank.find_element(By.TAG_NAME, "img").get_attribute('src')
      date = rank.find_elements(By.TAG_NAME, "p")[-1].text.split('\n')[0]
      place = rank.find_elements(By.TAG_NAME, "p")[-1].text.split('\n')[1]
      ranking = rank.find_element(By.CLASS_NAME, "fluctuation span").text
      goods_info.update({ i : {"title": title, "image": image, "date": date, "place": place, "ranking": ranking }})



    print(" goods_info : \n", goods_info)


    return goods_info

    # html = driver.page_source    #동적으로 내용 불러오는지 .....html  안읽어와짐..
    # soup = bs(html, 'html.parser')

    # print("rank_best: ",rank_best)
    # print("rank_list: ",rank_list)

def login(driver):     #*로그인이 필요한 경우 사용
  
    print("id 입력 : ", end='')
    user_id = input()
    user_pw = getpass.getpass()


    USER_INFO = {
        "id": user_id
        ,"pw": user_pw

    }

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



def run_browser(driver):
    # login(driver)
    # get_seat(driver)
    goods_info = get_rank(driver)


    return goods_info

    time.sleep(500)

    driver.quit()
    while True:     #브라우저 자동종료 방지 코드
        pass



# driver = run()
# run_browser(driver)
# driver.quit()

