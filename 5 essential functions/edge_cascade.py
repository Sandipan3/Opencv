import cv2 as cv

img=cv.imread("./dog.jpg")
cv.imshow("color",img)

edge=cv.Canny(img,125,175)
cv.imshow("edge",edge)

cv.waitKey(0)