#!/usr/bin/env python3
import cv2
import numpy as np

cap = cv2.VideoCapture('data/train.mp4')

ret, old_frame = cap.read()

back_sub = cv2.createBackgroundSubtractorKNN()

def process_frames(image):
    cv2.namedWindow('Speed Challenge', flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Speed Challenge', 800, 600)

    fgMask = back_sub.apply(image)
    cv2.imshow('Speed Challenge', fgMask)
    print(fgMask)


while(cap.isOpened()):
    ret, frames = cap.read()
    if ret == True: 
        
        process_frames(frames)

        if cv2.waitKey(25) &  0xFF == ord('q'): 
            break
    else:
        break

cap.release()

