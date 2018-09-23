# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 18:07:50 2018

@author: grex_
"""


#Face recognition

#Import the libraries
import cv2 

#loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#Defining a function that does the detections
def detect(gray, frame):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')