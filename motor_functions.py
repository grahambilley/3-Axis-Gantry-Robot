# This .py file contains the function definitions for controlling the stepper motors.

from config import MOTOR_PINS, MOTOR_PARAMS, RESOLUTION, step_angle, SPR, CW, CCW


def move_motor(XYZ, distance, resolution='Full', travel_time=1, wait_time=0.5):
    DIR=MOTOR_PINS[XYZ]['DIR']      # This is the GPIO pin corresponding to the Direction GPIO output
    STEP=MOTOR_PINS[XYZ]['STEP']    # This is the GPIO pin corresponding to the Step GPIO output
    MODE=MOTOR_PINS[XYZ]['MODE']    # This is the GPIO pin corresponding to the Step Size GPIO outputs
    deg2mm=MOTOR_PARAMS[XYZ]['deg2mm']  # This corresponds to the pitc of the linear actuator
    res=RESOLUTION[resolution]      # This corresponds to the way the MODE pins need to be pulsed to move the motor in different step sizes

