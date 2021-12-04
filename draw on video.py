# draw on video in cv2
import cv2 as cp
import numpy as np
import datetime
cap=cp.VideoCapture('C:\\Users\\Death Empire\Documents\\Bandicam\\ki.mp4')
# print('width',cap.get(cp.CAP_PROP_FRAME_WIDTH))
# print('Height',cap.get(cp.CAP_PROP_FRAME_HEIGHT))
print('Width',cap.get(3))
print('Height',cap.get(4))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cp.FONT_HERSHEY_COMPLEX_SMALL
        text='Height= '+str(cap.get(4))+'Width= '+str(cap.get(3))       
        frame=cp.putText(frame,text,(10,70),font,1,(255,20,147),1,cp.LINE_AA)
        datee=('Date : '+str(datetime.datetime.now()))
        frame=cp.putText(frame,datee,(10,40),font,1,(255,20,147),1,cp.LINE_AA)
        frame = cp.rectangle(frame, (204, 220), (333, 333), (0, 255, 255), 3)
        cp.imshow('Video',frame)
        if cp.waitKey(40) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cp.destroyAllWindows()