import os
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


def go():
    PATH = os.getcwd()
    PATH=PATH.split("\GUI")[0]
    
    os.chdir(PATH+"\Expression_detector")
    print(os.getcwd())
    import test as t
    
    t.start(0)      
    print("Button1 Clicked")
    PATH = os.getcwd()
    PATH=PATH.split("\GUI")[0]
    os.chdir(PATH+"\Expression_detector")
    import test
    global cap
    cap=cv2.VideoCapture(0)
    
    
    l1=Label(frame)
    l1.pack()
    
    while (True):
        img=cap.read()[1]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img= Image.fromarray(img)
        img= imgtk.PhotoImage(img)
        l1['image']=img
    
        window.update()
go()
