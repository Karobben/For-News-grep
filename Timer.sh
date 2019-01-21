#!/usr/bin/bash
while [ 1 > 10 ]
do
date=$(date| awk '{print $4}')
#echo $date
H_time=$(echo $date| sed 's/:/\t/g'|awk '{print $1}')
M_time=$(echo $date| sed 's/:/\t/g'|awk '{print $2}')

#echo $H_time $M_time

if [ $H_time -eq 6 ]
then
#echo "is about the time Houre"
	if [ $M_time -eq 57 ];then
		echo "lets do the job"
		date
                cat Nature.txt news.today >> TB.all
		./News-NPR.1.4.sh
#	else
#		echo "is not about the time"
fi
fi
sleep 50
done
