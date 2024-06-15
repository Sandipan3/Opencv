import cv2 as cv
import numpy as np
import os

hc=cv.CascadeClassifier('haar_face.xml')

face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face-trained.yml')

people=[]
for i in os.listdir(r'E:\python\face recognition\train'):
    people.append(i)

    
capture=cv.VideoCapture(0)

while True:
    isTrue, frame=capture.read()
    
    if not True:
        break

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face_rect=hc.detectMultiScale(frame,1.1,5)

    for(x,y,w,h) in face_rect:

        roi=gray[y:y+h,x:x+w]

        label,confidence=face_recognizer.predict(roi)
        cv.rectangle(frame, (x,y) , (x+w , y+h ), (0,255,0), 2)

        cv.putText(frame, str(people[label]) ,(150,20), cv.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 2)
        cv.putText(frame, str(confidence),(150,50), cv.FONT_HERSHEY_COMPLEX, 1 ,(0,255,0), 2)

        cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('g'):
        break

capture.release()
cv.destroyAllWindows()


