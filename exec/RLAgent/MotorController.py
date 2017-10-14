#!/usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit

# Speed / direction Controller
# issue : left motor's speed is slower than R's

class MotorController:

        mh = Adafruit_MotorHAT(addr=0x60)

        def __init__(self):
                print("motor init")
                atexit.register(self.turnOffMotors)
                self.defaultSpeedValue = 50
                self.resetSpeedValue = 45
                self.myMotorL = MotorController.mh.getMotor(3)
                self.myMotorR = MotorController.mh.getMotor(4)
                self.myMotorL.setSpeed(self.defaultSpeedValue)
                self.myMotorR.setSpeed(self.defaultSpeedValue)

        def turnOffMotors(self):
                MotorController.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
                MotorController.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

        def driveForward(self):
                print("Forward!")
                self.speedSetup(self.resetSpeedValue)
                self.myMotorL.run(Adafruit_MotorHAT.FORWARD)
                self.myMotorR.run(Adafruit_MotorHAT.FORWARD)

        def driveRight(self):
                print("Right!")
                self.myMotorL.run(Adafruit_MotorHAT.FORWARD)
                self.myMotorR.run(Adafruit_MotorHAT.FORWARD)
                for i in range(self.resetSpeedValue, 300):
                        self.myMotorL.setSpeed(i)
                self.speedSetup(self.resetSpeedValue)


        def driveLeft(self):
                print("Left!")
                #for i in range(self.speedValue, 200):
                self.myMotorL.run(Adafruit_MotorHAT.FORWARD)
                self.myMotorR.run(Adafruit_MotorHAT.FORWARD)
                for i in range(self.resetSpeedValue, 300):
                	self.myMotorR.setSpeed(i)
                #time.sleep(0.005)
                self.speedSetup(self.resetSpeedValue)

        def driveBackward(self):
                print("Backward! ")
                self.myMotorL.run(Adafruit_MotorHAT.BACKWARD)
                self.myMotorR.run(Adafruit_MotorHAT.BACKWARD)
                self.speedSetup(70)

        def driveRelease(self):
                print("Release")
                self.myMotorL.run(Adafruit_MotorHAT.RELEASE)
                self.myMotorR.run(Adafruit_MotorHAT.RELEASE)
                time.sleep(1.0)
                
        def speedSetup(self, val):
                val2 = val + 10
                self.myMotorL.setSpeed(val2)
                self.myMotorR.setSpeed(val)
                
        def speedUpControl(self):
                print("\tSpeed up...")
                for i in range(self.resetSpeedValue, 100):
                        self.myMotorL.setSpeed(i)
                        self.myMotorR.setSpeed(i)
                        time.sleep(0.01)

        def speedDownControl(self):
                print("\tSlow down...")
                for i in reversed(list(range(self.resetSpeedValue, 100))):
                        self.myMotorL.setSpeed(i)
                        self.myMotorR.setSpeed(i)
                        time.sleep(0.01)
