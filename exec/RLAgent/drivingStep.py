import random
import numpy as np

from SensorController import MSSensor
from MotorController import MotorController
import time 

class GameState:
    def __init__(self):
		#MotorController
        self.sensor = MSSensor(35)
        self.motor=MotorController()

        # Global-ish.
        self.crashed = False

        # Record steps.
        self.num_steps = 0


    def frame_step(self, action):

        if action == 0:  # Turn left.
            self.motor.driveLeft()
            time.sleep(0.8)

        elif action == 1:  # Turn right.
            self.motor.driveRight()
            time.sleep(0.8)

        elif action == 2:
            self.motor.driveForward()


        # Get the current location and the readings there.
        readings = self.get_sonar_readings()
        state = np.array([readings])

        # Set the reward.
        # Car crashed when any reading == 1
        if self.car_is_crashed(readings):
            self.crashed = True
            reward = -500
            self.recover_from_crash()
        else:
            # Higher readings are better, so return the sum.
            reward = -5 + int(self.sum_readings(readings) / 10)
        self.num_steps += 1

        return reward, state

    def car_is_crashed(self, readings):
        if readings[1] < 5:
            return True
        else:
            return False

    def recover_from_crash(self):
        """
        We hit something, so recover.
        """
        while self.crashed:
            # Go backwards.
            self.motor.driveBackward()
            time.sleep(0.8)
            self.crashed = False

    def sum_readings(self, readings):
        """Sum the number of non-zero readings."""
        tot = 0
        for i in readings:
            tot += i
        return tot

    def get_sonar_readings(self):
        readings = []
        readings = self.sensor.getDistance()
       
        return readings

if __name__ == "__main__":
    game_state = GameState()
    while True:
        game_state.frame_step((random.randint(0, 2)))
