# INITIALIZATION
from cv_functions import make_dispensing_plan, take_picture, findAruco, ResizeWithAspectRatio, find_carts, pixels_to_mm, mm_to_pixels
from motor_functions import move_motor, move_to_home





# TAKE PICTURE OF CART TRAY
carts = take_picture()
carts_compressed = ResizeWithAspectRatio(carts, width=1000)
circles, dispense_locations, _ = find_carts(carts_compressed)



# CREATE MOVEMENT PLAN
dispensing_plan = make_dispensing_plan(dispense_locations)





# MOVE ROBOT TO FILL CARTS
move_to_home






