import cv2 as cv
import numpy as np
import path_const

def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo", dst)

def gause_demo(image):
    dst = cv.GaussianBlur(image, (0,0), 15)
    cv.imshow("gause demo", dst)

def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 50)
    cv.imshow("shift_demo", dst)

src = cv.imread(path_const.IMAGE_PATHS[3])
cv.imshow("input image", src)
bi_demo(src)
gause_demo(src)
shift_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()