import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const

'''
【顶帽】开操作与原图像相减
【黑帽】闭操作与愿图像相减
【基本梯度】
【内梯度】
【外梯度】
'''

def top_hat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    dst = cv.add(dst,cimage)
    cv.imshow("top hat",dst)

def black_hat_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_BLACKHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    dst = cv.add(dst,cimage)
    cv.imshow("top hat",dst)

def gradient(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dm = cv.dilate(image,kernel)
    em = cv.erode(image,kernel)
    dst1 = cv.subtract(image,em)
    dst2 = cv.subtract(dm,image)
    cv.imshow("internel",dst1)
    cv.imshow("outer", dst2)

src = cv.imread(path_const.IMAGE_PATHS[2])
#cv.imshow("input image", src)
top_hat_demo(src)
black_hat_demo(src)
gradient(src)
cv.waitKey(0)

cv.destroyAllWindows()