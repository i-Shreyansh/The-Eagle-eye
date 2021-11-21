from tkinter import *
import sys
import os
import cv2
from PIL import Image
from PIL import ImageTk as imgtk

from keras.models import load_model
from time import sleep
from keras.preprocessing.image import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np


def btn0_clicked():
    print("Button0 Clicked")
def btn1_clicked():
    print("Button1 Clicked")
    PATH = os.getcwd()
    PATH=PATH.split("\GUI")[0]
    os.chdir(PATH+"\Expression_detector")

    global cap

    device=0
    face_classifier = cv2.CascadeClassifier('./Face_Classifier.xml')
    classifier =load_model('./Emotion_Detection.h5')
    
    class_labels = ['Angry','Happy','Neutral','Sad','Surprise']
    
    cap = cv2.VideoCapture(device)
    
    
    l1=Label(frame)
    l1.pack()
    while True:
        # Grab a single frame of video
        ret, f = cap.read()
        
        labels = []
        gray = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
    
        for (x,y,w,h) in faces:
            cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h,x:x+w]
            roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)
    
    
            if np.sum([roi_gray])!=0:
                roi = roi_gray.astype('float')/255.0
                roi = img_to_array(roi)
                roi = np.expand_dims(roi,axis=0)
    
            # make a prediction on the ROI, then lookup the class
    
                preds = classifier.predict(roi)[0]
                
                label=class_labels[preds.argmax()]
                
                label_position = (x,y)
                cv2.putText(f,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            else:
                cv2.putText(f,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            
        img=f
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img= Image.fromarray(img)
        img= imgtk.PhotoImage(img)
        l1['image']=img
        window.update()

def btn2_clicked():
    print("Button2 Clicked")
    cap.release()
    
def btn3_clicked():
    print("Button3 Clicked")
    PATH = os.getcwd()
    PATH=PATH.split("\GUI")[0]
    
    os.chdir(PATH+"\Expression_detector")
    print(os.getcwd())
    
    
    
    l1=Label(frame)
    l1.pack()
    
    
    

def btn4_clicked():
    print("Button4 Clicked")
def btn5_clicked():
    print("Button5 Clicked")
def btn6_clicked():

    print("Button6 Clicked")
    
def btn7_clicked(): #exit
    print("Button7 Clicked")
  
    os._exit(0)



window = Tk()


window.geometry("1000x711")
window.configure(bg = "#0b07ec")
canvas = Canvas(
    window,
    bg = "#0b07ec",
    height = 711,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    500.0, 355.5,
    image=background_img)


canvas.create_rectangle(
    327, 125, 327+665, 125+483,
    fill = "#c9b4e3",
    outline = "")






img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn0_clicked,
    relief = "flat")

b0.place(
    x = 426, y = 4,
    width = 148,
    height = 37)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn1_clicked,
    relief = "flat")

b1.place(
    x = 232, y = 650,
    width = 207,
    height = 58)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn2_clicked,
    relief = "flat")

b2.place(
    x = 459, y = 657,
    width = 193,
    height = 51)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn3_clicked,
    relief = "flat")

b3.place(
    x = 2, y = 4,
    width = 115,
    height = 106)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn4_clicked,
    relief = "flat")

b4.place(
    x = 285, y = 3,
    width = 131,
    height = 37)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn5_clicked,
    relief = "flat")

b5.place(
    x = 144, y = 3,
    width = 131,
    height = 37)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn6_clicked,
    relief = "flat")

b6.place(
    x = 606, y = 0,
    width = 250,
    height = 53)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn7_clicked,
    relief = "flat")

b7.place(
    x = 869, y = 3,
    width = 131,
    height = 50)

canvas.create_text(
    721.5, 26.5,
    text = "Sign up",
    fill = "#000000",
    font = ("Aclonica-Regular", int(20.0)))

canvas.create_text(
    673.0, 348.5,
    text = "Welcome to Eagle Eye",
    fill = "#000000",
    font = ("Aclonica-Regular", int(20.0)))

frame=Frame(window)
frame.pack()
frame.place(x=327,y=125, height=483, width=665)
"""
canvas2 = Canvas(
    frame,
    bg = "#0b07ec",
    height = 483,
    width = 665,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)


canvas2.create_rectangle(
    0, 0, 665, 483,
    fill = "#c9b4e3",
    outline = "")
canvas2.create_text(
    332.0, 241.5,
    text = "Welcome to Eagle Eye",
    fill = "#000000",
    font = ("Aclonica-Regular", int(20.0)))
frame=Frame(window, bg="green")
"""

window.resizable(False, False)
window.mainloop()
