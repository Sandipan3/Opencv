import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('dog.jpg')
cv.imshow('img', img)


blank=np.zeros((img.shape[:2]),dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2-75),150,255,-1)

mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',mask)


plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('no of pixels')

color=('b','g','r')
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],None,[256],[0,256])

    # masked color histogram
    # hist=cv.calcHist([img],[i],circle,[256],[0,256])

    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)