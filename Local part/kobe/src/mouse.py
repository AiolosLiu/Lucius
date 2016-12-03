import cv2, os
import numpy as np

ix, iy = -1, -1


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ix, iy = x, y
        print('ix,iy',ix,iy)


# Create a black image, a window and bind the function to window
dirname = '/home/ming/AI/faces/raw_face/0'
os.chdir(dirname)

img = cv2.imread('1.jpg')
# cv2.imshow('image', img)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print ix, iy
cv2.destroyAllWindows()
