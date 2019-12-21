import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary =  cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("ret",ret)
    cv.imshow("binary",binary)
    contours,heiarchy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x,y,w,h = cv.boundingRect(contour)
        mm = cv.moments(contour)
        if mm['m00'] != 0:
            cx = mm['m10']/mm['m00']
            cy = mm['m01']/mm['m00']
        else:
            cx,cy = 0,0
        print("area",area)
        approxCurve = cv.approxPolyDP(contour,4,True)
        cv.circle(image,(np.int(cx),np.int(cy)),3,(0,255,255),-1)
        cv.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        print(approxCurve)
        if approxCurve.shape[0] > 20:
            cv.drawContours(image,contours,i,(0,255,0),2)
    cv.imshow("measure_object",image)

src = cv.imread("/opencv/images/test.jpeg")
#cv.imshow("input image", src)
measure_object(src)
cv.waitKey(0)

cv.destroyAllWindows()