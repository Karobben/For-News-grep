#!/data/data/com.termux/files/usr/bin/python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')

args = parser.parse_args()
INPUT = args.input

import fileinput
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re

import threading
import time

U_1="http://www.youdao.com/w/eng/"
U_2="/#keyfrom=dict2.index"

def job(line,NUM):
     if line == "\n" :
        Tran="\n"
     else:
      try:
        ## got translation on youdao
        body = line
        body=body.replace("\n",'')
        body=body.replace("    ",'')
        TR = body.replace("/"," or ")
        TR = TR.replace("\x95","")
        TR = TR.replace("—",",")
        TR = TR.replace("Þ","%C3%9E")
        TR = TR.replace("–",",")
        TR = TR.replace("#","")
        TR = TR.replace("’","%E2%80%99")
        TR = TR.replace("\"","%22T")
        TR = TR.replace("é","%C3%A9")
        TR = TR.replace("ó","%C3%B3")
        TR = TR.replace(" ","%20")
        TR = TR.replace("\xad","")
        TR = TR.replace("\xa0","")
        TR = TR.replace(":","%3A")
        TR = TR.replace(">","%3E")
        TR = TR.replace("+","%2B")
        TR = TR.replace("..","")
        TR = TR.replace("=","%3D")
        url2=U_1 + TR + U_2
        html = urlopen(url2).read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        ## Word or Sentence on the Anno
        Tran=soup.find(id="fanyiToggle")
        Tran=str(Tran)
        if Tran == 'None':            #This is a word
            Tran = str(soup.find(id="phrsListTab"))
            if Tran == 'None':
                Tran= 'None'  #this is a wrong word
            else:
                Tran = str(soup.find(id="phrsListTab").find_all("li"))
                if Tran =='[]':             #This word could only find on Internet
                    Tran=soup.find(id="tWebTrans")
                    Tran=Tran.find_all('span')
                    Tran=str(Tran).replace("[]","")
                    Tran=str(Tran).replace(" ","")
                    Tran=str(Tran).replace("\n","")
                    Tran=Tran.replace("<span>",'')
                    Tran=Tran.replace("</span>",'')
                else:                     #This word could find on official dictionary
                    Tran=Tran.replace("<li>",'')
                    Tran=Tran.replace("</li>",'')
        else:      # INPUT is a sentence or paragraph
            Tran=soup.find(id="fanyiToggle").find_all('p')[1].get_text()
      except:
        Tran="\n"
      print("\n",[NUM+0.1],"\n",[NUM+0.2],"\n",[NUM+0.3],line,"\n",[NUM+0.4],"\n",[NUM+0.5],"\n",[NUM+0.6],Tran)
      AAA = "\n" + str([NUM+0.1]) + "\n" + str([NUM+0.2]) + "\n" + str([NUM+0.3]) + line + "\n" + str([NUM+0.4]) + "\n" + str([NUM+0.5]) + "\n" + str([NUM+0.6]) + Tran
      print("AAA=",AAA)
      with open("OUTPUT", 'a') as f:
          f.write(AAA)


A_time = time.time()

NUM=0
body=""
for i in fileinput.input(INPUT):
    body=body+"##GAP##"+str(i)

body = body.split("##GAP##")
threads = []
files = range(len(body))
for i in files:
    NUM=NUM+1
    t = threading.Thread(target=job,args=([body[i],NUM,]))
    threads.append(t)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()

print(time.time()-A_time)
