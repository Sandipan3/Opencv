import cv2 as cv

img=cv.imread('faces.webp')
cv.imshow('faces',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

hc=cv.CascadeClassifier('haar_face.xml')

face=hc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(len(face))


cv.waitKey(0)