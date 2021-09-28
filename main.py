import cv2


img="C:/Users/shrey/OneDrive/Pictures/pic.jpeg"
vid="C:/Users/shrey/OneDrive/Pictures/Camera Roll/WIN_20210903_22_56_48_Pro.mp4"

a=cv2.VideoCapture(5)


while True:
    sucess,img =a.read()
    cv2.imshow("video",img)
    if cv2.waitKey(20 ) & 0xFF == ord("q"):
        break

