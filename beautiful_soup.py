from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys
import pandas as pd

query_txt = input('크롤링할 키워드는 무엇인가요?: ')
f_name = input('검색 결과를 저장할 txt 파일경로와 이름을 지정하세요 (예: C:\\Users\\s_jeun097\\Desktop\\crawler\\1.txt)": ')
fc_name = input('검색 결과를 저장할 csv 파일경로와 이름을 지정하세요 (예: C:\\Users\\s_jeun097\\Desktop\\crawler\\1.csv": ')
fx_name = input('검색 결과를 저장할 xls 파일경로와 이름을 지정하세요 (예: C:\\Users\\s_jeun097\\Desktop\\crawler\\1.xls)": ')

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

time.sleep(1)

orig_stdout = sys.stdout
f = open(f_name, 'a', encoding='UTF-8')
sys.stdout = f
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
content_list = soup.find('ul', class_='list_thumType flnon')

no = 1
no2 = []
contents2 = []
tags2 = []

for i in content_list:
    no2.append(no)
    print('번호: ', no)

    contents = i.find('div', class_='tit').get_text()
    contents2.append(contents)
    print('내용:',contents.strip())

    tag = i.find('p', 'tag').get_text()
    tags2.append(tag)
    print('태그:',tag.strip())
    print('\n')

    no += 1

sys.stdout = orig_stdout
f.close()

korea_trip = pd.DataFrame()
korea_trip['번호'] = no2
korea_trip['내용'] = contents2
korea_trip['태그'] = tags2

korea_trip.to_csv(fc_name, encoding="utf-8-sig")
print("csv 파일 저장 경로: %s" %fc_name)



print("데이터 수집이 완료되었습니다.")
