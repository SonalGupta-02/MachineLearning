#!/usr/bin/python3
import  cv2

#  Start  Camera
cap=cv2.VideoCapture(2)

#  Status of Camera
while  cap.isOpened():
    status,frame=cap.read()

#  Detecting  Red Color
    redimg=cv2.inRange(frame,(0,0,0),(40,40,255))  
    cv2.imshow('liveredcolor',redimg)
    if  cv2.waitKey(10)  & 0xff  == ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
