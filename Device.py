
import cv2
import numpy as np



def webam(cam=0):
    a=cv2.VideoCapture(cam)
    
    width= a.get(cv2.CAP_PROP_FRAME_WIDTH)
    height= a.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(height,width)
    while True:
        sucess,img =a.read()
        cv2.flip(img,-1)
        print(np.array(img).shape)
        
        cv2.imshow("video",img)
        if cv2.waitKey(20 ) & 0xFF == ord("q"):
            break


webam(5)