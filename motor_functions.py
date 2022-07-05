# This .py file contains the function definitions for controlling the stepper motors.
import RPi.GPIO as GPIO
from config import MOTOR_PINS, MOTOR_PARAMS, RESOLUTION, step_angle, SPR, CW, CCW
from time import sleep

def move_motor(XYZ, distance, resolution='Full', speed=100, wait_time=0.25):
    #print('testing')
    DIR=MOTOR_PINS[XYZ]['DIR']      # This is the GPIO pin corresponding to the Direction GPIO output
    STEP=MOTOR_PINS[XYZ]['STEP']    # This is the GPIO pin corresponding to the Step GPIO output
    MODE=MOTOR_PINS[XYZ]['MODE']    # This is the GPIO pin corresponding to the Step Size GPIO outputs
    deg_per_mm=MOTOR_PARAMS[XYZ]['deg2mm']  # This corresponds to the pitc of the linear actuator
    res=RESOLUTION[resolution]['MODE']      # This corresponds to the way the MODE pins need to be pulsed to move the motor in different step sizes
    #print('res', res)
    steps_per_revolution=SPR*RESOLUTION[resolution]['count']
    #print('spr', steps_per_revolution)
    move_time = abs(distance/speed)
    
    # Number of degrees needed to move distance
    deg=abs(distance*deg_per_mm)

    #print('deg ',deg)
    # Convert degrees to total revolutions
    rev=deg/360
    #print('rev ',rev)
    # Convert to number of steps
    step_count=rev*steps_per_revolution
    #print('step count ',step_count)
    delay=move_time/step_count
    #print('delay ',delay)
    
    direction=1 if distance >=0  else 0   # Move clockwise for forward and counter clockwise for backward
    #print('dist',distance)
    #print('direction',direction)
    
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.setup(MODE, GPIO.OUT)
    GPIO.output(MODE, res)
    GPIO.output(DIR, direction)

    # Pulse the GPIO pins to move the motor
    for x in range(int(step_count)):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

    #print('sleeping ', wait_time, 'seconds')
    sleep(wait_time)
    #print('cleanup GPIO pins')
    GPIO.cleanup()

def move_to_home():
    return 
