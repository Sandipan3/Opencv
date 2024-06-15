import cv2 as cv

img=cv.imread("./dog.jpg")
cv.imshow("color",img)

crop=img[20:500, 200:400]
cv.imshow("crop",crop)

cv.waitKey(0)