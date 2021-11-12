# -*- coding:utf-8 -*-
"""
Created on 20211111

@author: jack rich
"""
import cv2 as cv

index = 1
video = cv.VideoCapture('v.mp4')
if video.isOpened():
    open, frame = video.read()
else:
    open = False
while open:
    ret, frame = video.read()
    if frame is None:
        break
    if ret == True:
        cv.imwrite(str('21061214_')+str(index)+'frame'+'.JPG', frame)
        index += 1
