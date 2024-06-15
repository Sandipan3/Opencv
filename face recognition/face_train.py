import cv2 as cv
import os
import numpy as np

people=[]
for i in os.listdir(r'E:\python\face recognition\train'):
    people.append(i)

dir=r'E:\python\face recognition\train'
hc=cv.CascadeClassifier('haar_face.xml')

feature=[]
labels=[]
def create_train():

    for person in people:
        path=os.path.join(dir,person)
        label=people.index(person)

        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            face_rect=hc.detectMultiScale(gray,1.1,4)

            for(x,y,w,h) in face_rect:
                
                roi=gray[y:y+h, x:x+w]
                feature.append(roi)
                labels.append(label)

create_train()

feature=np.array(feature,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()

face_recognizer.train(feature,labels)

face_recognizer.save('face-trained.yml')

print("successful")