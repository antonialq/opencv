import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def back_projection_demo():
    sample = cv.imread("//opencv/test.jpeg")
    target = cv.imread("//opencv/WechatIMG1.jpeg")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2GRAY)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2GRAY)

    cv.imshow("sample", sample)
    cv.imshow("target",target)

    roiHist = cv.calcHist([roi_hsv],[0,1],None,[36,48],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject(target,[0,1],roiHist,[0,180,0,256],1)
    cv.imshow("back projection demo",dst)

def hist2d_demo(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
    plt.imshow(hist,interpolation='nearest')
    plt.title("hist")
    plt.show()


src1 = cv.imread("//opencv/test.jpeg")
src2 = cv.imread("//opencv/WechatIMG1.jpeg")
back_projection_demo()
#hist2d_demo(src1)
cv.waitKey(0)

cv.destroyAllWindows()