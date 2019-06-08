from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver")
URL = "https://kissmanga.com"
browser.get(URL)

time.sleep(7)

browser.find_element_by_xpath("//a[@id='liMostViewtab']").click()
