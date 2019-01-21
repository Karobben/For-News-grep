#!/usr/local/bin/python3.7
#########
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i','-I','--input')     #输入文件

args = parser.parse_args()
INPUT = args.input

###########
print("Let the fun begin")
import urllib.request
import urllib.parse
import json
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re, time, pyperclip, fileinput
import multiprocessing as mp

def Trans_long(content,NUM):
  url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
  data = {        #表单数据
              'i': content,
              'from': 'AUTO',
              'to': 'AUTO',
              'smartresult': 'dict',
              'client': 'fanyideskweb',
              'doctype': 'json',
              'version': '2.1',
              'keyfrom': 'fanyi.web',
              'action': 'FY_BY_CLICKBUTTION',
              'typoResult': 'false'
          }
  data=urllib.parse.urlencode(data).encode('utf-8')
  response=urllib.request.urlopen(url,data)
  html=response.read().decode('utf-8')
  target=json.loads(html)
  result = ""
  #for i in range(len(target['translateResult'][0])):
  result += str([NUM+0.1])+target['translateResult'][0][0]['src']+"\n" + str([NUM+0.2])+target['translateResult'][0][0]['tgt'] + '\n'
  print("re= ",result)
  with open("OUTPUT", 'a') as f:
    f.write(result)

NUM=0
body=[]
for i in fileinput.input(INPUT):
    body += [str(i)]


def multicore():
  NUM = 0
  pool = mp.Pool(processes=200)
  for i in range(len(body)):
    NUM +=1
    multi_res = [pool.apply_async(Trans_long,(body[i],NUM,))]
  pool.close()
  pool.join()

if __name__ == '__main__':
    multicore()
