from selenium import webdriver
from bs4 import BeautifulSoup
import time
import urllib
import os
from pyvirtualdisplay import Display

def ProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):

    iteration = iteration+1
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

def scrape():
    display = Display(visible=0, size=(800, 600))
    display.start()

    browser = webdriver.Chrome("/home/piyush/Downloads/chromedriver_linux64/chromedriver")

    URL = "https://kissmanga.com"
    browser.get(URL)
    print("Fetching Data .", end =" ")
    time.sleep(10)

    print()

    search = browser.find_element_by_xpath("//input[@id='keyword']")
    srch = input("Search: ")
    search.send_keys(srch)

    print("Searching")

    browser.find_element_by_xpath("//input[@id='imgSearch']").click()

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

    browser.get(URL+link[x-1])


    page = browser.page_source
    soup = BeautifulSoup(page, features='lxml')

    link=[]
    name=[]

    for t in soup.find_all('table',attrs={'class':'listing'}):
        for a in t.find_all('a',href=True):
            link.append(a['href'])
            name.append(a.text.replace('\n','').strip())

    for i in range(0,11):
        print(str(i+1)+".",name[i])

    x = int(input("Enter choice: "))

    browser.get(URL+link[x-1])
    chp = name[x-1]

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
        na = str(i)+"."+image[i].split('.')[len(image[i].split('.'))-1]

        urllib.request.urlretrieve(image[i], os.path.join(my_path, na))

        ProgressBar( i, l, prefix = 'Progress', suffix = 'Complete', length = 50)


    browser.close()
    display.stop()

if __name__=="__main__":
    scrape()
