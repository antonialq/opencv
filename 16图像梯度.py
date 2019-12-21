import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
def lapalian_demo(image):
    dst = cv.Laplacian(image,cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian",lpls)

def soble_demo(image):
    grad_x = cv.Scharr(image,cv.CV_32F,1,0)
    grad_y = cv.Sobel(image,cv.CV_32F,0,1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient-x", gradx)
    cv.imshow("gradient-y", grady)

    gradxy = cv.addWeighted(gradx,0.5,grady,0.5,0)
    cv.imshow("gradient",gradxy)

src = cv.imread("/opencv/images/test.jpeg")
#cv.imshow("input image", src)
lapalian_demo(src)
soble_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()