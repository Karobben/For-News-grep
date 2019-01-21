#!/usr/local/bin/python3.7
import argparse

#命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件

#获取参数
args = parser.parse_args()

INPUT = args.input


####grep information from uniprot
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re



## got translation on youdao
TR = INPUT.replace("/"," or ")
TR = TR.replace(" ","%20")
TR = TR.replace(":","%3A")
TR = TR.replace(">","%3E")
TR = TR.replace("+","%2B")
TR = TR.replace("=","%3D")

U_1="http://www.youdao.com/w/eng/"
U_2="/#keyfrom=dict2.index"
url2=U_1 + TR + U_2
html = urlopen(url2).read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')


### Word or Sentence on the Anno



Tran=soup.find(id="fanyiToggle")
Tran=str(Tran)

if Tran == 'None':            #This is a word
    Tran = str(soup.find(id="phrsListTab"))
    if Tran == 'None':
        Tran=soup.find_all('a',{'class':"search-js"})  #this is a wrong word
        print("The word \""+INPUT+ "\" has not been found. Do you mean"+"\n")
        for m in Tran:
            print(m.get_text())
    else:
        Tran = str(soup.find(id="phrsListTab").find_all("li"))
        if Tran =='[]':             #This word could only find on Internet
            print("None")
            Tran=soup.find(id="tWebTrans")
            Tran=Tran.find_all('span')
            Tran=str(Tran).replace("[]","")
            Tran=str(Tran).replace(" ","")
            Tran=str(Tran).replace("\n","")
            Tran=Tran.replace("<span>",'')
            Tran=Tran.replace("</span>",'')
            print(INPUT+"\t"+Tran)
        else:                     #This word could find on official dictionary
            Tran=Tran.replace("<li>",'')
            Tran=Tran.replace("</li>",'')
            if str(soup.find('span',{'class':"phonetic"})) == "None":
                print(INPUT+"\t"+Tran)
            else:
                Pro=soup.find('span',{'class':"phonetic"}).get_text()
                print(INPUT+" "+Pro+"\t"+Tran)
else:      # INPUT is a sentence or paragraph
    Tran=soup.find(id="fanyiToggle").find_all('p')[1].get_text()
    print(INPUT+"\n"+Tran)
