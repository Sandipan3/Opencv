import cv2 as cv

img=cv.imread("./dog.jpg")
cv.imshow("color",img)

resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow("resize",resize)

cv.waitKey(0)