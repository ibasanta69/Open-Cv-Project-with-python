import cv2 as cp
import pyautogui as py
import numpy
rs=py.size()
fourcc=cp.VideoWriter_fourcc(*"XVID")
output=cp.VideoWriter('C:\\Users\\Death Empire\\Desktop\\Kivy python\\hi.mp4',fourcc,60.0,rs)
cp.namedWindow("Recording",cp.WINDOW_NORMAL)
cp.resizeWindow("Recording",(600,400))
while True:
    img=py.screenshot()
    f=numpy.array(img)
    f=cp.cvtColor(f,cp.COLOR_BGR2GRAY)
    output.write(f)
    cp.imshow('recording',f)
    if cp.waitKey(1)==ord('q'):
        break
output.release()
cp.destroyAllWindows()