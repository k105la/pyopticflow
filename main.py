#!/usr/bin/env python3
import cv2
import numpy as np

feature_params = dict(maxCorners=300, qualityLevel=0.2, minDistance=2, blockSize=7)

lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

cap = cv2.VideoCapture('data/train.mp4')
color = (10, 255, 10)
ret, first_frame = cap.read()
mask = np.zeros_like(first_frame)
## convert first frame to gray scale image
prev_gray_frames = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
prev = cv2.goodFeaturesToTrack(prev_gray_frames, mask=None, **feature_params)

def process_frames(image):
    global prev_gray_frames, prev, mask

    cv2.namedWindow('Speed Challenge', flags=cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Speed Challenge', 800, 600)
    gray_frames = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _next, status, error = cv2.calcOpticalFlowPyrLK(prev_gray_frames, gray_frames, prev, None, **lk_params)
    good_old = prev[status == 1]
    good_new = _next[status == 1]

    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()

        mask = cv2.line(mask, (a,b), (c,d), color, 2)
        frame = cv2.circle(frames, (a,b), 3, color, -1)

    output = cv2.add(frame, mask)
    cv2.imshow('Speed Challenge', output)
    prev_gray_frames = gray_frames.copy()
    prev = good_new.reshape(-1, 1, 2)
    prev_gray_frames = gray_frames
    print(output)


while(cap.isOpened()):
    ret, frames = cap.read()
    if ret == True: 
        
        process_frames(frames)

        if cv2.waitKey(25) &  0xFF == ord('q'): 
            break
    else:
        break

cap.release()

