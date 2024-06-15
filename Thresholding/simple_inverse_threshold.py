import cv2  as cv

img=cv.imread('dog.jpg')
cv. imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threshold, thresh_inv=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh',thresh_inv)
print(threshold)


cv.waitKey(0)