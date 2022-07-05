# INITIALIZATION
from cv_functions import take_picture, findAruco, ResizeWithAspectRatio, find_carts, pixels_to_mm, mm_to_pixels





# TAKE PICTURE OF CART TRAY
carts = take_picture()
carts_compressed = ResizeWithAspectRatio(carts, width=1000)
circles, dispense_locations = find_carts(carts_compressed)



# CREATE MOVEMENT PLAN






# MOVE ROBOT TO FILL CARTS







