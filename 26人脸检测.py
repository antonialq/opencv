import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import path_const

def face_detect_demo():
    gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    face_dector = cv.CascadeClassifier("resources/haarcascade_frontalface_alt_tree.xml")
    faces = face_dector.detectMultiScale(gray,1.02,3)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("face detection",src)

src = cv.imread(path_const.IMAGE_PATHS[2])
#cv.imshow("input image", src)
face_detect_demo()
cv.waitKey(0)

cv.destroyAllWindows()