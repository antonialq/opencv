import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const
def threhold_demo(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray,127,255,cv.THRESH_TOZERO | cv.THRESH_OTSU)
    print("threshold value %s "%(ret))
    cv.imshow("binary",binary)

def local_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10)
    cv.imshow("local_threshold",dst)

def custom_threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray, [1,w*h])
    mean = m.sum() /(w*h)
    print("mean :",mean)
    ret, custom = cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    cv.imshow("custom_threshold",custom)

src = cv.imread("//opencv/test.jpeg")
cv.imshow("input image", src)
local_threshold(src)
cv.waitKey(0)

cv.destroyAllWindows()