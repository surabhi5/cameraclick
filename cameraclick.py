# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:18:09 2018

@author: SURABHI
"""

import cv2

cap = cv2.VideoCapture(0) 
while(True):
    ret,frame = cap.read() 
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite("images.png",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()