#! /bin/bash

#python serial_test.py

sudo service motion start
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.78.63.210:8008/darknet

while true
do
	sleep 1
	scp -i /home/animo02/secret/soptAMSKey.pem /var/lib/motion/lastsnap.jpg ubuntu@52.78.63.210:/home/ubuntu/CNN/motion
	sudo rm -rf /var/lib/motion/01-*.jpg | sudo rm -rf /var/lib/motion/*.avi
done



#a=$(curl -sb -H "Accept: application/json" -H "Content-Type: application/json" http://52.78.63.210$

#echo "a is : ${a}"

