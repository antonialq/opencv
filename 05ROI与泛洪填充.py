import cv2 as cv
import numpy as np
import path_const

def fill_color_demo(image):
    copyimg = image.copy()
    h,w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copyimg,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill result",copyimg)


def fill_binary_demo():
    image = np.zeros([400,400,3],np.uint8)
    image[100:300,100:300,:] = 255
    cv.imshow("fill Bresult",image)
    h, w = image.shape[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    mask[101:301,101:301] = 0
    cv.floodFill(image,mask,(200,200),(0,0,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("fill B",image)

#region of interest
src = cv.imread(path_const.IMAGE_PATHS[0])
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
face = src[200:400,100:300]
cv.imshow("face",face)
face = cv.bitwise_not(face)
src[200:400,100:300] = face
cv.imshow("result",src)
#fill_color_demo(src)
fill_binary_demo()
cv.waitKey(0)
cv.destroyAllWindows()
