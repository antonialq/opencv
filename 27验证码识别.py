import cv2 as cv
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import path_const
import pytesseract as tess

def recognize_text(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(1,2))
    bin1 = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(2,2))
    open_out = cv.morphologyEx(bin1,cv.MORPH_OPEN,kernel)
    cv.imshow("binary",open_out)

    cv.bitwise_not(open_out,open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print(text)


src = cv.imread(path_const.IMAGE_PATHS[4])
cv.imshow("input image", src)
recognize_text(src)
cv.waitKey(0)

cv.destroyAllWindows()