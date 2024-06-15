import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('dog.jpg')
cv.imshow('img', img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

hist=cv.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('grayscale histogram')
plt.xlabel('bins')
plt.ylabel('no of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()


cv.waitKey(0)