import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def big_image_bin(image):
    print(image.shape)
    cw = 256
    ch = 256
    h,w = image.shape[:2]
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    for row in range(0,h,ch):
        for col in range(0,w,cw):
            roi = gray[row:row+ch,col:col+cw]
            dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
            gray[row:row + ch, col:col + cw] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("//opencv/test1.jpeg", gray)


src = cv.imread("//opencv/test.jpeg")
#cv.imshow("input image", src)
big_image_bin(src)

cv.waitKey(0)

cv.destroyAllWindows()