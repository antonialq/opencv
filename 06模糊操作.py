import cv2 as cv
import numpy as np
import path_const
'''
【模糊操作】
-均值模糊
-中值模糊
-自定义模糊
【基本原理】基于离散卷积，定义好每个卷积核，不同卷积核得到不同效果，模糊是一种卷积的表现
【卷积】
'''
def blur_demo(image):
    dst = cv.blur(image,(5,5))
    cv.imshow("blur",dst)

def median_blur_demo(image):
    dst = cv.medianBlur(image,5)
    cv.imshow("blur",dst)

def custom_blur_demo(image):
    kernel = np.ones([5,5],np.float32)/25
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("blur2",dst)

src = cv.imread(path_const.IMAGE_PATHS[0])
cv.imshow("input image", src)
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()