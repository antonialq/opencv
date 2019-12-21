import cv2 as cv
import numpy as np
import path_const

def clamp(pv):
    if pv>255:
        return 255
    if pv < 0:
        return 0
    return pv

def gaussian_noise(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            for ch in range(c):
                s = np.random.normal(0,20,3)
                b = image[row,col,0]
                g = image[row, col, 1]
                r = image[row, col, 2]
                image[row, col, 0] = clamp(b + s[0])
                image[row, col, 0] = clamp(g + s[0])
                image[row, col, 0] = clamp(r + s[0])
    cv.imshow("noise image",image)

src = cv.imread(path_const.IMAGE_PATHS[3])
cv.imshow("input image", src)
dst = cv.GaussianBlur(src, (0,0), 15)
cv.imshow("gause blur",dst)
t1 = cv.getTickCount()
#gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time cosume: %s"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()