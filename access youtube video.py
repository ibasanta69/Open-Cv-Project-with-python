import cv2 as cp
import pafy
url="https://www.youtube.com/watch?v=PAuco4ehQUE&t=2345s"
data=pafy.new(url)
data=data.getbest(preftype='mp4')
cap=cp.VideoCapture(0)
cap.open(data.url)
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        farme=cp.resize(frame,(400,300))
        cp.imshow('youtube video',frame)
        if cp.waitKey(1) & 0xFF==ord('q'):
            break
cap.release()
cp.destroyAllWindows()