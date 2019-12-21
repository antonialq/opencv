import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def open_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV |cv.THRESH_OTSU)
    cv.imshow("binary",binary)
'''
【开操作】腐蚀+膨胀-帮助消除图像中小的干扰区域
【闭操作】膨胀+腐蚀-填充小的封闭区域
 水平或者垂直线提取
'''
src = cv.imread("/Users/qing.liu/PycharmProjects/毕设准备/opencv/test.jpeg")
#cv.imshow("input image", src)

cv.waitKey(0)

cv.destroyAllWindows()