
import cv2



def Cam(cam=0):
    a=cv2.VideoCapture(cam)
    width= a.get(cv2.CAP_PROP_FRAME_WIDTH)
    height= a.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(height,width)
    while True:
        sucess,img =a.read()
        cv2.imshow("video",img)
        if cv2.waitKey(20 ) & 0xFF == ord("q"):
            break

