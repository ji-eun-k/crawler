from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys

query_txt = input('크롤링할 키워드는? :')

path = "C:\\Users\\s_jeun097\\Desktop\\crawler\\chromedriver\\chromedriver.exe"
driver = webdriver.Chrome(path)
