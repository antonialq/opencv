import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst = cv.erode(binary,kernel)
    cv.imshow("erode_image",dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.dilate(binary,kernel)
    cv.imshow("dilate_image",dst)

src = cv.imread("/opencv/images/test.jpeg")
#cv.imshow("input image", src)
erode_demo(src)
dilate_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()