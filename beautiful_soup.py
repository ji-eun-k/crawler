from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

query_txt = input('크롤링할 키워드는 무엇인가요?: ')
f_name = input('검색 결과를 저장할 파일경로와 이름을 지정하세요 (예: C:\\Users\\s_jeun097\\Desktop\\crawler\\1.txt)": ')

path = "C:\\Users\\s_jeun097\\Desktop\\crawler\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://korean.visitkorea.or.kr/main/main.do")
time.sleep(2)

dad = driver.find_element_by_id('safetyStay1')
dad.find_element_by_class_name('btn_close3').click()
time.sleep(1)

driver.find_element_by_id("btnSearch").click()
element = driver.find_element_by_id("inp_search")
element.send_keys(query_txt)

driver.find_element_by_link_text("검색").click()

full_html = driver.page_source

soup = BeautifulSoup(full_html, 'html.parser')

content_list = soup.find("li", class_='bdr_nor')

print(content_list.text)
