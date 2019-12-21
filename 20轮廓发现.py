import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
def contours_demo(image):
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary image",binary)
    contours,heiarchy = cv.findContours(binary, cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for i,contours in enumerate(contours):
        cv.drawContours(image,contours,-1,(0,0,255),-1)
        print(i)
    cv.imshow("detect contours", image)

src = cv.imread("/opencv/images/test.jpeg")
#cv.imshow("input image", src)
contours_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()