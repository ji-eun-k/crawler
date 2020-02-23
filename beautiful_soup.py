from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

query_txt = input('크롤링할 키워드는 무엇인가요? : ')

path = "C:\\Users\\s_jeun097\\Desktop\\crawler\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://korean.visitkorea.or.kr/main/main.do")
time.sleep(3)

dad = driver.find_element_by_id('safetyStay1')
dad.find_element_by_class_name('btn_close3').click()

time.sleep(2)

driver.find_element_by_id("btnSearch").click()

element = driver.find_element_by_id("inp_search")

element.send.keys(query_txt)

driver.find_element_by_link_text("검색").click()


