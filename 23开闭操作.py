import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
'''
【开操作】腐蚀+膨胀-帮助消除图像中小的干扰区域
【闭操作】膨胀+腐蚀-填充小的封闭区域
 水平或者垂直线提取
'''

def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    binary = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("open-result",binary)

def close_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    binary = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("close_demo",binary)

src = cv.imread(path_const.IMAGE_PATHS[2])
#cv.imshow("input image", src)
open_demo(src)
close_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()