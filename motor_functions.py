# This .py file contains the function definitions for controlling the stepper motors.

from config import MOTOR_PINS


def move_motor(XYZ, distance, resolution='Full', travel_time=1, wait_time=0.5):
    pins=MOTOR_PINS[XYZ]
    DIR=pins['DIR']
    STEP=pins['STEP']
    MODE=pins['MODE']
    deg2mm=pins['deg2mm']