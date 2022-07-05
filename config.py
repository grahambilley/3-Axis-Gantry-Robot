# Motor Parameters
MOTOR_PARAMS = {'X':{'deg2mm':1.8},
                'Y':{'deg2mm':1.8},
                'Z':{'deg2mm':1.8}}

step_angle = 1.8
SPR = 360/step_angle # 200 Steps per Revolution with step angle of 1.8 degrees
CW = 1    # Clockwise Rotation
CCW = 0   # Counterclockwise Rotation

# Motor Pin Assignment
MOTOR_PINS = {'X':{'DIR' :5,
                   'STEP':6,
                   'MODE':(2,3,4)},
               'Y':{'DIR' :23,
                   'STEP':24,
                   'MODE':(10,9,11)},
              'Z':{'DIR' :20,
                   'STEP':21,
                   'MODE':(14,15,18)}}

# Raspberry Pi Pin Assignment

# Resolution Dictionary for Stepper Motors
RESOLUTION = {'Full': {'MODE':(0, 0, 0),
                       'count':1},
              'Half': {'MODE':(0, 0, 1),   #(1, 0, 0)
                       'count':2},
              '1/4' : {'MODE':(0, 1, 0),
                       'count':4},
              '1/8' : {'MODE':(1, 1, 0),
                       'count':8},
              '1/16': {'MODE':(1, 0, 0),   #(0, 0, 1)
                       'count':16},
              '1/32': {'MODE':(1, 0, 1),
                        'count':32}}

