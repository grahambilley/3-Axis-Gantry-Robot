# INITIALIZATION
print('Initializing...')
import cv2
from cv_functions import make_dispensing_plan, take_picture, findAruco, ResizeWithAspectRatio, find_carts, pixels_to_mm, mm_to_pixels
from motor_functions import move_motor, move_to_home

# TAKE PICTURE OF CART TRAY
print('Taking picture of tray...')
# carts = take_picture()
imgName = 'Cart Tray with ArUco - Up Close.jpg'
imagePath = f'./Pictures/{imgName}'
img = cv2.imread(imagePath,0)

print('Locating cart edges...')
circles, dispense_locations, bbox, ids = find_carts(img)

# CREATE MOVEMENT PLAN
print('Creating dispensing plan...')
dispensing_plan = make_dispensing_plan(dispense_locations)

# MOVE ROBOT TO FILL CARTS
print('Moving home...')
move_to_home()

print('Executing dispensing plan...')
for movement in dispensing_plan:
    #print('moving x')
    move_motor('X', movement[0]/10, resolution='1/32')
    #print('moving y')
    move_motor('Y', movement[1]/10, resolution='1/32')
    #print('moving z 1')
    move_motor('Z',15, resolution='1/32')
    # Dispense....
    #print('moving z 2') 
    move_motor('Z',-15, resolution='1/32')

print('Moving home...')
move_to_home()
print('Filling Complete!')
