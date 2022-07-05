# This .py file contains the function definitions for controlling the stepper motors.

from asyncio.windows_events import NULL
import RPi.GPIO as GPIO
from config import MOTOR_PINS, MOTOR_PARAMS, RESOLUTION, step_angle, SPR, CW, CCW
from time import sleep

def move_motor(XYZ, distance, resolution='Full', travel_time=1, wait_time=0.05):
    DIR=MOTOR_PINS[XYZ]['DIR']      # This is the GPIO pin corresponding to the Direction GPIO output
    STEP=MOTOR_PINS[XYZ]['STEP']    # This is the GPIO pin corresponding to the Step GPIO output
    MODE=MOTOR_PINS[XYZ]['MODE']    # This is the GPIO pin corresponding to the Step Size GPIO outputs
    deg_per_mm=MOTOR_PARAMS[XYZ]['deg2mm']  # This corresponds to the pitc of the linear actuator
    res=RESOLUTION[resolution]['MODE']      # This corresponds to the way the MODE pins need to be pulsed to move the motor in different step sizes
    steps_per_revolution=SPR*RESOLUTION[resolution]['count']
   
    # Number of degrees needed to move distance
    deg=distance*deg_per_mm
    # Convert degrees to total revolutions
    rev=deg/360
    # Convert to number of steps
    step_count=rev*steps_per_revolution

    delay=travel_time/step_count    
    dir=1 if distance>0  else 0   # Move clockwise for forward and counter clockwise for backward
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(MODE, GPIO.OUT)
    GPIO.output(MODE, res)
    GPIO.output(DIR, dir)

    # Pulse the GPIO pins to move the motor
    for x in range(int(step_count)):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    sleep(wait_time)
    GPIO.cleanup()


def move_to_home():
    return NULL