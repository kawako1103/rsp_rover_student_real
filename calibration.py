from sensor import get_sensor

from drive import motor
import time

def calibrate():

    motor.rotate()
    gyro()

