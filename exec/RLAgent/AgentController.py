#!/usr/bin/python
import time

from SensorController import MSSensor
from MotorController import MotorController

class AgentController:

    def __init__(self):
        print("[AgentController] init\n")
        self.mssnsr=MSSensor(35)
        self.motor=MotorController()
        
    def release(self):
        self.motor.turnOffMotors()
        print("hoho~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        
    def execute(self):
        while True:
            #time.sleep(0.5)
            self.mssnsr.getDistance()
            flag=self.mssnsr.checkDistance()
    
            print("flag-------------")
            check=flag[1::2]
            right = check[0]
            left = check[1]
            front = check[2]
            #right = check[2]
            #right = 1
            
            print("check-------------")
            print(check)

            if front == 1 and left == 1 and right == 1:
                #stop
                print("[AgentController] danger in front\n")
                self.motor.driveBackward()
            elif front == 1 and left == 1:
                #right
                print("[AgentController] danger in left\n")
                self.motor.driveRight()
            elif front == 1 and right == 1:
                #left
                print("[AgentController] danger in right\n")
                self.motor.driveLeft()
            elif front == 1:
                #backward
                print("[AgentController] danger in front\n")
                self.motor.driveBackward()
            else:
                #front
                print("[AgentController] gogo\n")
                self.motor.driveForward()
                
'''        
            if left == 1 and right == 1:
                #stop
                print("[AgentController] danger in front\n")
                self.motor.driveBackward()                
            elif left == 1:
                #right
                print("[AgentController] danger in left\n")
                self.motor.driveRight()
            elif right == 1:
                #left
                print("[AgentController] danger in right\n")
                self.motor.driveLeft()
            else:
                #front
                print("[AgentController] gogo\n")
                self.motor.driveForward()

            elif left == 1:
                #right
                print("[AgentController] danger in right\n")
                self.motor.driveLeft()
'''
