import cv2 as c
import pyautogui as p
import numpy as np
rs=p.size()
fourcc=c.VideoWriter_fourcc(*'XVID')
output=c.VideoWriter('C:\\Users\\Death Empire\\Desktop\\hhh.mp4',fourcc,100.0,rs)
c.namedWindow("Live-Video-Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live-recordeing",(400,300))
while True:
    img=p.screenshot()
    f=np.array(img)
    f=c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow('dd',f)
    if c.waitKey(1)==ord('q'):
        break
output.release()
c.destroyAllWindows()