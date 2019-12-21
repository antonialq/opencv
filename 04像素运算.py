import cv2 as cv
import numpy as np
import path_const

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("dst1",dst)


def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("dst2",dst)

def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("dst3",dst)

def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("dst4",dst)

def others(m1,m2):
    M1,dev1 = cv.meanStdDev(m1)
    M2,dev2 = cv.meanStdDev(m2)
    print(M1)
    print(M2)
    print(dev1)
    print(dev2)

def logic_demo(m1,m2):
    dst = cv.bitwise_and(m1,m2)
    cv.imshow("dst",dst)
    dst = cv.bitwise_not(m1, m2)
    cv.imshow("dst", dst)

def contrast_brightness_demo(image,c,b):
    h,w,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c,blank,1-c,b)
    cv.imshow("con_bri_demo",dst)


src1 = cv.imread(path_const.IMAGE_PATHS[0])
src2 = cv.imread(path_const.IMAGE_PATHS[0])
print(src1.shape)
print(src2.shape)
cv.imshow("image1", src1)
cv.imshow("image2", src2)
#add_demo(src1,src2)
#subtract_demo(src1,src2)
#divide_demo(src1,src2)
#multiply_demo(src1,src2)
logic_demo(src1,src2)
others(src1,src2)
contrast_brightness_demo(src1,2,0.8)
cv.waitKey(0)

cv.destroyAllWindows()