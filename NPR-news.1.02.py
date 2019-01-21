#!/usr/local/bin/python3.7

import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-t','-T','--translation', default = "None")     #输入文件

#获取参数
args = parser.parse_args()

translation = args.translation


##########
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re
import requests
import time

print(time.asctime())

url= "https://www.npr.org/"
html = urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')

U_1="http://www.youdao.com/w/eng/"
U_2="/#keyfrom=dict2.index"
story_today=soup.find_all('div',{"class":"story-wrap"})

if translation == 'yes':
    num=0
    for i in story_today[0:]:
        num=num+1
        ###Translation
        Title=i.find('h3',{"class":"title"}).get_text()
        TR = Title.replace("/"," or ")
        TR = TR.replace("\"","%22T")
        TR = TR.replace(" ","%20")
        TR = TR.replace(":","%3A")
        TR = TR.replace(">","%3E")
        TR = TR.replace("+","%2B")
        TR = TR.replace("=","%3D")
        url2=U_1 + TR + U_2
        html = urlopen(url2).read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        Tran=soup.find(id="fanyiToggle").find_all('p')[1].get_text()
        print([num],Title+"\n"+"\n"+"\n"+Tran+"\n"+"\n"+"\n"+"\n")         # Title

    NOM=0
    num=0
    for i in story_today[NOM:]:
                num=num+1
                ###Translation
                Title=i.find('h3',{"class":"title"}).get_text()
                TR = Title.replace("/"," or ")
                TR = TR.replace("—","")
                TR = TR.replace("\"","%22T")
                TR = TR.replace(" ","%20")
                TR = TR.replace(" ","%20")
                TR = TR.replace(":","%3A")
                TR = TR.replace(">","%3E")
                TR = TR.replace("..","")
                TR = TR.replace("=","%3D")
                url2=U_1 + TR + U_2
                html = urlopen(url2).read().decode('utf-8')
                soup = BeautifulSoup(html, 'lxml')
                Tran=soup.find(id="fanyiToggle").find_all('p')[1].get_text()
                print([num],Title+"\n"+"\n"+"\n"+Tran+"\n"+"\n"+"\n"+"\n")
                result_url = i.find('a',{'href':re.compile("https://www.npr.org*")})['href']
                print(result_url)
                html = urlopen(result_url).read().decode('utf-8')
                soup = BeautifulSoup(html, 'lxml')
                body=soup.find_all('p')
                for i in body[0:]:
                    body=i.get_text()
                    print(body+"\n"+"\n")        # Body
else:
    num=0
    for i in story_today[0:]:
        num=num+1
        ###Translation
        Title=i.find('h3',{"class":"title"}).get_text()
        print([num],Title+"\n"+"\n"+"\n")         # Title

    NOM=0
    num=0
    for i in story_today[NOM:]:
                num=num+1
                ###Translation
                Title=i.find('h3',{"class":"title"}).get_text()
                print([num],Title+"\n"+"\n"+"\n")
                result_url = i.find('a',{'href':re.compile("https://www.*")})['href']
                print(result_url)
                html = urlopen(result_url).read().decode('utf-8')
                soup = BeautifulSoup(html, 'lxml')
                body=soup.find_all('p')
                for i in body[0:]:
                    body=i.get_text()
                    print(body+"\n"+"\n")        # Body
