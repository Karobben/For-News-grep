#!/usr/local/bin/python3.7
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import requests
import threading
import time

print(time.asctime())
url= "https://www.nature.com/nature/"
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')


A_time=time.time()
###########
#Head Line#
###########

Head_line=soup.find("div",{"class":"container cleared container-type-hero"})
title=Head_line.find("h3").get_text()
descrip=Head_line.find("div",{"class":"serif text17 headline-summary tighten-line-height contrast-text pt20 ma0 mq480-hide"}).get_text()
Head=Head_line.find("a")['href']
print("Head Line:",title,"\n","descrip:",descrip,"\n\n\n\n")


print("\n#Article for First_4\n\n")
NUM=0
First_4=soup.find(id="featured-content").find_all("article")
for i in First_4:
    NUM=NUM+1
    title=i.find("h3").get_text()
    title=title.replace("\n","")
    title=title.replace("  ","")
    try:
        quick_see=i.find("div",{"class":"mt4 serif text13 tighten-line-height text-gray suppress-bottom-margin hide-overflow"}).find("p").get_text()
    except:
        quick_see="BLANK"
    try:
        Authors=i.find("ul",{"class":"ma0 mt6 pa0 clean-list inline-list text13 tighten-line-height text-gray-light js-list-authors-3 js-etal-collapsed"}).get_text()
    except:
        Authors="BLANK"
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    print([NUM],title,"\n")
    print("Authors:",Authors)
    print("quick_see:",quick_see,"\n","\n")


print("\n#Latest Research\n\n")
Latest=soup.find(id="latest-research").find_all("article")
for i in Latest:
    NUM=NUM+1
    title=i.find("h3").get_text()
    title=title.replace("\n","")
    title=title.replace("  ","")
    try:
        quick_see=i.find("div",{"class":"mt4 serif text13 tighten-line-height text-gray suppress-bottom-margin hide-overflow"}).find("p").get_text()
    except:
        quick_see="BLANK"
    try:
        Authors=i.find("ul",{"class":"ma0 mt6 pa0 clean-list inline-list text13 tighten-line-height text-gray-light js-list-authors-3 js-etal-collapsed"}).get_text()
    except:
        Authors="BLANK"
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    print([NUM],title,"\n")
    print("Authors:",Authors)
    print("quick_see:",quick_see,"\n","\n")

print("\n#Latest Review\n\n")
Latest=soup.find(id="latest-reviews").find_all("article")
for i in First_4:
    NUM=NUM+1
    title=i.find("h3").get_text()
    title=title.replace("\n","")
    title=title.replace("  ","")
    try:
        quick_see=i.find("div",{"class":"mt4 serif text13 tighten-line-height text-gray suppress-bottom-margin hide-overflow"}).find("p").get_text()
    except:
        quick_see="BLANK"
    try:
        Authors=i.find("ul",{"class":"ma0 mt6 pa0 clean-list inline-list text13 tighten-line-height text-gray-light js-list-authors-3 js-etal-collapsed"}).get_text()
    except:
        Authors="BLANK"
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    print([NUM],title,"\n")
    print("Authors:",Authors)
    print("quick_see:",quick_see,"\n","\n")


print("\n#News & Comment\n\n")
News=soup.find(id="news-comment").find_all("article")
for i in News:
    NUM=NUM+1
    title=i.find("h3").get_text()
    title=title.replace("\n","")
    title=title.replace("  ","")
    try:
        quick_see=i.find("div",{"class":"mt4 serif text13 tighten-line-height text-gray suppress-bottom-margin hide-overflow"}).find("p").get_text()
    except:
        quick_see="BLANK"
    try:
        Authors=i.find("ul",{"class":"ma0 mt6 pa0 clean-list inline-list text13 tighten-line-height text-gray-light js-list-authors-3 js-etal-collapsed"}).get_text()
    except:
        Authors="BLANK"
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    print([NUM],title,"\n")
    print("Authors:",Authors)
    print("quick_see:",quick_see,"\n","\n")



print("\n#Head Line\n\n")
Head=Head_line.find("a")['href']
html = urlopen(Head).read().decode('utf-8')
soup_H = BeautifulSoup(html, 'lxml')

paper=soup_H.find(id='content').find('article')
title= paper.find("header").find("h1").get_text()
title=title.replace("\xa0"," ")
author= paper.find("header").find("ul").find_all('li')
Abstract = paper.find(id="Abs1-content").find("p").get_text()
Abstract = Abstract.replace("\xa0"," ")

print("Title: ",title,"\n\n")
for i in author:
    i=i.find("a").get_text()
    print(i)
print("\nAbstract: ", Abstract,"\n\n\n")


print("#Article for First_4\n\n")
First_4=soup.find(id="featured-content").find_all("article")
list=First_4
def First_4(i):
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    html = urlopen(paper_sit).read().decode('utf-8')
    soup_FF = BeautifulSoup(html, 'lxml')
    paper=soup_FF.find(id='content').find('article')
    title= paper.find("header").find("h1").get_text()
    title=title.replace("\xa0"," ")
    try:
        author= paper.find("header").find("ul").find_all('li')
    except:
        author= paper.find("header").find("ul").find('li')
    Abstract = paper.find(id="Abs1-content").find("p").get_text()
    Abstract = Abstract.replace("\xa0"," ")
    A=""
    for i in author:
        i=i.find("a").get_text()
        A =A+ i
    print("\n\n","Title: ",title,"\n\n",A,"\nAbstract: ", Abstract,"\n\n\n")
threads = []
files = range(len(list))
for i in files:
    t = threading.Thread(target=First_4,args=(list[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

print("#Latest Research\n\n")
Latest=soup.find(id="latest-research").find_all("article")
list=Latest
def Latest(i):
    paper_sit="https://www.nature.com"+i.find("h3").find("a")['href']
    html = urlopen(paper_sit).read().decode('utf-8')
    soup_LR = BeautifulSoup(html, 'lxml')
    paper=soup_LR.find(id='content').find('article')
    title= paper.find("header").find("h1").get_text()
    title=title.replace("\xa0"," ")
    try:
        author= paper.find("header").find("ul").find_all('li')
    except:
        author= paper.find("header").find("ul").find('li')
    Abstract = paper.find(id="Abs1-content").find("p").get_text()
    Abstract = Abstract.replace("\xa0"," ")
    A=""
    for i in author:
        i=i.find("a").get_text()
        A =A+ i
    print("\n\n","Title: ",title,"\n\n",A,"\n\nAbstract: ", Abstract,"\n\n\n")
threads = []
files = range(len(list))
for i in files:
    t = threading.Thread(target=Latest,args=(list[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()


print("#Latest Review\n\n")
Latest_V=soup.find(id="latest-reviews").find_all("article")
list=Latest_V
def Latest_V(addres):
    paper_sit="https://www.nature.com"+addres.find("h3").find("a")['href']
    html = urlopen(paper_sit).read().decode('utf-8')
    soup_LV = BeautifulSoup(html, 'lxml')
    paper=soup_LV.find(id='content').find('article')
    title= paper.find("header").find("h1").get_text()
    title=title.replace("\xa0"," ")
    author=paper.find_all("a",{"class":"icon icon-right-top icon-mail-12x9-blue pr15 js-no-scroll"})
    try:
        body=paper.find("div",{"class","article__body serif cleared"}).find_all("p")
    except:
        body=paper.find(id="Abs1-content").find_all("p")
    A=""
    for i in author:
        i=i.get_text()
        A = A+ i
    B=""
    for i in body:
        i=i.get_text()
        B = B+"\n\n"+i
    print("\n\n","Title: ",title,"\n\n",A,"\n\nAbstract: ",B,"\n\n\n")
threads = []
files = range(len(list))
for i in files:
    t = threading.Thread(target=Latest_V,args=(list[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

print("#News & Comment\n\n")
News=soup.find(id="news-comment").find_all("article")
list=News
def News(adders):
    paper_sit="https://www.nature.com"+adders.find("h3").find("a")['href']
    html = urlopen(paper_sit).read().decode('utf-8')
    soup_NW = BeautifulSoup(html, 'lxml')
    paper=soup_NW.find(id='content').find('article')
    title= paper.find("header").find("h1").get_text()
    title=title.replace("\xa0"," ")
    author=paper.find_all("a",{"class":"icon icon-right-top icon-mail-12x9-blue pr15 js-no-scroll"})
    body=paper.find("div",{"class","article__body serif cleared"}).find_all("p")
    A=""
    for i in author:
        i=i.find("a").get_text()
        A =A+ i
    B=""
    for i in body:
        i=i.get_text()
        B = B+"\n\n"+i
    print("\n\n","Title: ",title,"\n\n",A,"\n\n\nAbstract: ", B,"\n\n\n")
threads = []
files = range(len(list))
for i in files:
    t = threading.Thread(target=News,args=(list[i],))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()


print(time.time()-A_time)
