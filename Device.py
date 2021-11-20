
import cv2
from tkinter import *
import numpy as np
from PIL import Image, ImageTk



def webcam(cam=0):
    cap=cv2.VideoCapture(cam)
    

    img=cap.read()[1]
    cv2.flip(img,-1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    arr= Image.fromarray(img)
    if cv2.waitKey(20 ) & 0xFF == ord("q"):
        break

        

webcam()