import cv2 as cv

hc=cv.CascadeClassifier('haar_face.xml')

capture=cv.VideoCapture(0)

while True:
    isTrue, frame=capture.read()
    
    if not True:
        break

    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    
    face=hc.detectMultiScale(frame,1.1,5)

    for(x,y,w,h) in face:
        cv.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),2)

    cv.imshow('video',frame)

    if cv.waitKey(20) & 0xFF==ord('g'):
        break

capture.release()
cv.destroyAllWindows()