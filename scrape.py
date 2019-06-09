from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import urllib
from urllib.parse import urlparse
import os
from pyvirtualdisplay import Display # requires xvfv- sudo apt-get install xvfb
import progress
import sys

option = webdriver.ChromeOptions()
chrome_prefs = {}
option.experimental_options["prefs"] = chrome_prefs
chrome_prefs["profile.default_content_settings"] = {"images": 2}
chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver",options=option) #change path here

def scrape():

    if(urlparse((sys.argv[1])).scheme!=''):
        download(sys.argv[1],sys.argv[1].split('/')[len(sys.argv[1].split('/'))-1].split('\\')[0],0)
    else:
        URL = "https://kissmanga.com"
        browser.get(URL)
        print("Fetching Data .", end =" ")
        time.sleep(10)

        print()

        search = browser.find_element_by_xpath("//input[@id='keyword']")
        search.send_keys(sys.argv[1])
        search.send_keys(Keys.RETURN)
        print("Searching")

        #browser.find_element_by_xpath("//input[@id='imgSearch']").click()

        page = browser.page_source
        soup = BeautifulSoup(page, features='lxml')


        link=[]
        name=[]

        for t in soup.find_all('table',attrs={'class':'listing'}):
            for a in t.find_all('a',href=True):
                link.append(a['href'])
                name.append(a.text.replace('\n','').strip())

        print("Search Result:")

        for i in range(0,len(link)):
            print(str(i+1)+".",name[i])

        x = int(input("Enter choice: "))

        t = urlparse(URL+link[x-1]).path.split('/')
        v = len(t)
        if(v>3):
            download(URL+link[x-1],t[3],1)
            browser.close()
            display.stop()
            sys.exit()

        browser.get(URL+link[x-1])


        page = browser.page_source
        soup = BeautifulSoup(page, features='lxml')

        link=[]
        name=[]

        for t in soup.find_all('table',attrs={'class':'listing'}):
            for a in t.find_all('a',href=True):
                link.append(a['href'])
                name.append(a.text.replace('\n','').strip())

        for i in range(0,6):
            print(str(i+1)+".",name[i])

        x = int(input("Enter choice: "))
        chp = name[x-1]
        download(URL+link[x-1],chp,1)


    browser.close()
    display.stop()

def download(URL,chp,q):

    browser.get(URL)
    if(q==0):
        time.sleep(10)
    my_path = '/home/piyush/Downloads/'+chp #change path here

    try:
        os.mkdir(my_path)
    except FileExistsError:
        x = input("Directory already exists! Press Y to overwrite files: ")
        if(x != 'Y'):
            sys.exit()

    page = browser.page_source
    soup = BeautifulSoup(page, features='lxml')

    image = []

    for div in soup.find_all('div',attrs={'id':'divImage'}):
        for img in div.find_all('img'):
            image.append(img['src'])

    l=len(image)
    print("Downloading "+chp)

    progress.ProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)

    for i in range(0,l):

        urllib.request.urlretrieve(image[i], os.path.join(my_path, str(i)))

        progress.ProgressBar( i, l, prefix = 'Progress', suffix = 'Complete', length = 50)

    print("File Downloaded at "+my_path)

if __name__=="__main__":
    scrape()
