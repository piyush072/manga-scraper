from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib
import os

def ProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):

    iteration = iteration+1
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver")
URL = "https://kissmanga.com"
browser.get(URL+"/Manga/One-Piece")

time.sleep(12)
'''
search = browser.find_element_by_xpath("//input[@id='keyword']")
search.send_keys("One Piece")

browser.find_element_by_xpath("//input[@id='imgSearch']").click()
page = browser.page_source
soup = BeautifulSoup(page, features='lxml')

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


browser.get(URL+link[x-1])
'''

page = browser.page_source
soup = BeautifulSoup(page, features='lxml')

link=[]
name=[]

for t in soup.find_all('table',attrs={'class':'listing'}):
    for a in t.find_all('a',href=True):
        link.append(a['href'])
        name.append(a.text.replace('\n','').strip())

browser.get(URL+link[0])
chp = name[0]
my_path = '/home/piyush/Downloads/'+chp
os.mkdir(my_path)
page = browser.page_source
soup = BeautifulSoup(page, features='lxml')

image = []

for div in soup.find_all('div',attrs={'id':'divImage'}):
    for img in div.find_all('img'):
        image.append(img['src'])

l=len(image)

ProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

for i in range(0,l):
    na = str(i)+"."+image[i].split('.')[1]

    urllib.request.urlretrieve(image[i], os.path.join(my_path, na))

    ProgressBar( i, l, prefix = 'Progress', suffix = 'Complete', length = 50)


browser.close()
