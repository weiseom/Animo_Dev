#! /bin/bash

#python serial_test.py

sudo service motion start
curl -i -H "Accept: application/json" -H "Content-Type: application/json" http://52.78.63.210:8008/darknet

while true
do
	scp -i /home/animo02/secret/soptAMSKey.pem -r /var/lib/motion/ ubuntu@52.78.63.210:/home/ubuntu/CNN
	sudo rm -rf /var/lib/motion/*.jpg | sudo rm -rf /var/lib/motion/*.avi
done


