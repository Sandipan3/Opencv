import cv2 as cv

img=cv.imread('dog.jpg')
cv.imshow('img',img)

b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

merged=cv.merge([b,g,r])
cv.imshow('merge',merged)

cv.waitKey(0)