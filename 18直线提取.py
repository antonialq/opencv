import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0+1000*(-b))
        y1 = int(x0 + 1000 * (a))
        x2 = int(x0 + 1000 * (-b))
        y2 = int(x0 + 1000 * (a))
        dst = cv.line(image,(x1,y1),(x2,y2),(0,0,255,2))
    cv.imshow("line",dst)

def line_detect_possible_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLinesP(edges,1,np.pi/180,200,minLineLength=50,maxLineGap=10)
    for line in lines:
        x1,y1,x2,y2 = line[0]
        dst = cv.line(image,(x1,y1),(x2,y2),(0,0,255,2))
    cv.imshow("line1", dst)


src = cv.imread("/Users/qing.liu/PycharmProjects/毕设准备/opencv/test.jpeg")
#cv.imshow("input image", src)
line_detection(src)
line_detect_possible_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()