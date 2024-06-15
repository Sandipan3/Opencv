import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('dog.jpg')
cv.imshow('img', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blank=np.zeros((img.shape[:2]),dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2-75),150,255,-1)

mask=cv.bitwise_and(gray,circle)
cv.imshow('mask',mask)

hist=cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('no of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)