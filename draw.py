import cv2 as cv
import numpy as np

flag = np.zeros((501,501,3),dtype='uint8')

cv.imshow('flag', flag)
# blank[200:300, 300:400] = 0,0, 255
# cv.imshow('Green', blank)

cv.rectangle(flag,(0,0),(flag.shape[1]//1,flag.shape[0]//3),(0,128,255),thickness=cv.FILLED)
cv.rectangle(flag, (0,flag.shape[0]//3),(flag.shape[1],2*flag.shape[0]//3),(255,255,255),thickness=-1 )
cv.rectangle(flag, (0,2*flag.shape[0]//3), (flag.shape[1],flag.shape[0]), (0,255,0),thickness=-1 )
cv.circle(flag, (int(flag.shape[1]/2), int(flag.shape[0]/2)), 83, (255,0,0), 2)

cv.line(flag, (int(flag.shape[1]/2), int(flag.shape[0]/2)),(int(flag.shape[1]/2),flag.shape[0]//3),(255,0,0),2)
cv.line(flag, (int(flag.shape[1]/2), int(flag.shape[0]/2)),(int(flag.shape[1]/2),2*flag.shape[0]//3),(255,0,0),2)
cv.line(flag, (int(flag.shape[1]/2), int(flag.shape[0]/2)),(int(flag.shape[1]/2)-83, int(flag.shape[0]/2)),(255,0,0),2)
cv.line(flag, (int(flag.shape[1]/2), int(flag.shape[0]/2)),(int(flag.shape[1]/2)+83, int(flag.shape[0]/2)),(255,0,0),2)

cv.imshow('Rect', flag)

# cv.circle(blank, (flag.shape[1]//2,flag.shape[0]//2),radius=50, color=(0,0,255),thickness=-1)
# cv.imshow('circle',flag)

# cv.line(blank, (0,0),(250,250), color=(255,255,255), thickness=2)
# cv.imshow('line', flag)


# img = cv.imread('Pics/adiyogi_01.jpg')
# cv.imshow('Shiv', img)
cv.waitKey(0)