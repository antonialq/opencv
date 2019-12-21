import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0,256])
    plt.show()

def image_demo(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0,256])
        plt.plot(hist,color=color)
        plt.xlim([0,256])
    plt.show()

src = cv.imread("//opencv/test.jpeg")
cv.imshow("input image", src)
plot_demo(src)
image_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()