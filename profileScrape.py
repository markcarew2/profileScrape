from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import datetime
import codecs, time

browser = webdriver.Chrome()
url = "https://www.linkedin.com/in/mark-carew-16764590/"
browser.get(url)

time.sleep(1)

if (browser.current_url.strip() == url.strip()):
    html = browser.page_source
    browser.quit()
    current_load = True
    with codecs.open("html.txt", "w", encoding="utf-8") as f:
        f.write(html)
    with codecs.open("html.txt", "a", encoding="utf-8") as f:
        f.write("\n" + datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

else:
    #use saved html from last successful access
    browser.quit()
    current_load = False
    with codecs.open("html.txt", "r", encoding="utf-8") as f:
        html = f.read() 
    
    
soup = BeautifulSoup(html, "html.parser")

summary = soup.find_all("h2", {"class": "summary__heading pp-section__heading"})[0].findNext("p")

experience = soup.find_all("ul", {"class":"experience__list"})

jobs = experience[0].find_all("div", {"class": "result-card__contents"})

edulist = soup.find("ul", {"class": "education__list"})

eduContent = []
for edu in edulist:
    eduContent.append(edu)

#format html
for job in jobs:    
    buttons = job.find_all("button")
    links = job.find_all("a", {"class": "result-card__subtitle-link experience-item__subtitle-link"})
    job.find("span", {"class": "date-range__duration"}).decompose()
    if(job.find("p", {"class": "show-more-less-text__text--more"}) != None):
        job.find("p", {"class": "show-more-less-text__text--less"}).decompose()
    for button in buttons:
        button.decompose()
    for link in links:
        print("*****")
        print(link)
        del link['href']


we1 = jobs[0]
we2 = jobs[1]
we3 = jobs[2]
try:
    we4 = jobs[3]
except(IndexError):
    we4 = ""
try:
    we5 = jobs[4]
except(IndexError):
    we5 = ""
try:
    we6 = jobs[5]
except(IndexError):
    we6 = ""
try:
    we7 = jobs[6]
except(IndexError):
    we7 = ""

edu1 = eduContent[0]
print(edu1)
edu2 = eduContent[1]
try:
    edu3 = eduContent[2]
except(IndexError):
    edu3 = ""
try:
    edu4 = eduContent[3]
except(IndexError):
    edu4 = ""

with codecs.open("html.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    load_time = lines[-1]