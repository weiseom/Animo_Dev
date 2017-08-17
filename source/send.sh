#! /bin/bash

sudo service motion start

while true
do
	scp -i /home/animo02/secret/soptAMSKey.pem -r /var/lib/motion/ ubuntu@52.78.63.210:/home/ubuntu/CNN/raw_image
	sudo rm -rf /var/lib/motion/*.jpg | sudo rm -rf /var/lib/motion/*.avi
done


