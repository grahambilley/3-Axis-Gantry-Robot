# Motor Parameters
from sandbox import RESOLUTION


step_angle = 1.8
SPR = 360/step_angle # 200 Steps per Revolution with step angle of 1.8 degrees
CW = 1    # Clockwise Rotation
CCW = 0   # Counterclockwise Rotation

# Motor Pin Assignment
MOTOR_PINS = {'X':{'DIR' :5,
                   'STEP':6,
                   'MODE':(2,3,4),
                   'deg2mm': 1}, # This needs to be calibrated
              'Y':{'DIR' :23,
                   'STEP':24,
                   'MODE':(10,9,11),
                   'deg2mm': 1}, # This needs to be calibrated
              'Z':{'DIR' :20,
                   'STEP':21,
                   'MODE':(14,15,18),
                   'deg2mm': 1}, # This needs to be calibrated
             }

# Raspberry Pi Pin Assignment

# Resolution Dictionary for Stepper Motors
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4' : (0, 1, 0),
              '1/8' : (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

