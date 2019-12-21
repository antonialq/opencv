import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const

def watershed_demo(image):
    print(image.shape)
    blurred = cv.pyrMeanShiftFiltering(src,10,100)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary-image", binary)

    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    mb = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel,iterations=2)
    sure_bg = cv.dilate(mb,kernel,iterations=3)
    cv.imshow("mor-opt",sure_bg)

    dist = cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_output = cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    cv.imshow("distance t",dist_output*50)

    ret,surface = cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface",surface)

    surface_fg = np.uint8(surface)
    unknown = cv.subtract(sure_bg,surface_fg)
    ret,markers = cv.connectedComponents(surface_fg)
    print(ret)

    markers = markers + 1
    markers[unknown==255] = 0
    markers = cv.watershed(image,markers=markers)
    src[markers==-1] = (0,0,255)
    cv.imshow("result",image)

src = cv.imread(path_const.IMAGE_PATHS[2])
#cv.imshow("input image", src)
watershed_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()