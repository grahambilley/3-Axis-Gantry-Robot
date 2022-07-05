# INITIALIZATION
print('Initializing...')
from cv_functions import make_dispensing_plan, take_picture, findAruco, ResizeWithAspectRatio, find_carts, pixels_to_mm, mm_to_pixels
from motor_functions import move_motor, move_to_home

# TAKE PICTURE OF CART TRAY
print('Taking picture of tray...')
carts = take_picture()
print('Compressing picture for faster processing...')
carts_compressed = ResizeWithAspectRatio(carts, width=1000)
print('Locating cart edges...')
circles, dispense_locations, _ = find_carts(carts_compressed)

# CREATE MOVEMENT PLAN
print('Creating dispensing plan...')
dispensing_plan = make_dispensing_plan(dispense_locations)

# MOVE ROBOT TO FILL CARTS
print('Moving home...')
move_to_home()
print('Executing dispensing plan...')
for movement in dispensing_plan:
    move_motor('X', movement[0])
    move_motor('Y', movement[1])
    move_motor('Z',5)
    # Dispense....
    move_motor('Z',-5)
print('Moving home...')
move_to_home()

print('Filling Complete!')