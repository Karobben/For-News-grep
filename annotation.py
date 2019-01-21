#!/usr/local/bin/python3.7
import re, os

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

f = open("news.today",'r')
A = f.read()

f = open('Uf','r')
B = f.read().split('\n')[:-1]

for i in B:
  A = re.sub(r"\b%s\b"%i,"\x1b[7;41;1m"+i+'\x1b[0m',A)

result=''
for i in A.split("\n"):
  L1 = list(find_all(i,"\x1b[7;41;1m"))
  L2 = list(find_all(i,"\x1b[0m"))
  for ii in range(len(L1)):
    word = i[L1[ii]+9:L2[ii]]
    Line = os.popen("awk '{print $2}' Uf.DB | grep -w -n "+word+"| awk -F: '{print $1}'").read().replace('\n','')
    word_ex = os.popen("awk 'NR=="+Line+"{print}' Uf.DB | awk -F'\t' '{print $3$4$5}'").read()
    i += "\n"+word_ex+'\n'
  result += i + '\n'
result = result.replace('\n\n','\n').replace('\n\n','\n')
f = open('annotated.news','w')
f.write(result)
