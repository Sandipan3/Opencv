import cv2 as cv

img=cv.imread("./dog.jpg")
cv.imshow("color",img)

canny=cv.Canny(img,125,175)
dilate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow("dilate",dilate)

cv.waitKey(0)