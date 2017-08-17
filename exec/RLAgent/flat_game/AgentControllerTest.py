#!/usr/bin/python

from SensorController import MSSensor
from MotorController import MotorController

class AgentController:

    def __init__(self):
        print("[AgentController] init\n")
        self.mssnsr=MSSensor(20)
        self.motor=MotorController()
        
    def execute(self):
        while True:
                check=self.mssnsr.getDistance()
                print(check)
