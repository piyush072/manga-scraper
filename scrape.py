from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver")
URL = "https://kissmanga.com"
browser.get(URL)

time.sleep(12)

search = browser.find_element_by_xpath("//input[@id='keyword']")
search.send_keys("One Piece")

browser.find_element_by_xpath("//input[@id='imgSearch']").click()
page = browser.page_source
soup = BeautifulSoup(page, features='lxml')

browser.close()

link=[]
name=[]

for t in soup.find_all('table',attrs={'class':'listing'}):
    for a in t.find_all('a',href=True):
        link.append(a['href'])
        name.append(a.text.replace('\n','').strip())

print("Search Result")

for i in range(0,len(link)):
    print(i+1,name[i])

x = int(input())

URL = "https://kissmanga.com"+link[x-1]

browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver")
browser.get(URL)

time.sleep(12)
