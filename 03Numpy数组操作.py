import cv2 as cv
import numpy as np

def access_pixel(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s, height : %s, channels : %s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixels_demo", image)

def inverse(image):
    dst = cv.bitwise_not(image)
    cv.imshow("inverse demo",dst)

def create_image():
    img = np.zeros([400,400,3],np.float32)
    cv.imshow("new image",img)
    img[: ,: ,2] = np.ones([400,400])*10
    cv.imwrite("//opencv/myimage1.jpeg", img)
    

src = cv.imread("//opencv/WechatIMG1.jpeg")
cv.namedWindow("input image", cv.WINDOW_FREERATIO)
cv.imshow("input image", src)
create_image()
t1 = cv.getTickCount()
#access_pixel(src)
inverse(src)
t2 = cv.getTickCount()
print("time: %s ms"%((t2-t1)/cv.getTickFrequency()*1000))
m1 = np.ones([3,3],np.int32)
m1.fill(3)
print(m1)
cv.waitKey(0)

cv.destroyAllWindows()