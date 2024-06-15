import cv2 as cv
import numpy as np
import os

hc=cv.CascadeClassifier('haar_face.xml')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face-trained.yml')

people=[]
for i in os.listdir(r'E:\python\face recognition\train'):
    people.append(i)

    
img=cv.imread(r'train\Madonna\8.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

face_rect=hc.detectMultiScale(gray,1.1,4)

for(x,y,w,h) in face_rect:

    roi=gray[y:y+h,x:x+w]

    label,confidence=face_recognizer.predict(roi)
    cv.rectangle(img, (x,y) , (x+w , y+h ), (0,255,0), 2)

    cv.putText(img, str(people[label]) ,(20,20), cv.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 2)
    cv.putText(img, str(confidence),(20,50), cv.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 2)

cv.imshow('face',img)

cv.waitKey(0)


