#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
import serial_test 
import time
import atexit

mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
	mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
	mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
 
atexit.register(turnOffMotors)

myMotorL = mh.getMotor(3)
myMotorR = mh.getMotor(4)
myMotorL.setSpeed(150)
myMotorR.setSpeed(150)

while (True):
	print "Forward! "
   	myMotorL.run(Adafruit_MotorHAT.FORWARD)
	myMotorR.run(Adafruit_MotorHAT.FORWARD)

    	print "\tSpeed up..."
    	for i in range(255):
    		myMotorL.setSpeed(i)
		myMotorR.setSpeed(i)
    		time.sleep(0.01)
     
    	print "\tSlow down..."
    	for i in reversed(range(255)):
    		myMotorL.setSpeed(i)
		myMotorR.setSpeed(i)
    		time.sleep(0.01)
     
    	print "Backward! "
    	myMotorL.run(Adafruit_MotorHAT.BACKWARD)
	myMotorR.run(Adafruit_MotorHAT.BACKWARD)

    	print "\tSpeed up..."
    	for i in range(255):
    		myMotorL.setSpeed(i)
		myMotorR.setSpeed(i)

    		time.sleep(0.01)
     
    	print "\tSlow down..."
    	for i in reversed(range(255)):
    		myMotorL.setSpeed(i)
		myMotorR.setSpeed(i)

    		time.sleep(0.01)
     
    	print "Release"
    	myMotorL.run(Adafruit_MotorHAT.RELEASE)
	myMotorR.run(Adafruit_MotorHAT.RELEASE)

    	time.sleep(1.0)
