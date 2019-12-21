'''
色彩空间
RGB
HSV H(0-180)
HIS
YCrCb
YUV-linux default
'''
import cv2 as cv
import numpy as np

def extract_object_demo(image):
    capture = cv.VideoCapture("")
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame,cv.COLOR_HSV2BGR)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv,lowerb=lower_hsv,upperb=upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("mask",dst)
        c = cv.waitKey(40)
        if c == 27:
            break

def color_space_demo(image):
    #gray = cv.cvtColor(image,cv.COLOR_GRAY2BGR)
    #cv.imshow("gray",gray)
    hsv = cv.cvtColor(image,cv.COLOR_HSV2BGR)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image,cv.COLOR_YUV2BGR)
    cv.imshow("yuv",yuv)
    Crcv = cv.cvtColor(image, cv.COLOR_RGB2YCrCb)
    cv.imshow("crcv", Crcv)

src = cv.imread("//opencv/WechatIMG1.jpeg")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image", src)
b,g,r = cv.split(src)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)
src[:,:,2]= 0
cv.imshow("change",src)
src = cv.merge([b,g,r])
cv.imshow("merge",src)
color_space_demo(src)
cv.waitKey(0)