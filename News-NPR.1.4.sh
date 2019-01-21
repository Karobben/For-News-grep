#!/usr/bin/bash
date
echo greping NPR News
./NPR-news.1.02.py > news.today
date
echo news annotating
./annotation.py
#echo translating NPR News
#./Trans.2.01.py -i news.today > news-T
#date
echo greping Nature News
./Nature.2.01.py > Nature.txt
#date
#echo translating Nature News
#./Trans.2.01.py -i Nature.txt > Nature-T
date
echo sending email

list=$(echo "cjy.100@163.com 1197001742@qq.com 591465908@qq.com 2125897391@qq.com M18117625258_2@KINDLE.CN 1198221810@qq.com 925306583@qq.com 8615595984208@KINDLE.CN 694196156@qq.com 1415059638@qq.com 1002067297@qq.com 386982854@qq.com 861489075@qq.com 793703572@qq.com 1007642425@qq.com")

#list=$(echo "1197001742@qq.com 591465908@qq.com ")

for i in $list;
do
echo sengding to $i
./Mail.3.1.py -i "news.today , Nature.txt , annotated.news" -R $i -b information_for_mail;
done


