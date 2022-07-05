# This .py file contains functions related to computer vision and image processing.

from pickle import NONE
import time
import PIL as Image
import numpy as np
import cv2 # From package opencv-python
import cv2.aruco as aruco # From package opencv-contrib-python


def pixels_to_mm(pix):
    return pix  # Need to define thr relationship



def mm_to_pixels(mm):
    return mm  # Need to define thr relationship



# Take an picture from the webcam
def take_picture(name='img1.png', savePic=False):
    cap = cv2.VideoCapture(1)
    if cap.isOpened():
        r, f = cap.read() # Initialize camera
        time.sleep(1)
        ret, frame = cap.read()
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)     
        im = Image.fromarray(img1)
        im.save(name) if savePic == True else NONE
        cap.release()
        return im
    else:
        cap.release()



# Compress image by a factor f
def compress(image, f=4, name='Compressed img1.png'):
    width, height = image.size
    w2 = int(np.floor(width/f))
    h2 = int(np.floor(height/f))
    im2 = image.resize((w2,h2))
    im2.save(name, optimize=True, quality = 100)
    return im2



# Read an image with ArUco markers
def findAruco(img, marker_size=6, total_markers=250, draw=True):
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key=getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
    arucoDict=aruco.Dictionary_get(key)
    arucoParam=aruco.DetectorParameters_create()
    bbox,ids,_=aruco.detectMarkers(gray,arucoDict,parameters=arucoParam)
    if draw:
        aruco.drawDetectedMarkers(img,bbox)
    return bbox, ids



def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=inter)



# Find and label circles in the image (as a function)
def find_carts(img):
#     img = cv2.imread(imagePath,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=40, param1=50, param2=40, minRadius=60, maxRadius=90)
    circles = np.uint16(np.around(circles))
    dispense_locations = np.round(np.array([circles[0][:,0],(circles[0][:,1]-0.6*circles[0][:,2])]).T).astype('int')

    # This will dispense along one row of carts, then move down one row
    d = dispense_locations
    d = d[d[:, 1].argsort()]  # Sort by column value
    d = np.hstack((d, np.concatenate([([i]*10) for i in range(10)], axis=0).reshape(100,1))) # Add group number
    d = d[np.lexsort((d[:,0],d[:,2]))]  # Sort by row number within each group
    
    for idx, i in enumerate(circles[0,:]):
        # draw the outer circle
        cv2.circle(cimg,center=(i[0],i[1]),radius=i[2],color=(0,255,0),thickness=5)
        # draw the center of the circle
        cv2.circle(cimg,center=(i[0],i[1]),radius=2,color=(0,0,255),thickness=8)
        # draw a tiny circle where the needle should dispense
        cv2.circle(cimg,center=(d[idx,0],d[idx,1]),radius=1,color=(255,0,255),thickness=idx)

    compcimg = ResizeWithAspectRatio(cimg, width=1050)
    bbox, ids = findAruco(compcimg)
    cv2.imshow('detected circles',compcimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return circles, d, bbox, ids