from time import sleep
import RPi.GPIO as GPIO

CW = 1    # Clockwise Rotation 
CCW = 0   # Counterclockwise Rotation
SPR = 200 # Steps per Revolution in full-step mode (Step angle of 1.8 degrees)

GPIO.setmode(GPIO.BCM)
RESOLUTION = {'Full': {'MODE':(0, 0, 0),
                       'count':1},
              'Half': {'MODE':(1, 0, 0),
                       'count':2},
              '1/4' : {'MODE':(0, 1, 0),
                       'count':4},
              '1/8' : {'MODE':(1, 1, 0),
                       'count':8},
              '1/16': {'MODE':(0, 0, 1),
                       'count':16},
              '1/32': {'MODE':(1, 0, 1),
                        'count':32}}

step_count = SPR*32
delay = 1/step_count


# Move the Z Motor
DIR = 20  # Direction GPIO Pin
STEP = 21 # Step GPIO Pin
MODE = (14, 15, 18)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE, RESOLUTION['1/32'])

# Travel CW
GPIO.output(DIR, CW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(0.5)

# Travel CCW
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(0.5)    
    
# Move the Y Motor
DIR = 23  # Direction GPIO Pin
STEP = 24 # Step GPIO Pin
MODE = (10, 9, 11)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE, RESOLUTION['1/32'])

# Travel CW
GPIO.output(DIR, CW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(0.5)

# Travel CCW
GPIO.output(DIR, CCW)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    
sleep(0.5)      


# Move the X Motor
DIR = 5  # Direction GPIO Pin
STEP = 6 # Step GPIO Pin
MODE = (2, 3, 4)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(MODE, GPIO.OUT)
GPIO.output(MODE, RESOLUTION['1/32'])
print('setup complete')

# Travel CW
GPIO.output(DIR, CW)
print('moving CW')
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

print('moving CW complete')
sleep(0.5)


# Travel CCW
GPIO.output(DIR, CCW)
print('moving CCW')
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

print('moving CCW complete')
GPIO.cleanup()

