# This .py file contains the function definitions for controlling the stepper motors.

from config import MOTOR_PINS, MOTOR_PARAMS, RESOLUTION, step_angle, SPR, CW, CCW
import RPi.GPIO as GPIO
from time import sleep

def move_motor(XYZ, direction, distance, resolution='Full', travel_time=1, wait_time=0.05):
    DIR=MOTOR_PINS[XYZ]['DIR']      # This is the GPIO pin corresponding to the Direction GPIO output
    STEP=MOTOR_PINS[XYZ]['STEP']    # This is the GPIO pin corresponding to the Step GPIO output
    MODE=MOTOR_PINS[XYZ]['MODE']    # This is the GPIO pin corresponding to the Step Size GPIO outputs
    deg2mm=MOTOR_PARAMS[XYZ]['deg2mm']  # This corresponds to the pitc of the linear actuator
    res=RESOLUTION[resolution]['mode']      # This corresponds to the way the MODE pins need to be pulsed to move the motor in different step sizes
    step_count=SPR*RESOLUTION[resolution]['count']
    delay=travel_time/step_count

    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(MODE, GPIO.OUT)
    GPIO.output(MODE, res)
    GPIO.output(DIR, direction)

    # Pulse the GPIO pins to move the motor
    for x in range(step_count):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    sleep(wait_time)
    GPIO.cleanup()

