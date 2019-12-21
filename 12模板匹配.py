import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

'''
【模板匹配】
'''
def template_demo():
    tpl = cv.imread("//opencv/eye.png")
    target = cv.imread("//opencv/test.jpeg")
    cv.imshow('template',tpl)
    cv.imshow('target',target)
    methods = [cv.TM_SQDIFF_NORMED,cv.TM_CCOEFF_NORMED,cv.TM_CCORR_NORMED]
    th,tw = tpl.shape[:2]
    for md in methods:
        print(md)
        result = cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0] + tw,tl[1] + th)
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.imshow("match-"+np.str(md),target)
        cv.imshow("match-"+np.str(md),result)


template_demo()
cv.waitKey(0)

cv.destroyAllWindows()