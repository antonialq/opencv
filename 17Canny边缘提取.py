import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
【canny算法介绍】
高斯模糊-灰度转换-计算梯度-非最大信号抑制-高低阈值输出二值图像
'''

def edge_demo(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    ygrad = cv.Sobel(gray,cv.CV_16SC1,1,0)
    edge_output = cv.Canny(xgrad,ygrad,50,150)
    cv.imshow("Canny Edge",edge_output)

    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow("Color Edge",dst)

src = cv.imread("/Users/qing.liu/PycharmProjects/毕设准备/opencv/test.jpeg")
#cv.imshow("input image", src)
edge_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()