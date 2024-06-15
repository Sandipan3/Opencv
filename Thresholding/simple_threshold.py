import cv2  as cv

img=cv.imread('dog.jpg')
cv. imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threshold, thresh=cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)
print(threshold)


cv.waitKey(0)