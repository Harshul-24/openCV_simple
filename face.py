import cv2 as cv
import numpy as np

#face detection of an loaded image
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv.imread('Pics/msn.jpg')
cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

faces = face_cascade.detectMultiScale(gray,1.2, 3) #returned as list of coordinates of rectangle

for (x,y,w,h) in faces:
    cv.rectangle(img, (x,y),(x+w,y+h), (255,0,0),2)

cv.imshow('img', img)
cv.waitKey(0)

#from webcam
cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    grayvid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayvid,1.1, 4)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),2)
    
    cv.imshow('frame', frame)
    k = cv.waitKey(42) & 0xff
    if k ==27:
        break

cap.release


#from video

cap = cv.VideoCapture('Videos/vid1.mp4')
while True:
    isTrue, frame = cap.read()
    grayvid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayvid,1.3, 3)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),2)
    
    cv.imshow('frame', frame)
    k = cv.waitKey(42) & 0xff
    if k ==27:
        break

cap.release



    
