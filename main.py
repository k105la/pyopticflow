#!/usr/bin/env python3
import cv2
import numpy as np

cap = cv2.VideoCapture('data/train.mp4')

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

while(1):
    ret, frame = cap.read()
    if ret == True: 
        gray_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('Speed Challenge', flags=cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Speed Challenge', 800, 600)
        cv2.imshow('Speed Challenge', gray_frames)
        if cv2.waitKey(25) &  0xFF == ord('q'): 
            break
    else:
        break

cap.release()

