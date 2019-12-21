import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def detect_circle_demo(image):
    dst = cv.pyrMeanShiftFiltering(image,10,100)
    cimage = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(cimage,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)
    cv.imshow("circles",image)


src = cv.imread("/Users/qing.liu/PycharmProjects/毕设准备/opencv/test.jpeg")
#cv.imshow("input image", src)
detect_circle_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()